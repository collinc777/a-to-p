from typing import Any, Dict, Generic, List, Optional, Sequence, Type, TypeVar, Union
from uuid import UUID

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlmodel import Column, desc, SQLModel, select
from sqlalchemy.ext.asyncio import AsyncSession as Session

from api.models import SQLModelBaseModel


ModelType = TypeVar("ModelType", bound=SQLModelBaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    async def get(self, db: Session, id: str | UUID) -> Optional[ModelType]:
        if isinstance(id, str):
            id = UUID(id)
        result = await db.execute(select(self.model).where(self.model.id == id))
        return result.scalars().first()

    async def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> Sequence[ModelType]:
        result = await db.execute(select(self.model).offset(skip).limit(limit))
        return result.scalars().all()

    async def filter(
        self, db: Session, *, skip: int = 0, limit: int = 100, order_by=None, **kwargs
    ) -> Sequence[ModelType]:
        result = await db.execute(
            select(self.model)
            .filter_by(**kwargs)
            .order_by(order_by)
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()

    async def create_many(
        self, db: Session, *, obj_in: List[CreateSchemaType]
    ) -> List[ModelType]:
        db_objs = [self.model(**jsonable_encoder(obj)) for obj in obj_in]
        db.add_all(db_objs)
        await db.commit()
        return db_objs

    async def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def remove(self, db: Session, *, id: int) -> Optional[ModelType]:
        obj = await self.get(db, id=id)
        if obj:
            await db.delete(obj)
            await db.commit()
            return obj

    async def get_all(self, db: Session) -> Sequence[ModelType]:
        result = await db.execute(select(self.model))
        return result.scalars().all()

    async def get_recent(
        self, db: Session, order_by: Column, page: int = 0, per_page: int = 10
    ) -> Sequence[ModelType]:
        result = await db.execute(
            select(self.model)
            .order_by(desc(order_by))
            .offset(page * per_page)
            .limit(per_page)
        )
        return result.scalars().all()
