"""Initial Migration

Revision ID: 8d8aec25ad71
Revises: 6f9236ed2ef5
Create Date: 2020-06-12 00:11:04.101877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d8aec25ad71'
down_revision = '6f9236ed2ef5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('pass_hash', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'pass_hash')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
