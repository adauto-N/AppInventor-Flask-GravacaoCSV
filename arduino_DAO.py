import pandas as pd


# Métodos comuns em arquivos de manipular csv:
# C - Create
# R - Read/read_all
# U - Update
# D - Delete

class ArduinoDAO():

    def open(self):
        df = pd.read_csv('arduino.csv')
        return df

    def save(self,df):
        df.to_csv('arduino.csv', index = False)

    def create(self, arduino):
        df = self.open()

        # criação de uma nova linha que será adicionada ao dataframe original
        new_row = pd.DataFrame(data=[[
                                    arduino.temperatura, arduino.presenca, arduino.luminosidade
                                    ]],
                                    columns= df.columns)    # pega as colunas do dataframe e coloca nesse "novo"

        df = df.append(new_row)  # adiciona esta linha criada no df original
        self.save(df)

