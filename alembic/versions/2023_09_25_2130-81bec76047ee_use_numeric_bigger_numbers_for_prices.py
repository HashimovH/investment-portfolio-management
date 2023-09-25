"""Use Numeric bigger numbers for prices

Revision ID: 81bec76047ee
Revises: 42063fd5df95
Create Date: 2023-09-25 21:30:08.708343

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81bec76047ee'
down_revision: Union[str, None] = '42063fd5df95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('clients', 'balance',
               existing_type=sa.NUMERIC(precision=6, scale=3),
               type_=sa.Numeric(precision=9, scale=3),
               existing_nullable=True)
    op.alter_column('stocks', 'price',
               existing_type=sa.NUMERIC(precision=6, scale=3),
               type_=sa.Numeric(precision=9, scale=3),
               existing_nullable=True)
    op.alter_column('transactions', 'price',
               existing_type=sa.NUMERIC(precision=6, scale=3),
               type_=sa.Numeric(precision=9, scale=3),
               existing_nullable=True)
    op.alter_column('transactions', 'purchase_price',
               existing_type=sa.NUMERIC(precision=6, scale=3),
               type_=sa.Numeric(precision=9, scale=3),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('transactions', 'purchase_price',
               existing_type=sa.Numeric(precision=9, scale=3),
               type_=sa.NUMERIC(precision=6, scale=3),
               existing_nullable=True)
    op.alter_column('transactions', 'price',
               existing_type=sa.Numeric(precision=9, scale=3),
               type_=sa.NUMERIC(precision=6, scale=3),
               existing_nullable=True)
    op.alter_column('stocks', 'price',
               existing_type=sa.Numeric(precision=9, scale=3),
               type_=sa.NUMERIC(precision=6, scale=3),
               existing_nullable=True)
    op.alter_column('clients', 'balance',
               existing_type=sa.Numeric(precision=9, scale=3),
               type_=sa.NUMERIC(precision=6, scale=3),
               existing_nullable=True)
    # ### end Alembic commands ###