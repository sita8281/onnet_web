"""empty message

Revision ID: ed920cbce672
Revises: 110bfcd6bf36
Create Date: 2024-06-19 19:11:57.750457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed920cbce672'
down_revision = '110bfcd6bf36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('connect_conditions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=100), nullable=True),
    sa.Column('info', sa.String(length=300), nullable=True),
    sa.Column('img', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('devices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('info', sa.String(length=300), nullable=True),
    sa.Column('params', sa.String(length=300), nullable=True),
    sa.Column('img', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=100), nullable=True),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('name_url', sa.String(length=100), nullable=True),
    sa.Column('info', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('info')
    op.drop_table('devices')
    op.drop_table('connect_conditions')
    # ### end Alembic commands ###