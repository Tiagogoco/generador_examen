"""Agregar campo respuesta_correcta a Pregunta

Revision ID: b32b2c399d7d
Revises: 7390e62da5dc
Create Date: 2024-11-14 10:03:52.252504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b32b2c399d7d'
down_revision = '7390e62da5dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('preguntas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('respuesta_correcta', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('preguntas', schema=None) as batch_op:
        batch_op.drop_column('respuesta_correcta')

    # ### end Alembic commands ###
