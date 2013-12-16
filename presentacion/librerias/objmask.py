#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

class object_mask(pygame.sprite.Sprite):
    """
    Esta clase define objetos sensibles a colisiones por pixel.
    """
    def __init__(self, id, x, y, img1, img2 = ""):
        """
        Método inicializador de la clase.
        
        @param id: Identificador único para cada instancia de esta clase.
        @type id: str
        @param x: Coordenada X donde se desea dibujar el objeto.
        @type x: int
        @param y: Coordenada Y donde se desea dibujar el objeto.
        @type y: int
        @param img1: Ruta de la imagen activa que se desea cargar.
        @type img1: str
        @param img2: Ruta de la imagen desactivada que se desea cargar.
        @type img2: str
        """ 
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.tipo_objeto = "mapa"
        self.image = pygame.image.load(img1)
        if not img2 == "":
            self.image_act =pygame.image.load(img2)            
        else:   
            self.image_act = self.image 
        self.image_des = self.image
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.hitmask = pygame.surfarray.array_alpha(self.image)

    def iluminar(self):
        """
        Cambia la imagen del objeto por la imagen activa.
        """
        self.image = self.image_act
    
    def apagar(self):
        """
        Cambia la imagen del objeto por la imagen desactivada.
        """
        self.image = self.image_des