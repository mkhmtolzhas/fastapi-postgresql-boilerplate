"""creating tables

Revision ID: 4da1d97e677c
Revises: dfcfb5b4994d
Create Date: 2025-02-08 19:58:06.960496

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4da1d97e677c'
down_revision: Union[str, None] = 'dfcfb5b4994d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
