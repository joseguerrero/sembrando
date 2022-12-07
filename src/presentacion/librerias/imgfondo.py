#!/usr/bin/env python

import pygame


class fondo:
    def __init__(self, largo, ancho, borde=3):
        """
        Método inicializador de la clase.

        @param largo: Largo del rectángulo.
        @type largo: int
        @param ancho: Ancho del rectángulo.
        @type ancho: int
        @param borde: Grosor del borde, valor por defecto = 3.
        @type borde: int
        """
        x = 0
        y = 0
        grosor = 20
        color = (136, 196, 52)
        color2 = (233, 238, 203)
        self.img = pygame.Surface((largo, ancho))
        self.img.fill((255, 255, 0))
        self.img.set_colorkey((255, 255, 0))
        pygame.draw.rect(self.img, color, (x + grosor, y, largo - grosor * 2, ancho))
        pygame.draw.rect(self.img, color, (x, y + grosor, largo, ancho - grosor * 2))
        pygame.draw.circle(self.img, color, (x + grosor, y + grosor), grosor)
        pygame.draw.circle(self.img, color, (x + largo - grosor, y + grosor), grosor)
        pygame.draw.circle(self.img, color, (x + grosor, y + ancho - grosor), grosor)
        pygame.draw.circle(
            self.img, color, (x + largo - grosor, y + ancho - grosor), grosor
        )

        if borde > 0:
            largo -= borde * 2
            ancho -= borde * 2
            img2 = pygame.Surface((largo, ancho))
            img2.fill((255, 255, 0))
            img2.set_colorkey((255, 255, 0))
            pygame.draw.rect(img2, color2, (x + grosor, y, largo - grosor * 2, ancho))
            pygame.draw.rect(img2, color2, (x, y + grosor, largo, ancho - grosor * 2))
            pygame.draw.circle(img2, color2, (x + grosor, y + grosor), grosor)
            pygame.draw.circle(img2, color2, (x + largo - grosor, y + grosor), grosor)
            pygame.draw.circle(img2, color2, (x + grosor, y + ancho - grosor), grosor)
            pygame.draw.circle(
                img2, color2, (x + largo - grosor, y + ancho - grosor), grosor
            )
            self.img.blit(img2, (borde, borde))

    def return_imagen(self):
        """
        Retorna la imagen del rectángulo.

        @return: Superficie con la imagen del rectángulo.
        @rtype: pygame.Surface
        """
        return self.img
