"""create tables

Revision ID: 0942cf789ea6
Revises: 139c424dcf04
Create Date: 2025-02-08 19:52:06.607767

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0942cf789ea6'
down_revision: Union[str, None] = '139c424dcf04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
