"""Created Test Table

Revision ID: 00e1b6b8f25d
Revises: 41d26240a6b1
Create Date: 2024-01-02 21:17:43.743690

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00e1b6b8f25d'
down_revision: Union[str, None] = '41d26240a6b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
