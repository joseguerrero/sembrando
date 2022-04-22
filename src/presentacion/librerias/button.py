#!/usr/bin/env python3

from pygame import error, Rect, Surface

from pygame import (
    RLEACCEL
)

from pygame.image import load
from pygame.font import SysFont
from pygame.mouse import get_pos
from pygame.sprite import Group, OrderedUpdates, Sprite

from manejador import Manejador as parent

class SpriteSheet(object):
    """
    Esta clase se encarga de transformar una imagen en una tira de imágenes que simula ser un botón animado.
    """
    
    def __init__(self, filename):
        try:
            self.sheet = load(filename).convert_alpha()
        except(error):
            raise(SystemExit)
    
    def image_at(self, rectangle, colorkey = None):
        rect = Rect(rectangle)
        image = self.sheet.subsurface(rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey , RLEACCEL)
        return image
    
    def load_images_at(self, rects, colorkey = None):
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
    
    def load_strip(self, rect, frames, colorkey = None):
        """
        Carga una lista de imágenes.
        
        @param rect: Lista de los rectángulos de cada imagen.
        @type rect: list
        @param frames: Numero de columnas que tendrá la tira de imágenes.
        @type frames: int
        @param colorkey: Define el color utilizado como transparencia, por defecto no es necesario.
        @type colorkey: tuple
        @return: Lista de imágenes que conforman la tira de imágenes.
        @rtype: list
        """
        
        tuples = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
                for x in range(frames)]
        return self.load_images_at(tuples, colorkey)

class Button(Sprite):
    """
    Esta clase permite crear y manipular botones animados a partir de una tira de imágenes.
    """
    
    def __init__(self, x, y, id, tooltip, filename, frames, colorkey = None, loop = False, frame_speed = 1):
        """
        Método inicializador de la clase.
        
        @param x: Coordenada X en la que se comenzara a dibujar el botón.
        @type x: int
        @param y : Coordenada Y en la que se comenzara a dibujar el botón.
        @type y: int
        @param id: Identificador único para cada instancia de esta clase.
        @type id: str
        @param tooltip: Nombre del texto de ayuda que aparece cuando se coloca el cursor sobre el botón.
        @type tooltip: str
        @param filename: Ruta de la imagen que se desea utilizar como botón.
        @type filename: str
        @param frames: Numero de columnas que contiene la imagen.
        @type frames: int
        @param colorkey: Define el color utilizado como transparencia, por defecto no es necesario.
        @type colorkey: tuple
        @param loop: Por defecto es False en todos los botones.
        @type loop: bool
        @param frame_speed: Indica la velocidad a la que se cambian los fotogramas del botón animado, siendo 1 el 
        valor mas rápido.
        @type frame_speed: int
        """

        Sprite.__init__(self)
        self.x = x
        self.y = y
        self.id = id
        self.parent = parent

        # Boolean states
        self.loop = loop
        self.stop = True
        self.sonar = True

        # Tooltip attributes
        my_font = SysFont("arial", self.parent.config.t_fuente)
        self.tooltip = tooltip
        self.texto = Sprite()
        self.texto.image = my_font.render(self.tooltip, True, (0, 0, 0), (230, 230, 130))
        self.texto.rect = Rect((0, 0, 0, 0))
        self.grupo_tooltip = Group()

        ss = SpriteSheet(filename)
        self.current_image = Surface((0,0))
        (_, _, width, height) = ss.sheet.get_rect()
        self.rect = Rect(x, y, int(width / frames), height)
        rt  = Rect(0, 0, int(width / frames), height)
        self.images = ss.load_strip(rt, frames, colorkey)
        
        self.current_frame = 0
        self.frame_speed = frame_speed
        self.frame_delta = frame_speed
        if self.frame_speed == 1:
            self.current_image = self.images[0]

    def update(self, grupo):
        """
        Llama al método colision() para determinar si el cursor pasa sobre un botón.
        De ser así muestra el mensaje de ayuda (tooltip) correspondiente. En caso contrario elimina el
        mensaje de ayuda del grupo de sprites.
               
        @param grupo: Grupo de sprites al que se agregara el mensaje de ayuda.
        @type grupo: pygame.sprite.Group()
        """

        if self.detect_collision():
            if not self.tooltip == "none":
                grupo.add(self.texto)
        else:
            grupo.remove(self.texto)
        
    def relocate(self, x = None, y = None):
        """
        Permite cambiar la posición en X e Y del botón.
        
        @param x: Nueva posición en X donde se desea ubicar el botón.
        @type x: int
        @param y: Nueva posición en Y donde se desea ubicar el botón.
        @type y: int
        @note: Esta función puede sustituir a la función mover() mencionada anteriormente.
        """

        if x:
            self.rect.x = x
        
        if y:
            self.rect.y = y

    def play_animation(self):
        """
        Anima el botón.
        """

        self.stop = False
        
    def stop_animation(self):
        """
        Detiene la animación del botón.
        """

        self.stop = True
    
    def replay_animation(self):
        """
        Repite la secuencia de una animación. A diferencia del método update(), este método se utiliza para 
        volver a reproducir animaciones que solo se reproducen una vez. 
        """

        self.stop = False
        self.current_frame = 0
    
    def next(self):
        """
        Actualiza la imagen que se debe dibujar en pantalla cada vez que esta se actualiza.
        """

        if self.current_frame >= len(self.images):
            if self.loop:
                self.current_frame = 0
            else:
                self.stop = True

        if not self.stop:
            self.current_image = self.images[self.current_frame]
            self.frame_delta -= 1
            if self.frame_delta == 0:
                self.current_frame += 1
                self.frame_delta = self.frame_speed

    def play_sound(self, canal):
        """
        Reproduce el sonido predeterminado del botón.
        
        @param canal: Canal a través del cual se reproduce el sonido del botón.
        @type canal: pygame.mixer.Channel
        """

        if self.detect_collision() and canal.get_busy and self.sonar:
            self.sonar = False
            #canal.play(self.sonido)
    
    def detect_collision(self):
        """
        Determina si existe una colisión entre el cursor y rectángulo del botón.
        
        @return: Devuelve True si el cursor se encuentra sobre el botón al momento de llamar a esta función.
        De lo contrario devuelve False.
        @rtype: bool
        """

        if self.rect.collidepoint(get_pos()):
            self.play_animation()
            if get_pos()[0] >= (1024 - self.texto.image.get_width()):
                x = 1024 - self.texto.image.get_width() - 10
                # The tooltip text is always rendered with a small offset
                # hence the +10 and +20 values
                self.texto.rect = ((x + 10 , get_pos()[1] + 20, 0, 0))
            else:
                self.texto.rect = ((get_pos()[0] + 10, get_pos()[1] + 20, 0, 0))
            return True  
        else:
            self.sonar = True
            self.grupo_tooltip.empty()
            self.stop_animation()
            self.current_frame = 0
            self.current_image = self.images[0]
            self.stop = True
            return False
    
class RenderButton(OrderedUpdates):
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
            self.spritedict[spr] = surface_blit(spr.current_image, spr.rect)
            spr.next()
