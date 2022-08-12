"""empty message

Revision ID: 3926a41dc39e
Revises: 
Create Date: 2022-08-12 19:33:31.006663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3926a41dc39e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('persons', sa.Column('age', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('persons', 'age')
    # ### end Alembic commands ###
