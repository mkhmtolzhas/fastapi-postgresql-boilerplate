"""create tables3

Revision ID: 9512a62e409e
Revises: 0269a1de36de
Create Date: 2025-02-08 19:54:54.366987

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9512a62e409e'
down_revision: Union[str, None] = '0269a1de36de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
