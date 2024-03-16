"""make episode format non nullable

Revision ID: 2446f14a8d2a
Revises: 3b6b85b70917
Create Date: 2024-03-15 17:18:18.768828

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '2446f14a8d2a'
down_revision: Union[str, None] = '3b6b85b70917'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('episode', 'episode_format_id',
               existing_type=sa.UUID(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('episode', 'episode_format_id',
               existing_type=sa.UUID(),
               nullable=True)
    # ### end Alembic commands ###
