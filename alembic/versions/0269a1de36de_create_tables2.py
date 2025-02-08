"""create tables2

Revision ID: 0269a1de36de
Revises: 0942cf789ea6
Create Date: 2025-02-08 19:53:21.002569

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0269a1de36de'
down_revision: Union[str, None] = '0942cf789ea6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
