"""Added User Table

Revision ID: 28de6d4d3696
Revises: 00e1b6b8f25d
Create Date: 2024-01-03 03:27:00.190244

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28de6d4d3696'
down_revision: Union[str, None] = '00e1b6b8f25d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
