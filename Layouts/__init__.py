import PySimpleGUI as sg


def layoutCarregamento():
    return [[sg.T('Bem-Vindo\nAo\nSafety Car Place', font=('calibri', 40), justification='center',
                  size=(600, 3), pad=(16, 30))],
            [sg.T('Carregando', font=('calibri', 30), justification='center', size=(600, 1))],
            [sg.ProgressBar(100, orientation='h', size=(50, 40), key='-LOAD-')],
            [sg.T('0 %', font=('calibri', 30), justification='center', key='-CARREGA-', size=(600, 1))],
            [sg.B('Cancelar', font=('calibri', 25)),
             sg.B('Iniciar Programa', font=('calibri', 25), key='-CONFIRMA-', visible=False)]]


def layoutInicial():
    return [[sg.T('Opções', font=('calibri', 35), size=(1000, 1), justification='center', pad=(10, 30))],
            [sg.B('Entrada de veiculos', font=('calibri', 30), key='-ENTRADA-', border_width=2, pad=(20, 8))],
            [sg.B('Saida de veiculos', font=('calibri', 30), key='-SAIDA-', border_width=2, pad=(20, 8))],
            [sg.B('Registros', font=('calibri', 30), key='-ESTATISTICA-', border_width=2, pad=(20, 8))],
            [sg.B('Finalizar o dia', font=('calibri', 30), key='-FCAIXA-', border_width=2, pad=(20, 8))]]


def layoutEntrada(veiculos, pagamento):
    return [[sg.T('Entrada de Veiculos', font=('calibri', 30), size=(800, 1), justification='center')],
            [sg.T('Tipo de Veiculos', font=('calibri', 25))],
            [sg.Combo(values=veiculos, default_value='Moto', font=('calibri', 25), readonly=True, key='-VEICULO-')],
            [sg.T('Metodo de Pagamento', font=('calibri', 25), key='-PAGAMAENTO-')],
            [sg.Combo(values=pagamento, font=('calibri', 25), readonly=True, default_value='Dinheiro', key='-PAGAMENTO-')],
            [sg.B('Voltar', font=('calibri', 24), pad=(4, 10)), sg.B('Proximo', font=('calibri', 24), pad=(10, 10))]]


def layoutPagamento(vaga, valorApagar, vagasSobrando, vagasOcupadas, metodoPagamento):
    return [[sg.T('Pagamento', font=('calibri', 30), justification='center', size=(800, 1))],
            [sg.T(f'Vaga Resignada: {vaga}', font=('calibri', 25), pad=(30, 15)),
             sg.T(f'Valor a ser pago: {valorApagar} R$',
           font=('calibri', 25), pad=(50, 15))],
            [sg.T(f'Vagas Sobrando: {vagasSobrando}',
           font=('calibri', 25), pad=(30, 15)),
             sg.T(f'Vagas Ocupadas: {vagasOcupadas}',
           font=('calibri', 25), pad=(30, 2))],
            [sg.T(f'Metodo de Pagamento: {metodoPagamento}', font=('calibri', 25), pad=(30, 15))],
             [sg.B('Voltar', font=('calibri', 25), pad=(30, 10)),
             sg.B('Confirmar', font=('calibri', 25), pad=(30, 10))]]


def layoutSaida(tipos, vagas):
    return [[sg.T('Saida De Veiculos', font=('calibri', 30), size=(600, 1), justification='center')],
                       [sg.T('Tipo do Veiculo', font=('calibri', 25), pad=(20, 20)), sg.T('Vaga Deixada', font=('calibri', 25), pad=(120, 20))],
                       [sg.Combo(values=tipos, readonly=True, size=(15, 1),
                                 default_value='Leve', font=('calibri', 20), key='-GRUPO-', pad=(20, 0)),
                        sg.Combo(values=vagas, readonly=True, size=(15, 1),
                                 key='-OCUPADO-', font=('calibri', 20), pad=(102, 0))],
                       [sg.B('Voltar', font=('calibri', 23), pad=(20, 30), border_width=2), sg.B('Finalizar', font=('calibri', 23), pad=(20, 30), border_width=2)]]


def layoutRegistros(ano, meses, Pdias):
    return [[sg.T('Registros', font=('calibri', 30), size=(800, 1), justification='center')],
                             [sg.T('Selecione a data na qual deseja ver os registros', font=('calibri', 25))],
                             [sg.T('Ano: ', font=('calibri', 25), pad=(20, 10)),
                              sg.Combo(values=[x for x in range(ano, 2000, -1)],
                                       font=('calibri', 25), default_value=ano, readonly=True, key='-ANO-')],
                             [sg.T('Mês: ', font=('calibri', 25), pad=(20, 10)),
                              sg.Combo(values=meses, key='-MES-', default_value=meses[0], font=('calibri', 25), pad=(2, 0), readonly=True)],
                             [sg.T('Dia: ', font=('calibri', 25), pad=(20, 10)),
                              sg.Combo(values=Pdias[0], key='-DIA-', font=('calibri', 25), default_value=Pdias[0][0], pad=(15, 0), readonly=True)],
                             [sg.B('Voltar', font=('calibri', 20)), sg.B('Confirmar', font=('calibri', 20))]]


def layoutDados(diaEscolhido, mesEscolhido, anoEscolhido, dados):
    Titulo = [[sg.T(f'Dados Referentes a {diaEscolhido}/{mesEscolhido}/{anoEscolhido}', font=('calibri', 30))],
              [sg.T('Hora de Entrada - Classe do Veiculo  -  Vaga Ocupada  -  Valor Pago  -  Metodo de Pagamento',
                    font=('calibri', 20))]]

    listaDados = [[sg.Frame(layout=[[sg.T(f'- {dados[y][1]:>2}:{dados[y][0]:<6} - {dados[y][5]:<12} - {dados[y][6]:<8} - {dados[y][7]:<2}R$   - {dados[y][8]:^11}',
                                    font=('Courier', 20), background_color='white')]], title='') for x in range(1)] for y in range(0, len(dados))]

    frontDados = [[sg.Frame(layout=[[sg.Column(listaDados, vertical_scroll_only=True, scrollable=True, size=(990, 300))]], title='')]]

    botoes = [[sg.B('Voltar', font=('calibri', 25))]]

    return Titulo + frontDados + botoes