#!/usr/bin/env python3

from pygame import Rect

from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import smoothscale

class GameObject(Sprite):
    def __init__(self, x, y, imagen, nombre):
        Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = load(imagen).convert_alpha()
        self.rect = Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        
    def get_center(self):
        """
        Obtiene el punto medio de una imagen previamente cargada, relativo al ancho de la pantalla.
        
        @return: Valor del punto medio de la imagen.
        @rtype: bool
        """

        (_, _, width, _) = self.image.get_rect()
        return int(self.x + (width / 2.0))

    def relocate(self, x = None, y = None):
        """
        Reubica un objeto previamente creado, en las coordenadas especificadas.
        
        @param x: Coordenada X donde se desea reubicar el objeto.
        @type x: int
        @param y: Coordenada Y donde se desea reubicar el objeto.
        @type y: int
        """

        if x:
            self.rect.x = x
        if y:
            self.rect.y = y

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
    

    def set_center(self, x, y):
        self.rect.center = (x, y)

class PropObject(GameObject):
    """
    Esta clase define objetos con los que el personaje puede interactuar en la actividad 1.
    
    @todo: Crear una superclase 'objeto' que defina los métodos usados por las clases: imagen, objeto, entre otras.    
    """

    aumentos = {
        "la carretilla. ":1, 
        "las semillas. ":1, 
        "la regadera. ":2, 
        "la pala. ":4, 
        "el abono. ":8, 
        u"el controlador biológico. ":16
    }
    
    """
    Es un diccionario que asigna a cada tipo de objeto un valor de aumento para calcular los cambios
    de imágen en la clase personaje. 
    """

    def __init__(self, posx, posy, imagen, nombre):
        """
        Método inicializador de la clase.
        
        @param posx: Coordenada X donde se desea dibujar el objeto.
        @type posx: int
        @param posy: Coordenada Y donde se desea dibujar el objeto.
        @type posy: int
        @param imagen: Ruta de la imagen que representa al objeto.
        @type imagen: str
        @param nombre: Identificador que representa al objeto.
        @type nombre: str
        """

        Sprite.__init__(self)
        self.nombre = nombre
        self.x = posx
        self.y = posy
        self.image = load(imagen).convert_alpha()
        self.rect = Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.aumento = self.aumentos[nombre]
