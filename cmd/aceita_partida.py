#Importar módulos

#1° Módulo - pyautogui
#Módulo para Automação de GUI (Graphical User Interface / Interface gráfica do usuário)

#Função que retorna coordenadas(x,y) na tela, referênte ao centro imagem passada como parâmetro.
from pyautogui import locateCenterOnScreen

#Função que movimenta o mouse até uma coordenada(x,y) expecífica
from pyautogui import moveTo

#Função que realiza o click do mouse
from pyautogui import click

#Função que retorna a posição do mouse
from pyautogui import position

#2° Módulo - Pillow/PIL (Python Imaging Library / Módulo de imagens para Python)
#Módulo de processamento de imagem.

#Funções referênte a contrução, modificação e carregamento de imagens.
from PIL import Image

#3° Módulo - Time
#Módulo relacionado ao tempo.

#Função que suspende a execução do por um determinado tempo(n segundos).
from time import sleep

#4° Módulo - OS
#Módulo relacionado ao SO.

#Função que lista os arquivos em um diretório
from os import listdir

#Lista com caminho dos arquivos dentro da pasta 'imgs'
caminho_imgs = list()
for file in listdir("imgs"):
    if file.endswith(".png"):
        caminho_imgs.append('imgs/{}'.format(file))

#Carregar imagens da pasta para mémoria.
imgs = list()
for img in caminho_imgs:
    imgs.append(Image.open(img))

#Criar condição de loop para poder verificar a tela constantemente
#Enquanto o programa estiver aberto, sempre irá verificar
while True:

    #Para cada imagem, verifica e clica
    for img in imgs:
        local_da_img = locateCenterOnScreen(img, grayscale=True)

        #Caso tenho encontrado o botão na tela, executar as seguintes instruções
        if local_da_img != None:

            #Definir coordenadas x e y, é onde o botão se encontra na tela
            x, y = local_da_img

            #Armazenar as coordenadas de x e y do mouse
            mx, my = position()

            #Mover mouse até as coordenadas x e y na tela
            moveTo(x, y)

            #Realizar o click do mouse
            click()

            #Movimento o mouse para coordenada anterior
            moveTo(mx, my)

            #Informa no terminal que partida foi aceita
            print("Partida Aceita!")

        #Caso não tenha encontrado o botão na tela, informar que ainda esta procurando partida
        else:
            print("\rProcurando partida...")
    print("============================")
    #Suspender a execução do programa durante 1 segundo
    sleep(1)
