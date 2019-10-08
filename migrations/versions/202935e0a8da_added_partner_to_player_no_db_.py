"""added partner to Player: no db.relationship

Revision ID: 202935e0a8da
Revises: 
Create Date: 2019-07-21 19:29:24.227391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '202935e0a8da'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.Column('partner_name', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['table_id'], ['table.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('partner_name')
    )
    op.create_index(op.f('ix_player_username'), 'player', ['username'], unique=True)
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('suit', sa.String(length=80), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('state', sa.String(length=80), nullable=True),
    sa.Column('player_name', sa.String(length=80), nullable=True),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player_name'], ['player.username'], ),
    sa.ForeignKeyConstraint(['table_id'], ['table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_card_number'), 'card', ['number'], unique=False)
    op.create_index(op.f('ix_card_suit'), 'card', ['suit'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_card_suit'), table_name='card')
    op.drop_index(op.f('ix_card_number'), table_name='card')
    op.drop_table('card')
    op.drop_index(op.f('ix_player_username'), table_name='player')
    op.drop_table('player')
    op.drop_table('table')
    # ### end Alembic commands ###