"""update Migration

Revision ID: 4959120ae0f5
Revises: ecca59dba4cd
Create Date: 2022-05-09 15:30:59.862421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4959120ae0f5'
down_revision = 'ecca59dba4cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_constraint('users_username_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    # ### end Alembic commands ###
