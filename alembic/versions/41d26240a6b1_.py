"""empty message

Revision ID: 41d26240a6b1
Revises: 7faeb9df9ed0
Create Date: 2024-01-02 21:07:31.342464

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41d26240a6b1'
down_revision: Union[str, None] = '7faeb9df9ed0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
