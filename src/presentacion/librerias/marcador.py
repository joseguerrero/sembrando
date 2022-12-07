#!/usr/bin/env python

import pygame


class marcador(pygame.sprite.Sprite):
    """
    Esta clase define marcadores para la actividad 1.
    """

    def __init__(self, rect, id):
        """
        Método inicializador de la clase.

        @param rect: Rectángulo que define la posición, alto y ancho de un marcador.
        @type rect: pygame.Rect
        @param id: Identificador del marcador.
        @type id: str
        """
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(rect)
        self.id = id
