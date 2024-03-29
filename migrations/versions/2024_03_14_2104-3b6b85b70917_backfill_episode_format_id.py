"""backfill episode_format_id

Revision ID: 3b6b85b70917
Revises: 74b43b5662b7
Create Date: 2024-03-14 21:04:57.973072

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

from api.db import get_session_for_migrations
from api.models import Episode, EpisodeFormat, EpisodeFormatType


# revision identifiers, used by Alembic.
revision: str = "3b6b85b70917"
down_revision: Union[str, None] = "74b43b5662b7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    session = get_session_for_migrations(bind=op.get_bind())
    # backfill episode_format_id using sqlmodel
    episode_format_id = session.execute(
        sqlmodel.select(EpisodeFormat.id).where(
            EpisodeFormat.episode_format_type == EpisodeFormatType.dialogue
        )
    ).scalar_one()
    session.execute(
        sqlmodel.update(Episode)
        .where(Episode.episode_format_id == None)  # type: ignore
        .values(episode_format_id=episode_format_id)
    )

    op.drop_constraint("episodeformat_index_key", "episodeformat", type_="unique")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint("episodeformat_index_key", "episodeformat", ["index"])
    # ### end Alembic commands ###
