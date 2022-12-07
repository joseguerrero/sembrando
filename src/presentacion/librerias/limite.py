#!/usr/bin/env python

import pygame


class limite(pygame.sprite.Sprite):
    """
    Esta clase define objetos colisionables para la actividad 1.
    """

    def __init__(self, rect, id):
        """
        Método inicializador de la clase.

        @param rect: Rectángulo que define la posición, alto y ancho de un limite.
        @type rect: pygame.Rect
        @param id: Identificador del limite.
        @type id: str
        """
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(rect)
        self.id = id
