from flask_app import app

from flask import render_template, redirect, flash, session, request
from flask_app.models.usuario import Usuario
from flask_app.models.viaje import Viaje

@app.route('/dashboard')
def dashboard():
    if 'usuario_id'not in session:
        return redirect('/')
    return redirect('/viajes')

@app.route('/viajes')
def viajes():
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "error")
        return redirect('/')
    
    usuario = Usuario.get_by_id({'id': session['usuario_id']})
    viajes = Viaje.get_all()
    return render_template('dashboard.html', usuario=usuario, viajes=viajes)

@app.route('/viajes/<int:id>/ver')
def ver_viaje(id):
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "error")
        return redirect('/')
    
    viaje = Viaje.get_by_id({'id': id})
    if not viaje:
        flash("Viaje no encontrado", "error")
        return redirect('/viajes')
    
    usuario = Usuario.get_by_id({'id': session['usuario_id']})
    return render_template('ver_viaje.html', usuario=usuario, viaje=viaje)

@app.route('/viajes/nuevo')
def nuevo_viaje():
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "error")
        return redirect('/')
    
    usuario = Usuario.get_by_id({'id': session['usuario_id']})
    return render_template('nuevo_viaje.html', usuario=usuario)

@app.route('/viajes/crear', methods=['POST'])
def crear_viaje():
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "error")
        return redirect('/')
    
    if not Viaje.validar_viaje(request.form):
        return redirect('/viajes/nuevo')
    
    datos_viaje = {
        'destino': request.form['destino'],
        'fecha_inicio': request.form['fecha_inicio'],
        'fecha_fin': request.form['fecha_fin'],
        'itinerario': request.form['itinerario']
    }
    Viaje.save(datos_viaje)
    return redirect('/viajes')

@app.route('/viajes/<int:id>/editar')
def editar_viaje(id):
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "error")
        return redirect('/')
    
    viaje = Viaje.get_by_id({'id': id})
    if not viaje:
        flash("Viaje no encontrado", "error")
        return redirect('/viajes')
    
    usuario = Usuario.get_by_id({'id': session['usuario_id']})
    return render_template('editar_viaje.html', usuario=usuario, viaje=viaje)

@app.route('/viajes/<int:id>/actualizar', methods=['POST'])
def actualizar_viaje(id):
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "error")
        return redirect('/')
    
    if not Viaje.validar_viaje(request.form):
        return redirect(f'/viajes/{id}/editar')
    
    datos_viaje = {
        'id': id,
        'destino': request.form['destino'],
        'fecha_inicio': request.form['fecha_inicio'],
        'fecha_fin': request.form['fecha_fin'],
        'itinerario': request.form['itinerario']
    }
    Viaje.update(datos_viaje)
    return redirect('/viajes')

@app.route('/viajes/<int:id>/eliminar', methods=['POST'])
def eliminar_viaje(id):
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "error")
        return redirect('/')

    Viaje.eliminar({'id': id})

    return redirect('/viajes')