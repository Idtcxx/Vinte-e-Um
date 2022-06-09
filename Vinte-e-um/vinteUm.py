from random import randint
from time import sleep

def vinteUm():
    print('\n\t\t\t\t\tCARTAS - VINTE E UM\n')
    ponto = 0
    print('Para pegar uma carta digite [1] ou [0] para encerrar')
    print('Será sorteado um número aleatório entre [1] e [13]')
    print('Ao encerrar o computador irá sortear um número aleatório que será somado ao seu jogo')
    sot = int(input('\n   ---'))

    while sot == 1 :
        n = randint(1, 13)
        ponto += n
        print(f'Número sorteado: {n}')
        print(f'TOTAL:{ponto}\n')
        if ponto > 21:
            print('Você Perdeu!')
            break
        print('Para continuar digite [1], ou [0] para encerrar.')
        sot = int(input('   ---'))
        if sot == 0:
            x = randint(1, 13)
            print(f'\nNúmero total {ponto}')
            print('O número sorteado foi...')
            sleep(3)
            print(x)
            print(f'Total: {ponto} + {x} : {x + ponto}\n\n')
            if ponto + x <= 21:
                if ponto + x == 21:
                    print('VITÓRIA PERFEITA!!!! PARABÉNS!!!!')
                    break
                print('Parabéns você ganhou!!!')
            else:
                print('Você Perdeu. Infelizmente você excedeu 21 pontos.')

    print('Deseja continuar?  [1]sim   [0]não')
    cont = input('   ---')
    if cont == '1':
        vinteUm()

    print('Adeus!!!!')


vinteUm()