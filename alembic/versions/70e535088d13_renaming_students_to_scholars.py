"""Renaming students to scholars

Revision ID: 70e535088d13
Revises: 
Create Date: 2023-09-06 11:59:23.068203

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70e535088d13'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.rename_table('students', 'scholars')



def downgrade() -> None:
    op.rename_table('scholars', 'students')

