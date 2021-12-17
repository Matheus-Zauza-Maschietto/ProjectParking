from MainBackEnd import estacionamento
import Layouts
import PySimpleGUI as sg
import MainSQlite as bdd


sg.theme('Material1')

loadAtual = 0
iniciaPrograma = False
estacionamento = estacionamento()
BancoDeDados = bdd.Banco_de_Dados()

veiculos = ['Moto', 'Carro', 'Camionete, Van, Microônibus ou Caminhão de Pequeno Porte',
            'Ônibus ou Caminhão de grande porte']
tipos = ['Leve', 'Médio', 'Pesado', 'Muito Pesado']
pagamento = ['Dinheiro', 'Cartão', 'Pix']

window = sg.Window('Carregando', Layouts.layoutCarregamento(), size=(600, 500))
while True:
    key, value = window.read(timeout=10)
    if key == sg.WIN_CLOSED or key == 'Cancelar':
        break

    if loadAtual < 100:
        loadAtual += 1
        window['-LOAD-'].update(loadAtual)
        window['-CARREGA-'].update(f'{loadAtual} %')

    if loadAtual == 100:
        window['-CONFIRMA-'].update(visible=True)

    if key == '-CONFIRMA-':
        iniciaPrograma = True
        window.close()
        break

# Tela de opções para os carros que se aproximam
windowInicial = sg.Window('Tela de opções', Layouts.layoutInicial(), size=(800, 570))
while iniciaPrograma:
    key, value = windowInicial.read()

    if key == sg.WIN_CLOSED:
        windowInicial.close()
        iniciaPrograma = False

    elif key == '-ENTRADA-':
        # Janela de escolha do tipo de veiculo e de pagamento
        windowInicial.hide()
        windowEntrada = sg.Window('Entrada de Veiculos', Layouts.layoutEntrada(veiculos, pagamento), size=(800, 350))
        while True:
            key, value = windowEntrada.read()

            if key == 'Voltar' or key == sg.WIN_CLOSED:
                windowEntrada.close()
                windowInicial.un_hide()
                break

            elif key == 'Proximo':
                metodoPagamento = value['-PAGAMENTO-']
                grupo = estacionamento.EncontraGrupo(value['-VEICULO-'], veiculos)
                vaga = estacionamento.VerificaVaga(grupo)
                if not vaga:
                    sg.popup_ok('Não será possivel o uso de nossos serviços, nossas vagas para seu grupo de veiculos '
                                'estão '
                                'todas em uso. Volte novamente mais tarde',
                                font=('calibri', 20), keep_on_top=True)
                    windowEntrada.close()
                    windowInicial.un_hide()
                    break
                else:
                    # Janela Pagamento
                    windowEntrada.hide()
                    layoutPagamento = Layouts.layoutPagamento(vaga, estacionamento.listaValores[grupo],
                                                              estacionamento.vagasSobrando(grupo),
                                                              len(estacionamento.listaVagasOcupadas(grupo)), metodoPagamento)
                    windowPagamento = sg.Window('Pagamento', layoutPagamento, size=(800, 350))
                    while True:
                        key, value = windowPagamento.read()

                        if key == 'Voltar' or key == sg.WIN_CLOSED:
                            windowPagamento.close()
                            windowEntrada.un_hide()
                            break

                        elif key == 'Confirmar':
                            if sg.popup_yes_no('Tem certeza que deseja finalizar o pagamento ?', font=('calibri', 25)) == 'Yes':
                                estacionamento.EntradaVeiculo(grupo)
                                BancoDeDados.Adicionar(tipos[grupo], vaga, estacionamento.valorPago(grupo), metodoPagamento)
                                windowEntrada.close()
                                windowPagamento.close()
                                windowInicial.un_hide()
                                break

    elif key == '-SAIDA-':
        windowInicial.hide()
        grupo = 0  # Nivel do Grupo do veiculo
        vagas = estacionamento.listaVagas[grupo]
        variavelAntiga = tipos[0]
        layoutSaida = Layouts.layoutSaida(tipos, estacionamento.listaVagasOcupadas(grupo))

        windowSaida = sg.Window('Saida do Estacionamento', layoutSaida, size=(700, 300))
        while True:
            key, value = windowSaida.read(timeout=300)

            if key == 'Voltar' or key == sg.WINDOW_CLOSED:
                windowInicial.un_hide()
                windowSaida.close()
                break

            elif key == 'Finalizar':
                if value['-OCUPADO-'] != '':
                    if sg.popup_yes_no('Tem certeza que deseja realizar o fim da operação ?', font=('calibri', 20)) == 'Yes':
                        estacionamento.SaidaVeiculo(grupo, value['-OCUPADO-'])
                        windowInicial.un_hide()
                        windowSaida.close()
                        break
                else:
                    sg.PopupOK('Nenhuma vaga ocupada foi selecionada', font=('calibri', 20))

            for c in range(len(tipos)):  # transforma o tipo de veiculo de str em int
                if tipos[c] == value['-GRUPO-']:
                    grupo = c

            if value['-GRUPO-'] != variavelAntiga:  # Faz com que as vagas ocupadas sejam atualizadas apenas quando o campo de tipos mudar
                windowSaida['-OCUPADO-'].update(values=estacionamento.listaVagasOcupadas(grupo))
                variavelAntiga = value['-GRUPO-']

    elif key == '-ESTATISTICA-':
        windowInicial.hide()
        ano = int(BancoDeDados.datas[4])
        Pdias = [[x for x in range(1, 32)], [x for x in range(1, 31)], [x for x in range(1, 29)]]
        meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        variavelAntiga = meses[0]
        layoutEstatistica = Layouts.layoutRegistros(ano, meses, Pdias)

        windowRegistro = sg.Window('Janela de Registros', layoutEstatistica, size=(800, 350))
        while True:
            key, value = windowRegistro.read(timeout=300)

            if key == sg.WIN_CLOSED or key == 'Voltar':
                windowRegistro.close()
                windowInicial.un_hide()
                break

            elif key == 'Confirmar':
                windowRegistro.hide()

                diaEscolhido = value['-DIA-']
                mesEscolhido = value['-MES-']
                anoEscolhido = value['-ANO-']
                for c in range(0, len(meses)):
                    if mesEscolhido == meses[c]:
                        mesEscolhidoNumeral = c + 1
                        dados = BancoDeDados.SelecionaDados(diaEscolhido, mesEscolhidoNumeral, anoEscolhido)



                Titulo = [[sg.T(f'Dados Referentes a {diaEscolhido}/{mesEscolhido}/{anoEscolhido}',
                                font=('calibri', 30))],
                          [sg.T('Hora de Entrada - Classe do Veiculo  -  Vaga Ocupada  -  Valor Pago  -  Metodo de Pagamento', font=('calibri', 20))]]
                listaDados = [[sg.Frame(layout=[[sg.T(
                                        f'- {dados[y][1]:>2}:{dados[y][0]:<6} - {dados[y][5]:<12} - {dados[y][6]:<8} - {dados[y][7]:<2}R$ - {dados[y][8]:^10}',
                                        font=('Courier', 20), background_color='white')]], title='') for x in range(1)] for y in range(0, len(dados))]
                frontDados = [[sg.Column(listaDados, vertical_scroll_only=True, scrollable=True ,size=(990, 300))]]
                botoes = [[sg.B('Voltar', font=('calibri', 25))]]
                layout = Layouts.layoutDados(diaEscolhido, mesEscolhido, anoEscolhido, dados)
                windowDados = sg.Window('Dados', layout)
                while True:
                    key, value = windowDados.read()
                    if key == sg.WIN_CLOSED or key == 'Voltar':
                        windowDados.close()
                        windowRegistro.un_hide()
                        break

            # Gambiarra para parar de sar erro quando volta da tela de dados
            try:
                if value['-MES-'] != variavelAntiga:
                    variavelAntiga = value['-MES-']
                    if value['-MES-'] in ['janeiro', 'março', 'maio', 'julho', 'agosto', 'outubro', 'dezembro']:
                        windowRegistro['-DIA-'].update(values=[x for x in range(1, 32)])
                    elif value['-MES-'] in ['abril', 'junho', 'setembro', 'novembro']:
                        windowRegistro['-DIA-'].update(values=[x for x in range(1, 31)])
                    elif value['-MES-'] == 'fevereiro':
                        windowRegistro['-DIA-'].update(values=[x for x in range(1, 29)])
            except:
                pass


    elif key == '-FCAIXA-':
        if sg.popup_yes_no('Tem certeza que deseja finalizar o dia ?', font=('calibri', 20)) == 'Yes':
            window.close()
            break
