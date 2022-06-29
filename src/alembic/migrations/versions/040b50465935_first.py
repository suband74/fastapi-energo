"""First

Revision ID: 040b50465935
Revises: 
Create Date: 2022-06-29 04:18:08.006154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '040b50465935'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('devices',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('dev_id', sa.String(length=200), nullable=False),
    sa.Column('dev_type', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('devices_dev_id_dev_type_index', 'devices', ['dev_id', 'dev_type'], unique=False)
    op.create_table('endpoints',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('device_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['device_id'], ['devices.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('endpoints')
    op.drop_index('devices_dev_id_dev_type_index', table_name='devices')
    op.drop_table('devices')
    # ### end Alembic commands ###