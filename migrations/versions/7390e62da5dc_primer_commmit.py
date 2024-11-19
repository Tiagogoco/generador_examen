"""primer commmit

Revision ID: 7390e62da5dc
Revises: 
Create Date: 2024-11-13 10:05:37.894943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7390e62da5dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('estudiantes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=20), nullable=False),
    sa.Column('apellidos', sa.String(length=50), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('correo', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('apellidos'),
    sa.UniqueConstraint('correo'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('profesores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=20), nullable=False),
    sa.Column('apellidos', sa.String(length=50), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('correo', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('apellidos'),
    sa.UniqueConstraint('correo'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=20), nullable=False),
    sa.Column('apellidos', sa.String(length=50), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('correo', sa.String(length=50), nullable=False),
    sa.Column('tipo', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('apellidos'),
    sa.UniqueConstraint('correo'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('preguntas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('area', sa.String(length=20), nullable=False),
    sa.Column('definicion_operacional', sa.Text(), nullable=False),
    sa.Column('base_reactivo', sa.Text(), nullable=False),
    sa.Column('opcion1', sa.Text(), nullable=False),
    sa.Column('opcion2', sa.Text(), nullable=False),
    sa.Column('opcion3', sa.Text(), nullable=False),
    sa.Column('opcion4', sa.Text(), nullable=False),
    sa.Column('tipo_respuesta', sa.String(length=20), nullable=False),
    sa.Column('argumentacion', sa.String(length=20), nullable=False),
    sa.Column('profesor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['profesor_id'], ['profesores.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('preguntas')
    op.drop_table('usuarios')
    op.drop_table('profesores')
    op.drop_table('estudiantes')
    # ### end Alembic commands ###
