"""empty message

Revision ID: 31911b6b5e2e
Revises: 5deb5405adf0
Create Date: 2020-11-27 17:28:35.655143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31911b6b5e2e'
down_revision = '5deb5405adf0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prdseller', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('prdseller', 'is_active')
    # ### end Alembic commands ###