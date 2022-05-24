class Arduino():

    def __init__(self):
        self._temperatura = 0.0  # atributos privados
        self._presenca = 0
        self._luminosidade = 0.0

    @property  # proppertys e setters de cada atributo, chamam-se anotation.
    def temperatura(self):  # acessa propriedade protegida (privada) e retorna o valor atual dela
        return self._temperatura

    @temperatura.setter
    def temperatura(self, value):  # esta função altera o valor de temperatura mesmo ela sendo privada
        value = float(value)
        if -100.00 <= value <= 100.00:  # limite: -100 a 100 graus celsius
            self._temperatura = value

    @property
    def presenca(self):
        return self._presenca

    @presenca.setter
    def presenca(self, value):
        value = int(value)
        if value >= 0:   # não tem presença negativa
            self._presenca = value

    @property
    def luminosidade(self):
        return self._luminosidade

    @luminosidade.setter
    def luminosidade(self, value):
        value = float(value)
        if value >= 0:   # 0 é escuridão total
            self._luminosidade = value
