import uuid
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import StreamingResponse
from api.crud import crud_episode
from api.db import get_session

from api.longform_episode_generator import (
    generate_episode_task,
)
from typing import Annotated, Optional
from fastapi import BackgroundTasks, Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn
from pydantic import BaseModel, model_validator
from dotenv import load_dotenv
from api.models import Episode, ExtractedArticle, Transcript, UpdateEpisodeInput
import sentry_sdk
from api.settings import Settings, get_settings
from api.gql.resolvers import graphql_app


load_dotenv()


sentry_sdk.init(
    dsn=get_settings().sentry_dsn,
    traces_sample_rate=0.0,
    profiles_sample_rate=0.0,
)


app = FastAPI()

app.include_router(graphql_app, prefix="/graphql")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/python")
def hello_world(settings: Annotated[Settings, Depends(get_settings)]):
    # print the environment

    return {"message": "hello world"}


class CreateEpisodeRequest(BaseModel):
    article_text: Optional[str] = None
    article_url: Optional[str] = None
    # either article_text or article_url must be provided

    @model_validator(mode="after")
    def check_article_text_or_url(self):
        article_text, article_url = (self.article_text, self.article_url)
        if not article_text and not article_url:
            raise ValueError("Either article_text or article_url must be provided")
        return self


@app.post("/api/episode_create_task")
async def episode_create_task(
    create_episode_request: CreateEpisodeRequest,
    background_tasks: BackgroundTasks,
    session: AsyncSession = Depends(get_session),
) -> Episode:
    id = uuid.uuid4()
    article = None
    article_text = ""
    if create_episode_request.article_url:
        article = extract_article(create_episode_request.article_url)
        article_text = article.text

    if create_episode_request.article_text:
        article_text = create_episode_request.article_text

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
    background_tasks.add_task(generate_episode_task, str(id))
    return episode


@app.get("/api/episode/{id}")
async def episode_get(
    id: str,
    settings: Annotated[Settings, Depends(get_settings)],
    session: AsyncSession = Depends(get_session),
) -> Episode:
    episode = await crud_episode.get(session, uuid.UUID(id))
    if episode is None:
        return Episode(
            title="Not found",
            id=uuid.UUID(id),
            status="not found",
            url="",
            article_text="",
        )
    return episode


@app.patch("/api/episode/{id}")
async def episode_patch(
    id: str,
    update_episode_input: UpdateEpisodeInput,
    session: AsyncSession = Depends(get_session),
) -> Episode:
    episode = await crud_episode.get(session, uuid.UUID(id))
    if episode is None:
        raise ValueError("Episode not found")
    episode = await crud_episode.update(
        session, db_obj=episode, obj_in=update_episode_input
    )
    return episode


def extract_article(url: str) -> ExtractedArticle:
    import trafilatura

    response = trafilatura.fetch_url(url)
    if not isinstance(response, str):
        raise Exception("response is not a string")

    t = trafilatura.bare_extraction(response)
    article = ExtractedArticle.model_validate(t)
    return article


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # hello_world()


if __name__ == "__main__":
    main()
