#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from manejador import Manejador as parent

class spritesheet(object):
    """
    Esta clase se encarga de transformar una imagen en una tira de imágenes que simula ser un botón animado.
    """
    
    def __init__(self, filename):
        """
        Método inicializador de la clase.
        
        @param filename: Ruta de la imagen que se desea cargar para convertir en una tira de imágenes. 
        @type filename: str
        """
        
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except(pygame.error, message):
            raise(SystemExit, message)
    
    def image_at(self, rectangle, colorkey = None):
        """
        Carga una imagen suministrando el rectángulo en el que esta ubicada.
        
        @param rectangle: Rectángulo que especifica la zona de la imagen principal de la que se obtiene un 
        fotograma.
        @type rectangle: pygame.Rect
        @param colorkey: Define el color utilizado como transparencia, por defecto no es necesario.
        @type colorkey: tuple
        @return: Imagen en la ubicación suministrada.
        @rtype: pygame.Surface
        """
        
        rect = pygame.Rect(rectangle)
        image = self.sheet.subsurface(rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey , pygame.RLEACCEL)
        return image
    
    def images_at(self, rects, colorkey = None):
        """
        Carga varias imágenes suministrando una lista de rectángulos que contiene respectivamente a cada imagen.
        
        @param rects: Define el conjunto de rectángulos que sera parte de la tira de imágenes.
        @type rects: list
        @param colorkey: Define el color utilizado como transparencia, por defecto no es necesario.
        @type colorkey: tuple
        @return: Lista de las imágenes cargadas.
        @rtype: list
        """
        
        return [self.image_at(rect, colorkey) for rect in rects]
    
    def load_strip(self, rect, image_count, colorkey = None):
        """
        Carga una lista de imágenes.
        
        @param rect: Lista de los rectángulos de cada imagen.
        @type rect: list
        @param image_count: Numero de columnas que tendrá la tira de imágenes.
        @type image_count: int
        @param colorkey: Define el color utilizado como transparencia, por defecto no es necesario.
        @type colorkey: tuple
        @return: Lista de imágenes que conforman la tira de imágenes.
        @rtype: list
        """
        
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

