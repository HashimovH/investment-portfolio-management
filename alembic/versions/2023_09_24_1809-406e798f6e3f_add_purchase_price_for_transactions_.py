"""Add purchase price for transactions nullable

Revision ID: 406e798f6e3f
Revises: 5ac76883fe6b
Create Date: 2023-09-24 18:09:21.287142

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '406e798f6e3f'
down_revision: Union[str, None] = '5ac76883fe6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
