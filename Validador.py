def main_screen(): # Interface Gráfica e a leitura dos valores e eventos.
    from PySimpleGUI import PySimpleGUI as ms
    ms.theme('Reddit')
    layout = [
        [ms.Text('CPF:', size=(5, 0)), ms.Input(key='cpf', size=(50, 10))],
        [ms.Button('Validar')]
    ]
    UI = ms.Window('Validador de CPFs', size=(350, 100), layout=layout)
    while True:
        event, values = UI.read()
        if event == ms.WIN_CLOSED:
            break
        while True:
            if event == 'Validar' and verify_cpf(values['cpf']) == False:
                ms.popup('CPF INVÁLIDO!')
                UI.find_element(key='cpf').update('')
            elif event == 'Validar' and verify_cpf(values['cpf']) == True:
                ms.popup('CPF VÁLIDO!')
            break



def verify_cpf(n=''): # Função de validação do CPF
    n = n.replace('.', '')
    n = n.replace('-', '')
    if len(n) > 11 or len(n) < 11 or n == '':
        return False
    else:
        cpfDig = []
        cpfTest = []
        try:
            for a in n:
                a = int(a)
                cpfDig.append(a)
                cpfTest.append(a)
        except:
            return False
        # Calculando 1º Digito
        acumulador = 0
        dv1 = 0
        for n, i in enumerate(cpfTest):
            m = (n + 1) * i
            acumulador += m
            if n == 8:
                break
        dv1 = acumulador % 11
        if dv1 == 10:
            dv1 = 0
        cpfTest.pop(9)
        cpfTest.insert(9, dv1)
        # Caluculando 2º Digito
        acumulador2 = 0
        dv2 = 0
        for n, i in enumerate(cpfTest):
            m = n * i
            acumulador2 += m
            if n == 9:
                break
        dv2 = acumulador2 % 11
        if dv2 == 10:
            dv2 = 0
        cpfTest.pop(10)
        cpfTest.insert(10, dv2)
        if cpfTest == cpfDig:
            return True
        else:
            return False


main_screen()