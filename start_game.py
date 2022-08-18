import pygame
from pygame.locals import *
from sys import exit  # função para fechar janela

from snaker_game import snaker_game
from car_racing import loop_game



pygame.init()  # Iniciando o pygame

largura = 640
altura = 480

fonte = pygame.font.SysFont('arial', 18, True, False)

# Defenindo largura e altura da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')  # Definindo nome do jogo

relogio = pygame.time.Clock()  # Frame

img_fundo = pygame.image.load('./imgs/bg.jpg').convert()

# loop do jogo
while True:
    relogio.tick(10)  # Frame
    tela.fill((255, 255, 255))  # tela preta

    font_2 = pygame.font.SysFont("arial", 20, True, False)

    tela.blit(img_fundo, (0, 0))

    messagem_3 = "A -  Snaker Game"
    messagem_2 = "B -  Car Racing"

    text_formatado_03 = font_2.render(messagem_3, True, (0, 139, 139))
    ret_texto_3 = text_formatado_03.get_rect()
    ret_texto_3.center = (largura // 2, altura // 2 - 15)
    
    text_formatado_02 = font_2.render(messagem_2, True, (0, 139, 139))
    ret_texto_2 = text_formatado_02.get_rect()
    ret_texto_2.center = (largura // 2, altura // 2 - -10)

    tela.blit(text_formatado_03, ret_texto_3)
    tela.blit(text_formatado_02, ret_texto_2)

    controle_jogo = 0

    for event in pygame.event.get():  # Detectando se algum evento ocorreu

        # Evento de fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:

            if event.key == K_a:
                controle_jogo = 1
                if controle_jogo == 1:
                    snaker_game(controle_jogo)
            if event.key == K_b:
                controle_jogo = 2
                if controle_jogo == 2:
                    loop_game(controle_jogo)
           

    pygame.display.update()
