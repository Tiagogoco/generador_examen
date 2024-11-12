from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), unique=True, nullable=False)
    apellidos = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    correo = db.Column(db.String(50), unique=True, nullable=False)  # Corregido a db.String
    tipo = db.Column(db.String(20))  # Campo para la herencia de tabla única

    __mapper_args__ = {
        'polymorphic_identity': 'usuario',
        'polymorphic_on': tipo
    }

class Estudiante(Usuario):
    __tablename__ = 'estudiantes'
    id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'estudiante',
    }

class Profesor(Usuario):
    __tablename__ = 'profesores'
    id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)

    # Relación con las preguntas
    preguntas = db.relationship('Pregunta', back_populates='profesor', lazy=True)

    __mapper_args__ = {
        'polymorphic_identity': 'profesor',
    }

    def __repr__(self):
        return f'<Profesor {self.nombre}>'

class Pregunta(db.Model):
    __tablename__ = 'preguntas'
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(20), nullable=False)
    definicion_operacional = db.Column(db.Text, nullable=False)
    base_reactivo = db.Column(db.Text, nullable=False)
    opcion1 = db.Column(db.Text, nullable=False)
    opcion2 = db.Column(db.Text, nullable=False)
    opcion3 = db.Column(db.Text, nullable=False)
    opcion4 = db.Column(db.Text, nullable=False)
    tipo_respuesta = db.Column(db.String(20), nullable=False)
    argumentacion = db.Column(db.String(20), nullable=False)

    # Llave foránea para relacionar la pregunta con un profesor
    profesor_id = db.Column(db.Integer, db.ForeignKey('profesores.id'), nullable=False)

    # Relación inversa
    profesor = db.relationship('Profesor', back_populates='preguntas')

    def __repr__(self):
        return f'<Pregunta {self.texto[:30]}...>'
