from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Profesor, Estudiante, db, Usuario, Pregunta  # Asegúrate de que estos modelos están definidos correctamente

# Configura la aplicación Flask y carga la configuración de la base de datos
app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123@localhost:5432/preguntas'
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la base de datos y las migraciones
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def menu(): 
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Recoger los datos del formulario
        nombre = request.form['username']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        rol = request.form['rol']
        password = request.form['password']

        # Verificar si el correo ya está registrado
        usuario_existente = Usuario.query.filter_by(correo=correo).first()
        if usuario_existente:
            flash("El correo ya está registrado. Por favor, usa otro correo.", "error")
            return redirect(url_for('registro'))

        # Generar el hash de la contraseña
        hashed_password = generate_password_hash(password)

        # Crear el usuario según el rol
        if rol == 'estudiante':
            nuevo_usuario = Estudiante(nombre=nombre, apellidos=apellidos, correo=correo, password=hashed_password)
        elif rol == 'profesor':
            nuevo_usuario = Profesor(nombre=nombre, apellidos=apellidos, correo=correo, password=hashed_password)
        else:
            flash("Rol no válido. Selecciona Estudiante o Profesor.", "error")
            return redirect(url_for('registro'))

        # Agregar el nuevo usuario a la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()

        flash("Registro exitoso. Ahora puedes iniciar sesión.", "success")
        return redirect(url_for('login_profesor' if rol == 'profesor' else 'login_estudiante'))

    # Mostrar el formulario de registro
    return render_template('registro.html')

@app.route('/login/profesor', methods=['GET', 'POST'])
def login_profesor():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']
        profesor = Profesor.query.filter_by(correo=correo).first()

        if profesor and check_password_hash(profesor.password, password):
            session['user_id'] = profesor.id
            session['user_type'] = 'profesor'
            flash('Inicio de sesión exitoso como profesor')
            return redirect(url_for('dashboard_profesor'))
        else:
            flash('Credenciales incorrectas para profesor')

    return render_template('profesores/login_profesor.html')

@app.route('/login/estudiante', methods=['GET', 'POST'])
def login_estudiante():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']
        estudiante = Estudiante.query.filter_by(correo=correo).first()

        if estudiante and check_password_hash(estudiante.password, password):
            session['user_id'] = estudiante.id
            session['user_type'] = 'estudiante'
            flash('Inicio de sesión exitoso como estudiante')
            return redirect(url_for('dashboard_estudiante'))
        else:
            flash('Credenciales incorrectas para estudiante')

    return render_template('estudiantes/login_estudiante.html')

@app.route('/dashboard_profesor')
def dashboard_profesor():
    if 'user_id' not in session or session.get('user_type') != 'profesor':
        flash('Debes iniciar sesión como profesor', 'danger')
        return redirect(url_for('login_profesor'))

    profesor_id = session['user_id']
    preguntas = Pregunta.query.filter_by(profesor_id=profesor_id).all()
    return render_template('profesores/dashboard_profesor.html', preguntas=preguntas)


@app.route('/dashboard_estudiante')
def dashboard_estudiante():
    return render_template('estudiantes/estudiante.html')

@app.route('/crear_preguntas', methods=['GET', 'POST'])
def preguntas():
    if 'user_id' not in session or session.get('user_type') != 'profesor':
        flash('Debes iniciar sesión como profesor para acceder a esta página.', 'danger')
        return redirect(url_for('login_profesor'))  # Redirige al login del profesor si no está logueado

    if request.method == 'POST':
        # Obtener los datos del formulario
        area = request.form['area']
        definicion = request.form['definicion']
        base_reactivo = request.form['base']
        respuesta1 = request.form['respuesta1']
        respuesta2 = request.form['respuesta2']
        respuesta3 = request.form['respuesta3']
        respuesta4 = request.form['respuesta4']
        tipoRespuesta = request.form['tipoRespuesta']
        argumentacion = request.form['argumentacion']

        # Obtener el id del profesor desde la sesión
        profesor_id = session['user_id']

        # Crear una nueva pregunta
        nueva_pregunta = Pregunta(
            area=area,
            definicion_operacional=definicion,
            base_reactivo=base_reactivo,  # Puedes asignar alguna de las respuestas aquí si es necesario
            opcion1=respuesta1,
            opcion2=respuesta2,
            opcion3=respuesta3,
            opcion4=respuesta4,
            tipo_respuesta=tipoRespuesta,
            argumentacion=argumentacion,
            profesor_id=profesor_id  # Asociamos la pregunta al profesor
        )

        # Guardar la pregunta en la base de datos
        db.session.add(nueva_pregunta)
        db.session.commit()

        flash('Pregunta creada exitosamente', 'success')
        return redirect(url_for('dashboard_profesor'))  # Redirigir al dashboard del profesor

    return render_template('profesores/preguntas.html')



if __name__ == '__main__':
    app.run(debug=True)
