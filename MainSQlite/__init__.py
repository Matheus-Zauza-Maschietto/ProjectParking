import sqlite3 as sql
import datetime


class Banco_de_Dados:
    datas = [datetime.datetime.today().minute, datetime.datetime.today().hour, datetime.datetime.today().day,
             datetime.datetime.today().month, datetime.datetime.today().year]

    def __init__(self):
        self.BDD = sql.connect('BDD.db')
        self.mouse = self.BDD.cursor()
        self.mouse.execute('CREATE TABLE IF NOT EXISTS estacionamentoDados(mim TIMESTAMP, hora TIMESTAMP, dia TIMESTAMP, mes TIMESTAMP, ano TIMESTAMP, grupo TEXT, vagaOcupada INTEGER, valorPago INTEGER, metodoPagamento TEXT)')

    def Adicionar(self, grupo: str, vagaOcupada: int, valorPago: int, metodoPagamento: str):
        self.mouse.execute('INSERT INTO estacionamentoDados VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', (self.datas[0], self.datas[1], self.datas[2], self.datas[3], self.datas[4], grupo, vagaOcupada, valorPago, metodoPagamento))
        self.BDD.commit()

    def VerDados(self):
        self.mouse.execute('SELECT * FROM estacionamentoDados')
        print(self.mouse.fetchall())

    def DeletarDados(self):
        self.mouse.execute('DELETE FROM estacionamentoDados')

    def SelecionaDados(self, dia, mes, ano):
        self.mouse.execute('SELECT * FROM estacionamentoDados WHERE ano = ? AND mes = ? AND dia = ?', (ano, mes, dia))
        return self.mouse.fetchall()




