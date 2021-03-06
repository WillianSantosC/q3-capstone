"""create url_image in ImageModel

Revision ID: 9abd869ce3b8
Revises: 3d4fe6213434
Create Date: 2022-03-07 10:32:03.382061

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '9abd869ce3b8'
down_revision = '3d4fe6213434'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('images', sa.Column('url_image', sa.TEXT(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('images', 'url_image')
    # ### end Alembic commands ###
