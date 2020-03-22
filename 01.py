import threading
from time import sleep

global bown
# funcao que espera 1 segundo

def wait():
    cont = 0
    global bown
    while True:
        bown = 0
        print(cont)
        cont += 1
        sleep(1)
        bown = 1
        # print(bown)


def LerVelocidade():
    global bown
    while True:
        if (bown == 1):
            print('Leitura da Velocidade')


# ----------------criando a thread
#adicionar mutex

t = threading.Thread(target=wait, name='Wait')
t1 = threading.Thread(target=LerVelocidade, name='Velocidade')
t.start()
t1.start()

print("vou adicionar só algumas coisinhas pra ver se vai commitar")

