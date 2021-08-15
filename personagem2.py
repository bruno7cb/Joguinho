import pygame

class Personagem2():
    
    def __init__(self, janela):
        """ Inicializa o personagem e define sua localização """
        self.janela = janela

        # Carrega a imagem como um retangulo
        self.imagem = pygame.image.load('imagens/personagem.bmp')
        self.retangulo = self.imagem.get_rect()
        self.janela_retangular = janela.get_rect()

        self.retangulo.centerx = self.janela_retangular.centerx
        self.retangulo.bottom = self.janela_retangular.bottom
    
    def blitme(self):
        """ Desenha o personagem """
        self.janela.blit(self.imagem, self.retangulo)