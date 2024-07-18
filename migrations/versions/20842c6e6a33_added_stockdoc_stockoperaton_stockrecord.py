"""added StockDoc StockOperaton StockRecord

Revision ID: 20842c6e6a33
Revises: 57b757d63afa
Create Date: 2024-07-18 12:28:43.973789

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20842c6e6a33'
down_revision: Union[str, None] = '57b757d63afa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock_operations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('oper_type', sa.String(length=100), nullable=False),
    sa.Column('oper_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('oper_name'),
    sa.UniqueConstraint('oper_type')
    )
    op.create_index(op.f('ix_stock_operations_id'), 'stock_operations', ['id'], unique=False)
    op.create_table('stock_docs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doc_date', sa.Date(), nullable=False),
    sa.Column('autor_id', sa.Integer(), nullable=False),
    sa.Column('doc_number', sa.String(length=20), nullable=False),
    sa.Column('oper_id', sa.Integer(), nullable=False),
    sa.Column('note', sa.String(length=150), nullable=False),
    sa.ForeignKeyConstraint(['autor_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['oper_id'], ['stock_operations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stock_docs_id'), 'stock_docs', ['id'], unique=False)
    op.create_table('stock_records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doc_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.DECIMAL(precision=14, scale=3), nullable=False),
    sa.Column('price', sa.DECIMAL(precision=14, scale=4), nullable=False),
    sa.Column('note', sa.String(length=150), nullable=False),
    sa.ForeignKeyConstraint(['doc_id'], ['stock_docs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stock_records_id'), 'stock_records', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stock_records_id'), table_name='stock_records')
    op.drop_table('stock_records')
    op.drop_index(op.f('ix_stock_docs_id'), table_name='stock_docs')
    op.drop_table('stock_docs')
    op.drop_index(op.f('ix_stock_operations_id'), table_name='stock_operations')
    op.drop_table('stock_operations')
    # ### end Alembic commands ###