class boton(pygame.sprite.Sprite):
    """
    Esta clase permite crear y manipular botones animados a partir de una tira de imágenes.
    """
    
    def __init__(self, id, tooltip, filename, count, x, y, colorkey = None, loop = False, frames = 1):
        """
        Método inicializador de la clase.
        
        @param id: Identificador único para cada instancia de esta clase.
        @type id: str
        @param tooltip: Nombre del texto de ayuda que aparece cuando se coloca el cursor sobre el botón.
        @type tooltip: str
        @param filename: Ruta de la imagen que se desea utilizar como botón.
        @type filename: str
        @param count: Numero de columnas que contiene la imagen.
        @type count: int
        @param x: Coordenada X en la que se comenzara a dibujar el botón.
        @type x: int
        @param y : Coordenada Y en la que se comenzara a dibujar el botón.
        @type y: int
        @param colorkey: Define el color utilizado como transparencia, por defecto no es necesario.
        @type colorkey: tuple
        @param loop: Por defecto es False en todos los botones.
        @type loop: bool
        @param frames: Indica la velocidad a la que se cambian los fotogramas del botón animado, siendo 1 el 
        valor mas rápido.
        @type frames: int
        """
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.id = id
        self.tipo_objeto = "boton"
        self.parent = parent
        #self.sonido =  pygame.mixer.Sound("audio/gnr.ogg")
        my_font = pygame.font.SysFont("arial", self.parent.config.t_fuente)
        self.tt = tooltip
        self.texto = pygame.sprite.Sprite()
        self.texto.image = my_font.render(self.tt, True, (0, 0, 0), (233, 234, 131))
        self.texto.rect = pygame.Rect((0, 0, 0, 0))
        self.grupo_tooltip = pygame.sprite.Group()
        self.filename = filename
        ss = spritesheet(filename)
        (_,_, w,h) = ss.sheet.get_rect()
        self.rect = pygame.Rect(x, y, int(w/count), h)
        rt = pygame.Rect(0, 0, int(w/count), h)
        self.images = ss.load_strip(rt, count, colorkey)
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames
        self.image = pygame.Surface((0,0))
        self.stop = True
        self.sonar = True
        if frames == 1:
            self.image = self.images[0]
            
    def update(self, grupo):
        """
        Llama al método colision() para determinar si el cursor pasa sobre un botón.
        De ser así muestra el mensaje de ayuda (tooltip) correspondiente. En caso contrario elimina el
        mensaje de ayuda del grupo de sprites.
               
        @param grupo: Grupo de sprites al que se agregara el mensaje de ayuda.
        @type grupo: pygame.sprite.Group()
        """
        if self.colision():
            if not self.tt == "none": 
                grupo.add(self.texto)
        else:
            grupo.remove(self.texto)
            
    def mover(self, valor):
        """
        Permite cambiar la posición en X del botón.
        
        @param valor: Nueva posición en X donde se desea ubicar el botón.
        @type valor: int
        """
        (_,y,w,h) = self.rect
        self.rect = pygame.Rect(valor,y,w,h)
        
    def reubicar(self, x, y):
        """
        Permite cambiar la posición en X e Y del botón.
        
        @param x: Nueva posición en X donde se desea ubicar el botón.
        @type x: int
        @param y: Nueva posición en Y donde se desea ubicar el botón.
        @type y: int
        @note: Esta función puede sustituir a la función mover() mencionada anteriormente.
        """
        (_, _, w, h) = self.image.get_rect()
        self.rect = pygame.Rect(x, y, w, h)
              
    def animar(self):
        """
        Anima el botón.
        """
        self.stop = False
        
    def detener(self):
        """
        Detiene la animación del botón.
        """
        self.stop = True
    
    def repetir(self):
        """
        Repite la secuencia de una animación. A diferencia del método update(), este método se utiliza para 
        volver a reproducir animaciones que solo se reproducen una vez. 
        """
        self.stop = False
        self.i = 0
    
    def next(self):
        """
        Actualiza la imagen que se debe dibujar en pantalla cada vez que esta se actualiza.
        """
        if self.i >= len(self.images):
            if not self.loop:
                self.stop = True
            else:
                self.i = 0
        if not self.stop: 
            self.image = self.images[self.i]
            self.f -= 1
            if self.f == 0:
                self.i += 1
                self.f = self.frames
    
    def reproducir(self, canal):
        """
        Reproduce el sonido predeterminado del botón.
        
        @param canal: Canal a través del cual se reproduce el sonido del botón.
        @type canal: pygame.mixer.Channel
        """
        if self.colision() and canal.get_busy and self.sonar:
            self.sonar = False
            #canal.play(self.sonido)
    
    def colision(self):
        """
        Determina si existe una colisión entre el cursor y rectángulo del botón.
        
        @return: Devuelve True si el cursor se encuentra sobre el botón al momento de llamar a esta función.
        De lo contrario devuelve False.
        @rtype: bool
        """
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.animar()            
            if pygame.mouse.get_pos()[0] >= (1024 - self.texto.image.get_width()):
                x = 1024 - self.texto.image.get_width() - 10
                self.texto.rect = ((x + 10 , pygame.mouse.get_pos()[1] + 20, 0, 0))
            else:
                self.texto.rect = ((pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 20, 0, 0))
            return True  
        else:
            self.sonar = True
            self.grupo_tooltip.empty()
            self.detener()
            self.i = 0
            self.image = self.images[0]
            self.stop = True
            return False
    
class RenderBoton(pygame.sprite.OrderedUpdates):
    """
    Esta clase es una ligera modificación de la clase pygame.sprite.OrderedUpdates. 
    Permite cambiar el fotograma de la imagen cada cierto tiempo al actualizar la pantalla. 
    """
    def draw(self, surface):
        """
        Dibuja los miembros de un grupo de sprites sobre una superficie.
        
        @param surface: Superficie sobre la que se dibujaran los sprites pertenecientes a este grupo.
        @type surface: pygame.Surface
        """
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            self.spritedict[spr] = surface_blit(spr.image, spr.rect)
            spr.next()