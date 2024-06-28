from flask import jsonify, request
from app.models import Reserva


#Se obtiene la lista de reservas
def get_all_reservas():
    reservas = Reserva.get_all()
    return jsonify([Reserva.serialize() for Reserva in reservas])


#Función para seleccionar una reserva
def get_reserva(Id_reserva):
    reserva = Reserva.get_by_id(Id_reserva)
    if reserva:
        return jsonify(reserva.serialize())
    else:
        return jsonify({'error': 'Reserva no encontrada'}), 404


#Función para crear reserva en base de datos
def create_reserva():
    data = request.json
    
    new_reserva = Reserva(None, data['nombre'], data['email'], data['nro_telefono'], data['cant_comensales'],
                          data['fecha'], data['hora'], data['local'], data['preferencias'], data['confirmacion'])
    new_reserva.save()
    response = {'message': 'Reserva creada con éxito'}
    return jsonify(response), 201

#Función para actualizar una reserva existente
def update_reserva(Id_reserva):
    if request.is_json:
        data = request.get_json()
        act_reserva = Reserva(Id_reserva, data['nombre'], data['email'], data['nro_telefono'], data['cant_comensales'],
                        data['fecha'], data['hora'], data['local'], data['preferencias'], data['confirmacion'])
        act_reserva.save()
        
        response = {'message': 'Reserva actualizada con éxito'}
        return jsonify(response), 200
    else:
        response = {'error': 'El contenido debe ser JSON'}
        return jsonify(response), 415
    

#Función para confirmar las reservas    
def confirm_reserva(Id_reserva):
    Reserva.confirm(Id_reserva)
    response = {'message': 'Reserva actualizada con éxito'}
    return jsonify(response), 200


#Función para eliminar una reserva
def delete_reserva(Id_reserva):
    reserva = Reserva.get_by_id(Id_reserva)
    if not reserva:
        return jsonify({'message': 'Reserva No encontrada'}), 404
    reserva.delete()
    response = {'message': 'Reserva eliminada con éxito'}
    return jsonify(response), 200