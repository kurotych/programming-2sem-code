"""create users table

Revision ID: 192c4b9ae498
Revises: 
Create Date: 2026-02-11 08:55:17.557097

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '192c4b9ae498'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('email', sa.String(255), unique=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now())
    )
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
