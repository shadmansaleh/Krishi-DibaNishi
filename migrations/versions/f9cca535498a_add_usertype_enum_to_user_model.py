"""Add usertype enum to User model

Revision ID: f9cca535498a
Revises: 9e1388926ace
Create Date: 2025-01-08 15:52:09.838923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9cca535498a'
down_revision = '9e1388926ace'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usertype', sa.Enum('user', 'admin', name='usertype'), nullable=True))
    with op.batch_alter_table('user', schema=None) as batch_op:
        # Update existing rows to set a default value for usertype
        batch_op.execute("UPDATE user SET usertype='user' WHERE usertype IS NULL")
        # Alter the column to set NOT NULL
        batch_op.alter_column('usertype', nullable=False)


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('usertype')

    # ### end Alembic commands ###
