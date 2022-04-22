#!/usr/bin/env python3

from pygame import Rect, Surface

from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import smoothscale

class Image(Sprite):
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
    
    def get_center(self):
        """
        Obtiene el punto medio de una imagen previamente cargada, relativo al ancho de la pantalla.
        
        @return: Valor del punto medio de la imagen.
        @rtype: bool
        """

        (_, _, width, _) = self.image.get_rect()
        return int(self.x + (width / 2.0))
        
    def resize(self, width = None, height = None):
        """
        Redimensiona el alto de una imagen previamente cargada.
        
        @param alto: Altura que se le quiere asignar a la imagen.
        @type alto: int
        """

        self.image = self._original
        
        if not width:
            (_, _, width, _) = self.image.get_rect()

        if not height:
            (_, _, height, _) = self.image.get_rect()

        self.image = smoothscale(self.image, (width, height))
        
    def relocate(self, x, y):
        """
        Reubica una imagen previamente cargada, en las coordenadas especificadas.
        
        @param x: Coordenada X donde se desea reubicar el objeto.
        @type x: int
        @param y: Coordenada Y donde se desea reubicar el objeto.
        @type y: int
        """

        if x:
            self.rect.x = x
        
        if y:
            self.rect.y = y
