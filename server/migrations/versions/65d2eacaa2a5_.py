"""empty message

Revision ID: 65d2eacaa2a5
Revises: e9a208929797
Create Date: 2024-05-15 10:31:03.560130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65d2eacaa2a5'
down_revision = 'e9a208929797'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews_table', schema=None) as batch_op:
        batch_op.drop_column('content')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###
