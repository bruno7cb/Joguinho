import pygame
import funcoes_Jogo as fc
from configuracoes import Configuracoes
from personagem import Personagem
from pontuacoes import Pontuacoes
from paredes import Paredes
from personagem2 import Personagem2


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

    personagem2 = Personagem2(janela)

    while True:
        fc.verificar_Funcoes()
        fc.atualizacao_Tela(configuracoes, janela, personagem2)
        #pygame.draw.circle(janela, personagem.cor, personagem.dimensoes, personagem.raio)
        #pygame.draw.rect(janela, pontuacoes.cor, pontuacoes.dimensoes)
        #pygame.draw.line(janela, paredes.cor, paredes.xCoord, paredes.yCoord, paredes.largura)
        
rodar_jogo()