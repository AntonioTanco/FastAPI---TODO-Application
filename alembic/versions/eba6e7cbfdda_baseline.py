"""Baseline

Revision ID: eba6e7cbfdda
Revises: 5038b968e2ed
Create Date: 2024-01-03 03:56:43.072579

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eba6e7cbfdda'
down_revision: Union[str, None] = '5038b968e2ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
