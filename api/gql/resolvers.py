import uuid
import strawberry

from fastapi import Depends
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info
from sqlalchemy.ext.asyncio import AsyncSession
from api.crud import crud_episode

from api.db import get_session
from api.longform_episode_generator import (
    extract_article,
    generate_episode_audio_task,
    generate_episode_task,
)
from api.models import (
    CreateEpisodeRequest,
    Episode,
    ExtractedArticle,
    Transcript,
    TranscriptLine,
    UpdateEpisodeInput as UpdateEpisodeInputPydantic,
)


async def get_context(
    session: AsyncSession = Depends(get_session),
):
    return {"session": session}


@strawberry.experimental.pydantic.type(model=ExtractedArticle, all_fields=True)
class ExtractedArticleType:
    pass


@strawberry.experimental.pydantic.type(model=TranscriptLine, all_fields=True)
class TranscriptLineType:
    pass


@strawberry.experimental.pydantic.type(model=Transcript, all_fields=True)
class TranscriptType:
    pass


@strawberry.experimental.pydantic.type(model=Episode, all_fields=True)
class EpisodeType:
    pass


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    async def episode(self, id: str, info: Info) -> EpisodeType:
        db = info.context["session"]
        episode = await crud_episode.get(db, id)
        if not episode:
            return "Episode not found"
        return EpisodeType.from_pydantic(episode)


@strawberry.experimental.pydantic.input(ExtractedArticle, all_fields=True)
class UpdateExtractedArticleInput:
    pass


@strawberry.experimental.pydantic.input(TranscriptLine, all_fields=True)
class UpdateTranscriptLineInput:
    pass


@strawberry.experimental.pydantic.input(Transcript, all_fields=True)
class UpdateTranscriptInput:
    pass


@strawberry.experimental.pydantic.input(UpdateEpisodeInputPydantic, all_fields=True)
class UpdateEpisodeInput:
    pass


@strawberry.experimental.pydantic.input(CreateEpisodeRequest, all_fields=True)
class CreateEpisodeInput:
    pass


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def update_episode(
        self, id: str, input: UpdateEpisodeInput, info: Info
    ) -> EpisodeType:
        db = info.context["session"]
        episode = await crud_episode.get(db, id)
        if not episode:
            return "Episode not found"

        pydantic_input = input.to_pydantic()
        # remove none
        pydantic_input = pydantic_input.model_dump(exclude_none=True)
        pydantic_input = UpdateEpisodeInputPydantic(**pydantic_input)

        episode = await crud_episode.update(db, db_obj=episode, obj_in=pydantic_input)
        return EpisodeType.from_pydantic(episode)

    @strawberry.mutation
    async def generate_episode_audio(self, episode_id: str, info: Info) -> EpisodeType:
        background_tasks = info.context["background_tasks"]
        session = info.context["session"]
        episode = await crud_episode.get(session, episode_id)
        if episode is None:
            raise ValueError("Episode not found")
        episode = await crud_episode.update(
            session, db_obj=episode, obj_in={"status": "generating_audio"}
        )
        background_tasks.add_task(generate_episode_audio_task, episode.id)
        return EpisodeType.from_pydantic(episode)

    @strawberry.mutation
    async def create_episode_creation_task(
        self, input: CreateEpisodeInput, info: Info
    ) -> EpisodeType:
        session = info.context["session"]
        id = uuid.uuid4()
        article = None
        article_text = ""
        if input.article_url:
            article = extract_article(input.article_url)
            article_text = article.text

        if input.article_text:
            article_text = input.article_text

        print(str(id))
        episode = Episode(
            id=id,
            status="started",
            url="",
            article_text=article_text,
            title=article.title if article and article.title else "Untitled",
            extracted_article=article,
        )
        session.add(episode)
        await session.commit()
        await session.refresh(episode)
        background_tasks = info.context["background_tasks"]
        background_tasks.add_task(generate_episode_task, str(id))
        return episode


schema = strawberry.Schema(Query, Mutation)

graphql_app = GraphQLRouter(schema, context_getter=get_context)
