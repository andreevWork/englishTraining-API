"""empty message

Revision ID: 7b299b4b5121
Revises: 
Create Date: 2018-07-09 23:55:26.715461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b299b4b5121'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('serial',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('episode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('serial_id', sa.Integer(), nullable=False),
    sa.Column('season', sa.Integer(), nullable=False),
    sa.Column('episode', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('videoSrc', sa.String(length=120), nullable=False),
    sa.Column('previewImageSrc', sa.String(length=120), nullable=True),
    sa.Column('subtitleSrc', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['serial_id'], ['serial.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('episode')
    op.drop_table('serial')
    # ### end Alembic commands ###