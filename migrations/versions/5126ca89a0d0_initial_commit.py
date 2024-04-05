"""Initial commit

Revision ID: 5126ca89a0d0
Revises:
Create Date: 2024-04-05 12:13:20.492291
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5126ca89a0d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'messages',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('message', sa.String(255), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('messages')
