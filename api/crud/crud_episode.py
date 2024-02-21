from api.crud.crud_base import CRUDBase
from api.models import Episode


class CRUDEpisode(CRUDBase[Episode, Episode, Episode]):
    pass


crud_episode = CRUDEpisode(Episode)
