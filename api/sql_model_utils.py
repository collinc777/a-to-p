import json

# https://github.com/tiangolo/sqlmodel/issues/63#issuecomment-1081555082
from pydantic import parse_obj_as
from sqlmodel import JSON, TypeDecorator
from typing import Generic, TypeVar
from pydantic._internal._model_construction import ModelMetaclass
from fastapi.encoders import jsonable_encoder

T = TypeVar("T")


def pydantic_column_type(pydantic_type):
    class PydanticJSONType(TypeDecorator, Generic[T]):
        impl = JSON()

        def __init__(
            self,
            json_encoder=json,
        ):
            self.json_encoder = json_encoder
            super(PydanticJSONType, self).__init__()

        def bind_processor(self, dialect):  # type: ignore
            impl_processor = self.impl.bind_processor(dialect)  # type: ignore
            dumps = self.json_encoder.dumps
            if impl_processor:

                def process(value: T):  # type: ignore
                    if value is not None:
                        if isinstance(pydantic_type, ModelMetaclass):
                            # This allows to assign non-InDB models and if they're
                            # compatible, they're directly parsed into the InDB
                            # representation, thus hiding the implementation in the
                            # background. However, the InDB model will still be returned
                            value_to_dump = pydantic_type.model_validate(value)  # type: ignore
                        else:
                            value_to_dump = value
                        value = jsonable_encoder(value_to_dump)
                    return impl_processor(value)

            else:

                def process(value):
                    if isinstance(pydantic_type, ModelMetaclass):
                        # This allows to assign non-InDB models and if they're
                        # compatible, they're directly parsed into the InDB
                        # representation, thus hiding the implementation in the
                        # background. However, the InDB model will still be returned
                        value_to_dump = pydantic_type.model_validate(value)  # type: ignore
                    else:
                        value_to_dump = value
                    value = dumps(jsonable_encoder(value_to_dump))
                    return value

            return process

        def result_processor(self, dialect, coltype) -> T:  # type: ignore
            impl_processor = self.impl.result_processor(dialect, coltype)  # type: ignore
            if impl_processor:

                def process(value):
                    value = impl_processor(value)
                    if value is None:
                        return None

                    data = value
                    # Explicitly use the generic directly, not type(T)
                    full_obj = parse_obj_as(pydantic_type, data)
                    return full_obj

            else:

                def process(value):
                    if value is None:
                        return None

                    # Explicitly use the generic directly, not type(T)
                    full_obj = parse_obj_as(pydantic_type, value)
                    return full_obj

            return process  # type: ignore

        def compare_values(self, x, y):
            return x == y

    return PydanticJSONType
