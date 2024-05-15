"""empty message

Revision ID: 39da31eab801
Revises: 
Create Date: 2024-05-15 10:28:28.920749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39da31eab801'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('publications_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('video_games_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('videogame_id', sa.Integer(), nullable=True),
    sa.Column('publication_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['publication_id'], ['publications_table.id'], name=op.f('fk_reviews_table_publication_id_publications_table')),
    sa.ForeignKeyConstraint(['videogame_id'], ['video_games_table.id'], name=op.f('fk_reviews_table_videogame_id_video_games_table')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews_table')
    op.drop_table('video_games_table')
    op.drop_table('publications_table')
    # ### end Alembic commands ###
