import uuid
from fastapi.middleware.cors import CORSMiddleware

from api.crud import crud_episode
from api.db import get_session

from typing import Annotated
from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn
from dotenv import load_dotenv
from api.models import Episode, EpisodeStatus
import sentry_sdk
from api.settings import Settings, get_settings
from api.gql.resolvers import graphql_app
from sentry_sdk.integrations.strawberry import StrawberryIntegration


load_dotenv()

if get_settings().stage == "production":
    sentry_sdk.init(
        dsn=get_settings().sentry_dsn,
        traces_sample_rate=0.0,
        profiles_sample_rate=0.0,
        send_default_pii=True,
        integrations=[
            StrawberryIntegration(
                async_execution=True,
            ),
        ],
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
            status=EpisodeStatus.not_found,
            url="",
            article_text="",
        )
    return episode


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # hello_world()


if __name__ == "__main__":
    main()
