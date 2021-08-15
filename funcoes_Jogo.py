import sys
import pygame
from personagem2 import Personagem2

def verificar_Funcoes():
    for event in pygame.event.get():
    # Analisa as teclas e mouse
        if event.type == pygame.QUIT:
            sys.exit()

def atualizacao_Tela(configuracoes, janela, personagem):
    janela.fill(configuracoes.cor_bg) #  cor de fundo
    personagem2 = Personagem2(janela)
    personagem2.blitme()
    pygame.display.flip() # Atualiza a tela