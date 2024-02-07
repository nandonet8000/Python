import time
from datetime import datetime, timedelta
def test_automatizado(): # ENTENDENDO COMO FUNCIONA
    now = datetime.now()
    prazo = now + timedelta(days=30)

    tempo = datetime(2021,10,20,10,40,11)


    resultado = now - tempo

    tempoano = resultado.days / 365
    tempomes = resultado.days / 30

    anos = int(tempoano)
    mes = int((tempomes) * 4.5)
    return mes *3

