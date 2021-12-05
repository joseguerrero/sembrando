#!/usr/bin/env python

import pygame

class cursor(pygame.sprite.Sprite):
    """
    Esta clase define una sencilla interfaz para interactuar con el cursor.
    """
    def __init__(self):
        """
        Método inicializador de la clase.
        """
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, 1, 1)
    
    def update(self):
        """
        Actualiza la posición del cursor en la pantalla.
        """
        self.rect.left, self.rect.top = pygame.mouse.get_pos()
