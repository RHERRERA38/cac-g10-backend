from flask import Flask
from app.views import get_all_reservas
from app.database import init_app

#Iniciar la aplicacion con Flask
app = Flask(__name__)

init_app(app)

#Registrar rutas asociadas

app.route('/api/reservas', methods=['GET'])(get_all_reservas)


if __name__ == '__main__':
    app.run(debug=True)