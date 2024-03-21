"""voice

Revision ID: 8eaf28088582
Revises: 2446f14a8d2a
Create Date: 2024-03-19 20:41:12.608878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '8eaf28088582'
down_revision: Union[str, None] = '2446f14a8d2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('voice',
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('last_edited', sa.DateTime(), nullable=True),
    sa.Column('speaker_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('voice_category', sa.Enum('male', 'female', 'kid', name='voicecategory'), nullable=False),
    sa.Column('provider', sa.Enum('openai', 'aws', 'playht', name='voiceprovider'), nullable=False),
    sa.Column('voice_provider_voice_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('sample_output', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voice')
    # ### end Alembic commands ###
