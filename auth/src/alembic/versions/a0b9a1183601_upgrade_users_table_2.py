"""upgrade users table 2

Revision ID: a0b9a1183601
Revises: 4f9667ac33ed
Create Date: 2022-11-25 21:20:41.754633

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a0b9a1183601"
down_revision = "4f9667ac33ed"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("confirmed", sa.Boolean(), nullable=False))
    op.add_column("users", sa.Column("confirmed_on", sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "confirmed_on")
    op.drop_column("users", "confirmed")
    # ### end Alembic commands ###