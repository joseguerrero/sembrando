#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

class imagen(pygame.sprite.Sprite):
    """
    Esta clase permite cargar una imagen y realizar ciertas operaciones básicas.
    
    @todo: Crear una superclase 'objeto' que defina los métodos usados por las clases: imagen, objeto, entre otras.
    """
    img_aux = pygame.Surface((0, 0))
    """Superficie que guarda la imagen original como respaldo."""
    def __init__(self, imagen, x, y):
        """
        Método inicializador de la clase.
        
        @param imagen: Ruta de la imagen que se desea cargar.
        @type imagen: str
        @param x: Coordenada X donde se desea dibujar la imagen.
        @type x: int
        @param y: Coordenada Y donde se desea dibujar la imagen.
        @type y: int
        """
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagen).convert_alpha()
        self.img_aux = self.image
        (_,_,w,h) = self.image.get_rect()
        self.rect = pygame.Rect(x, y, w, h)
    
    def get_centro(self):
        """
        Obtiene el punto medio de una imagen previamente cargada, relativo al ancho de la pantalla.
        
        @return: Valor del punto medio de la imagen.
        @rtype: bool
        """
        (_,_,w,_) = self.image.get_rect()
        return int(self.x + (w/2.0))
    
    def ajustar_alto(self, alto):
        """
        Redimensiona el alto de una imagen previamente cargada.
        
        @param alto: Altura que se le quiere asignar a la imagen.
        @type alto: int
        """
        self.image = self.img_aux
        self.image = pygame.transform.smoothscale(self.image, (self.image.get_width(), alto + 20))
        
    def redimensionar(self, ancho, alto):
        """
        Redimensiona el alto y el ancho de una imagen previamente cargada.
        
        @param ancho: Ancho que se le quiere asignar a la imagen.
        @type ancho: int
        @param alto: Altura que se le quiere asignar a la imagen.
        @type alto: int
        """
        self.image = self.img_aux
        self.image = pygame.transform.smoothscale(self.image, (ancho + 20, alto + 20))
        
    def reubicar(self, x, y):
        """
        Reubica una imagen previamente cargada, en las coordenadas especificadas.
        
        @param x: Coordenada X donde se desea reubicar el objeto.
        @type x: int
        @param y: Coordenada Y donde se desea reubicar el objeto.
        @type y: int
        """
        (_,_,w,h) = self.image.get_rect()
        self.rect = pygame.Rect(x, y, w, h)