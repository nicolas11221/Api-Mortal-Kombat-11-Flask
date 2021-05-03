
# Importar Flask
# jsonify: Nos permite convertir un objeto a un json tipico de navegador
from flask import Flask, jsonify

# Iniciar Flask
app = Flask(__name__)

# Get: Obtener Datos 
# Post: Guardar Datos
# Delete: Eliminar Datos

# Importar Personajes
from personajes import characters

# Ruta De Prueba (Testeo)
@app.route('/ping')
# Cuando alguien entre a ping, se ejecutara lo siguiente
def ping():
    return jsonify({"message": "Pong!!"})

# De mi lista de productos, traeme el producto con el nombre especificado
@app.route('/personajes/<string:personaje_name>')
def getPersonaje(personaje_name):
    # Este For Recorre todos los personajes 1 a 1
    # El if dice, si el nombre del que recibo coincide con el del personaje, traelo y guardalo en la variable personajesFound
    personajesFound = [
        character for character in characters if character['name'] == personaje_name]
    return jsonify({'Personaje': personajesFound[0]})


# Get, Obtener Datos
@app.route('/personajes', methods=['GET'])
def getPersonajes():
    return jsonify({"caracteres": characters})


if __name__ == '__main__':
    app.run(debug=True, port=4000)