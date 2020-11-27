"""empty message

Revision ID: 5deb5405adf0
Revises: 225949876d96
Create Date: 2020-11-27 17:14:15.162810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5deb5405adf0'
down_revision = '225949876d96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cart_id'), 'cart', ['id'], unique=False)
    op.create_table('cartproduct',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id', 'cart_id', 'product_id')
    )
    op.create_index(op.f('ix_cartproduct_id'), 'cartproduct', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cartproduct_id'), table_name='cartproduct')
    op.drop_table('cartproduct')
    op.drop_index(op.f('ix_cart_id'), table_name='cart')
    op.drop_table('cart')
    # ### end Alembic commands ###
