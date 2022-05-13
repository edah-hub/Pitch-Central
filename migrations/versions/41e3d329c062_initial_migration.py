"""Initial Migration

Revision ID: 41e3d329c062
Revises: 963e2a49b38b
Create Date: 2022-05-12 11:47:26.335346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41e3d329c062'
down_revision = '963e2a49b38b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###
