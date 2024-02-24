import strawberry

from fastapi import Depends
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info
from sqlalchemy.ext.asyncio import AsyncSession
from api.crud import crud_episode

from api.db import get_session
from api.models import Episode, ExtractedArticle, Transcript, TranscriptLine


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


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema, context_getter=get_context)
