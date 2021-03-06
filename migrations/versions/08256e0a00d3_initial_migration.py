"""Initial Migration

Revision ID: 08256e0a00d3
Revises: ce65138c9812
Create Date: 2020-06-12 14:46:00.995200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08256e0a00d3'
down_revision = 'ce65138c9812'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'pass_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###
