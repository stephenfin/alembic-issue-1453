"""Rename table

Revision ID: 5e66dbc04b84
Revises: 5126ca89a0d0
Create Date: 2024-04-05 12:17:05.473881
"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '5e66dbc04b84'
down_revision = '5126ca89a0d0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("messages") as batch_op:
        batch_op.rename_table("messages", "message")
