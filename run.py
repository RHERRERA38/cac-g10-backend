from flask import Flask
from app.views import get_all_reservas, create_reserva, get_reserva, update_reserva, confirm_reserva, delete_reserva
from app.database import init_app

#Iniciar la aplicacion con Flask
app = Flask(__name__)

init_app(app)

#Registrar rutas asociadas

app.route('/api/reservas', methods=['GET'])(get_all_reservas) #Obtiene la lista de reservas
app.route('/api/reservas', methods=['POST'])(create_reserva) #crea una reserva
app.route('/api/reservas/<int:Id_reserva>', methods=['GET'])(get_reserva) #selecciona los datos de una reserva
app.route('/api/reservas/<int:Id_reserva>', methods=['PUT'])(update_reserva) #actualiza los datos de una reserva
app.route('/api/reservas/<int:Id_reserva>', methods=['DELETE'])(delete_reserva) #Elimina la reserva
app.route('/api/reservas/confirm/<int:Id_reserva>', methods=['PUT'])(confirm_reserva) #confirma la reserva


if __name__ == '__main__':
    app.run(debug=True)