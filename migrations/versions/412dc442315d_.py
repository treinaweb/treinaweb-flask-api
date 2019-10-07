"""empty message

Revision ID: 412dc442315d
Revises: f3f70b5b9872
Create Date: 2019-10-07 09:27:02.788399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '412dc442315d'
down_revision = 'f3f70b5b9872'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('senha', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    # ### end Alembic commands ###