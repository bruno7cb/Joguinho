import sys
import pygame

def verificar_Funcoes():
    for event in pygame.event.get():
    # Analisa as teclas e mouse
        if event.type == pygame.QUIT:
            sys.exit()