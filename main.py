import sys
import pygame
from configuracoes import Configuracoes
from personagem import Personagem
from pontuacoes import Pontuacoes
from paredes import Paredes

def rodar_jogo():
    # Inicia o jogo
    pygame.init()
    configuracoes = Configuracoes()
    personagem = Personagem()
    pontuacoes = Pontuacoes()
    paredes = Paredes()


    janela = pygame.display.set_mode(
        (configuracoes.janela_largura, configuracoes.janela_altura))
    pygame.display.set_caption("Titulo")

    while True:
        # Laço principal do jogo

        
         
        janela.fill(configuracoes.cor_bg)

        pygame.draw.circle(janela, personagem.cor, personagem.dimensoes, personagem.raio)
        pygame.draw.rect(janela, pontuacoes.cor, pontuacoes.dimensoes)
        pygame.draw.line(janela, paredes.cor, paredes.xCoord, paredes.yCoord, paredes.largura)

        pygame.display.flip() # Atualiza a tela

rodar_jogo()