"""empty message

Revision ID: 9fd370a3f1ac
Revises: eaaaca255142
Create Date: 2024-06-16 23:07:07.259175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fd370a3f1ac'
down_revision = 'eaaaca255142'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('busines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('base_url', sa.String(length=150), nullable=True),
    sa.Column('metrica_html', sa.String(length=300), nullable=True),
    sa.Column('zone_html', sa.String(length=300), nullable=True),
    sa.Column('info', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('base_url')
    )
    op.create_table('home',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('base_url', sa.String(length=150), nullable=True),
    sa.Column('metrica_html', sa.String(length=300), nullable=True),
    sa.Column('zone_html', sa.String(length=300), nullable=True),
    sa.Column('tariffs', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('base_url')
    )
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=True),
    sa.Column('info', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('static_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('base_url', sa.String(length=150), nullable=True),
    sa.Column('info', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('base_url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('static_info')
    op.drop_table('news')
    op.drop_table('home')
    op.drop_table('busines')
    # ### end Alembic commands ###