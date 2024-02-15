"""title and extracted article

Revision ID: 6109750d40a5
Revises: 3ec1ef0957de
Create Date: 2024-02-14 21:11:11.316314

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '6109750d40a5'
down_revision: Union[str, None] = '3ec1ef0957de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
