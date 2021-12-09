"""merging two heads

Revision ID: 76081240a9e0
Revises: c1f9e0df0545, e46d81ea3d1a
Create Date: 2021-12-07 08:52:17.787430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76081240a9e0'
down_revision = ('c1f9e0df0545', 'e46d81ea3d1a')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
