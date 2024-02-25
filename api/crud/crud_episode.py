from api.crud.crud_base import CRUDBase
from api.models import Episode, UpdateEpisodeDBInput


class CRUDEpisode(CRUDBase[Episode, Episode, UpdateEpisodeDBInput]):
    pass


crud_episode = CRUDEpisode(Episode)
