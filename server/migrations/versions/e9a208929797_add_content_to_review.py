"""add content to review

Revision ID: e9a208929797
Revises: 39da31eab801
Create Date: 2024-05-15 10:29:52.260234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9a208929797'
down_revision = '39da31eab801'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews_table', schema=None) as batch_op:
        batch_op.drop_column('content')

    # ### end Alembic commands ###
