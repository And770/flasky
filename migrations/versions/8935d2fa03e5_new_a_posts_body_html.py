"""new a posts.body_html

Revision ID: 8935d2fa03e5
Revises: a15330a542d9
Create Date: 2018-01-24 23:27:42.640537

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8935d2fa03e5'
down_revision = 'a15330a542d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###