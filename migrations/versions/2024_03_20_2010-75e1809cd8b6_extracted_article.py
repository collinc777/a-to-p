"""extracted_article

Revision ID: 75e1809cd8b6
Revises: 26b53c372d47
Create Date: 2024-03-20 20:10:51.541031

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "75e1809cd8b6"
down_revision: Union[str, None] = "26b53c372d47"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "extractedarticlemodel",
        sa.Column("id", sqlmodel.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("last_edited", sa.DateTime(), nullable=True),
        sa.Column("title", sqlmodel.AutoString(), nullable=False),
        sa.Column("text", sqlmodel.AutoString(), nullable=False),
        sa.Column("author", sqlmodel.AutoString(), nullable=True),
        sa.Column("url", sqlmodel.AutoString(), nullable=True),
        sa.Column("hostname", sqlmodel.AutoString(), nullable=True),
        sa.Column("description", sqlmodel.AutoString(), nullable=True),
        sa.Column("sitename", sqlmodel.AutoString(), nullable=True),
        sa.Column("date", sqlmodel.AutoString(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column(
        "episode",
        sa.Column("extracted_article_id", sqlmodel.GUID(), nullable=True),
    )
    op.create_foreign_key(
        None, "episode", "extractedarticlemodel", ["extracted_article_id"], ["id"]
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "episode", type_="foreignkey")
    op.drop_column("episode", "extracted_article_id")
    op.drop_table("extractedarticlemodel")
    # ### end Alembic commands ###
