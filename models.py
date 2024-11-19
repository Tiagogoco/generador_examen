from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), unique=True, nullable=False)
    apellidos = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    correo = db.Column(db.String(50), unique=True, nullable=False)
    tipo = db.Column(db.String(20))  # Campo para distinguir entre tipos de usuario

    __mapper_args__ = {
        'polymorphic_identity': 'usuario',
        'polymorphic_on': tipo
    }

class Estudiante(db.Model):
    __tablename__ = 'estudiantes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), unique=True, nullable=False)
    apellidos = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    correo = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Estudiante {self.nombre}>'

class Profesor(db.Model):
    __tablename__ = 'profesores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), unique=True, nullable=False)
    apellidos = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    correo = db.Column(db.String(50), unique=True, nullable=False)

    # Relación con las preguntas
    preguntas = db.relationship('Pregunta', back_populates='profesor', lazy=True)

    def __repr__(self):
        return f'<Profesor {self.nombre}>'

class Pregunta(db.Model):
    __tablename__ = 'preguntas'
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(100), nullable=False)  # Aumenta el límite si es necesario
    definicion_operacional = db.Column(db.String(255), nullable=False)  # Ajusta el tamaño
    base_reactivo = db.Column(db.String(255), nullable=False)
    opcion1 = db.Column(db.String(100), nullable=False)  # Asegúrate de que las opciones tengan suficiente espacio
    opcion2 = db.Column(db.String(100), nullable=False)
    opcion3 = db.Column(db.String(100), nullable=False)
    opcion4 = db.Column(db.String(100), nullable=False)
    tipo_respuesta = db.Column(db.String(50), nullable=False)  # Aumenta si es necesario
    argumentacion = db.Column(db.Text, nullable=True)  # Usa `Text` si puede ser muy larga
    respuesta_correcta = db.Column(db.String(50), nullable=False) # Ajusta según el valor máximo esperado
    # Llave foránea para relacionar la pregunta con un profesor
    profesor_id = db.Column(db.Integer, db.ForeignKey('profesores.id'), nullable=False)

    # Relación inversa
    profesor = db.relationship('Profesor', back_populates='preguntas')

    def __repr__(self):
        return f'<Pregunta {self.area}>'
