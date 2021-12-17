class estacionamento:
    listaVagas = [[c for c in range(1, 21)], [c for c in range(21, 51)],
                  [c for c in range(51, 71)], [c for c in range(71, 81)]]
    listaMaxMinVagas = [[1, 20], [21, 50], [51, 71], [71, 80]]
    listaValores = [5, 15, 20, 50]


    def __str__(self):
        return f'Para motos estão disponiveis as vagas {self.listaVagas[0]} ' \
               f'\nPara carros estão disponiceis as vagas {self.listaVagas[1]} ' \
               f'\nPara veiculos de médio-grande porte estão disponiveis as vagas {self.listaVagas[2]} ' \
               f'\nPara veiculos de grande poste estão disponiveis as vagas {self.listaVagas[3]}'

    @staticmethod
    def EncontraGrupo(grupo: str, listaGrupos: list):
        for c in range(0, len(listaGrupos)):
            if grupo == listaGrupos[c]:
                return c

    def vagasSobrando(self, grupo):
        return len(self.listaVagas[grupo])-1

    def VerificaVaga(self, grupo):
        try:
            self.listaVagas[grupo][0]
        except:
            return False
        else:
            return self.listaVagas[grupo][0]

    def EntradaVeiculo(self, grupo):
        try:
            vaga = self.listaVagas[grupo][0]
            self.listaVagas[grupo].pop(0)
        except:
            return False
        else:
            return vaga

    def SaidaVeiculo(self, grupo, vaga):
        if vaga not in self.listaVagas[grupo] and self.listaMaxMinVagas[grupo][-1] >= vaga >= self.listaMaxMinVagas[grupo][0]:
            self.listaVagas[grupo].append(vaga)
            self.listaVagas[grupo].sort()
        else:
            return False

    def listaVagasOcupadas(self, grupo):
        lista = []
        for c in range(self.listaMaxMinVagas[grupo][0], self.listaMaxMinVagas[grupo][1]):
            if c not in self.listaVagas[grupo]:
                lista.append(c)
        return lista

    def valorPago(self, grupo):
        return self.listaValores[grupo]
