import pygame,sys
from pygame.math import Vector2

class Configuracoes:
    largura = 1280
    altura = 720


class Level:
    def __init__(self):
        
        # Recebe o tamanho da tela
        self.display_surface = pygame.display.get_surface()

        # Grupos de Sprites
        self.all_sprites = pygame.sprite.Group()

    def run(self):
        self.display_surface.fill('white')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((Configuracoes.largura,
                                             Configuracoes.altura))
        pygame.display.set_caption("Frenesi Fantasy")
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.level.run()
            pygame.display.update()

if __name__ == '__main__':
    jogo = Jogo()
    jogo.run()