"""add episode format

Revision ID: 74b43b5662b7
Revises: aeb973378351
Create Date: 2024-03-14 19:35:25.221505

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

from api.db import get_session_for_migrations
from api.models import EpisodeFormat, EpisodeFormatType


# revision identifiers, used by Alembic.
revision: str = "74b43b5662b7"
down_revision: Union[str, None] = "aeb973378351"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "episodeformat",
        sa.Column("id", sqlmodel.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("last_edited", sa.DateTime(), nullable=True),
        sa.Column("display_value", sqlmodel.AutoString(), nullable=False),
        sa.Column("index", sa.Integer(), nullable=False),
        sa.Column(
            "episode_format_type",
            sa.Enum(
                "monologue",
                "dialogue",
                "interview",
                "panel",
                "educational",
                "storytelling",
                "news_current_events",
                "tts",
                name="episodeformattype",
            ),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("display_value"),
        sa.UniqueConstraint("episode_format_type"),
        sa.UniqueConstraint("index"),
    )
    op.add_column(
        "episode",
        sa.Column("episode_format_id", sqlmodel.GUID(), nullable=True),
    )
    op.create_foreign_key(
        None, "episode", "episodeformat", ["episode_format_id"], ["id"]
    )
    backfill()


def backfill():
    session = get_session_for_migrations(bind=op.get_bind())

    obj_in = [
        EpisodeFormat(
            display_value="Co-hosted (Dialogue)",
            episode_format_type=EpisodeFormatType.dialogue,
            index=0,
        ),
        EpisodeFormat(
            display_value="Monologue (Solo)",
            episode_format_type=EpisodeFormatType.monologue,
            index=1,
        ),
        EpisodeFormat(
            display_value="Interview",
            episode_format_type=EpisodeFormatType.interview,
            index=2,
        ),
        EpisodeFormat(
            display_value="Panel",
            episode_format_type=EpisodeFormatType.panel,
            index=3,
        ),
        EpisodeFormat(
            display_value="Educational",
            episode_format_type=EpisodeFormatType.educational,
            index=4,
        ),
        EpisodeFormat(
            display_value="Narrative Storytelling",
            episode_format_type=EpisodeFormatType.storytelling,
            index=5,
        ),
        EpisodeFormat(
            display_value="News and Current Events",
            episode_format_type=EpisodeFormatType.news_current_events,
            index=6,
        ),
    ]
    session.add_all(obj_in)
    session.commit()


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("episode", "episode_format_id")
    op.drop_table("episodeformat")
    op.execute("DROP TYPE episodeformattype")

    # ### end Alembic commands ###
