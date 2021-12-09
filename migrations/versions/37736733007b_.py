"""empty message

Revision ID: 37736733007b
Revises: 57d000520ed4
Create Date: 2021-12-09 14:53:43.256133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37736733007b'
down_revision = '57d000520ed4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('skills', sa.String(), nullable=False))
    op.drop_constraint('events_sponsors_id_fkey', 'events', type_='foreignkey')
    op.drop_constraint('events_skills_id_fkey', 'events', type_='foreignkey')
    op.create_foreign_key(None, 'events', 'company', ['sponsors_id'], ['id'])
    op.drop_column('events', 'skills_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('skills_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.create_foreign_key('events_skills_id_fkey', 'events', 'skills', ['skills_id'], ['id'])
    op.create_foreign_key('events_sponsors_id_fkey', 'events', 'sponsors', ['sponsors_id'], ['id'])
    op.drop_column('events', 'skills')
    # ### end Alembic commands ###