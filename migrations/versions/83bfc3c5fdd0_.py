"""empty message

Revision ID: 83bfc3c5fdd0
Revises: 9fd370a3f1ac
Create Date: 2024-06-18 22:35:21.179867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83bfc3c5fdd0'
down_revision = '9fd370a3f1ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('advanced',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('price', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('advanced')
    # ### end Alembic commands ###