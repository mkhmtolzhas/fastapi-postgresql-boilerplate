"""create tables4

Revision ID: dfcfb5b4994d
Revises: 9512a62e409e
Create Date: 2025-02-08 19:55:12.792694

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfcfb5b4994d'
down_revision: Union[str, None] = '9512a62e409e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
