#!/usr/bin/env python3

from pygame import Rect

from pygame.image import load
from pygame.sprite import Sprite

class GameObject(Sprite):
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
        
    def relocate(self, x, y):
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

