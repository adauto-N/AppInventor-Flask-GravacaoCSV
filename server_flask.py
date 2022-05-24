from flask import Flask
from arduino import Arduino
from arduino_DAO import ArduinoDAO

app = Flask(__name__)


@app.route('/arduino/<temperatura>/<presenca>/<luminosidade>')
def getArduino(temperatura, presenca, luminosidade):
    a1 = Arduino()  # Criação do objeto arduino

    a1.temperatura = temperatura
    a1.presenca = presenca
    a1.luminosidade = luminosidade

    dao = ArduinoDAO()
    dao.create(a1)

    output = "Temperatura: " + str(a1.temperatura) + ", " + "Presença: " + str(a1.presenca) + ", " + "Luminosidade: " + str(a1.luminosidade)
    return output


app.run(port=8000, host='0.0.0.0')
