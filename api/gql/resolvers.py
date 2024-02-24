import strawberry

from fastapi import Depends
from strawberry.fastapi import GraphQLRouter
from sqlalchemy.ext.asyncio import AsyncSession

from api.db import get_session


async def get_context(
    session: AsyncSession = Depends(get_session),
):
    return {"session": session}


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)
