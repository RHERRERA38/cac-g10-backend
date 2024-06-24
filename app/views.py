from flask import jsonify
from app.models import Reserva

def get_all_reservas():
    reservas = Reserva.get_all()
    return jsonify([Reserva.serialize() for Reserva in reservas])

