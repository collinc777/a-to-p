from sqlmodel import SQLModel
from api.crud.crud_base import CRUDBase
from api.models import EpisodeFormat


class CRUDEpisodeFormat(CRUDBase[EpisodeFormat, EpisodeFormat, SQLModel]):
    pass


crud_episode_format = CRUDEpisodeFormat(EpisodeFormat)
