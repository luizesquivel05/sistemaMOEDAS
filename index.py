import random; import os; import time as tm
while True:
    print('''
        Olá, seja bem-vindo ao nosso sistemas de sorteio de moedas, aqui iremos sortear pela moeda.
        
        Sendo:
        
        0 - cara
        1 - coroa
        
        Use o programa com sabedoria!
    ''')
    print('Estamos realizando o sorteio! POR FAVOR AGUARDE... ')
    tm.sleep(10)
    moeda = list([0, 1])
    sorteio = random.choice(moeda)
    if sorteio == 0: resultado = "cara"
    else: resultado = "coroa"
    print(f'\n\nO resultado do sorteio foi -> {resultado}\n\n')
    if str(input('Deseja fazer outro sorteio? S para SIM e N para NÃo: ')) == "S":
        try: 
            os.system('cls')
        except:
            os.system('clear')
    else:
        break