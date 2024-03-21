from sqlmodel import SQLModel
from api.crud.crud_base import CRUDBase
from api.models import Voice


class CRUDVoice(CRUDBase[Voice, Voice, SQLModel]):
    pass


crud_voice = CRUDVoice(Voice)
