#!/usr/bin/env python3

from pygame import Rect, Surface

from pygame.image import load
from pygame.sprite import Sprite

from .object import GameObject

class Image(GameObject):
    """
    Esta clase permite cargar una imagen y realizar ciertas operaciones básicas.
    
    @todo: Crear una superclase 'objeto' que defina los métodos usados por las clases: imagen, objeto, entre otras.
    """

    # Backup of the original surface
    _original = Surface((0, 0))
    
    def __init__(self, x, y, image):
        """
        Método inicializador de la clase.
        
        @param imagen: Ruta de la imagen que se desea cargar.
        @type imagen: str
        @param x: Coordenada X donde se desea dibujar la imagen.
        @type x: int
        @param y: Coordenada Y donde se desea dibujar la imagen.
        @type y: int
        """

        Sprite.__init__(self)

        self.image = load(image).convert_alpha()
        self._original = self.image
        (_, _, width, height) = self.image.get_rect()
        self.rect = Rect(x, y, width, height)
