from api.crud.crud_base import CRUDBase
from api.models import Episode, UpdateEpisodeInput


class CRUDEpisode(CRUDBase[Episode, Episode, UpdateEpisodeInput]):
    pass


crud_episode = CRUDEpisode(Episode)
