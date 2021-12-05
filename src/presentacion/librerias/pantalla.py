#!/usr/bin/env python

import pygame

from librerias.cursor import cursor
from librerias.boton import RenderBoton
from librerias.animaciones import RenderAnim
from librerias.speechserver import Speechserver
from librerias.magnificador import magnificador, Rendermag

class Pantalla(object):
    """
    Esta clase es una plantilla con atributos y funciones comunes para las pantallas que componen el ReDA
    "Sembrando para el futuro".
    """
    x = ""
    """Indica el objeto actual cuando se utiliza la navegación por teclado. """
    pops = "../imagenes/png/popups/"
    """Ruta de las imágenes de los pop-ups. """
    fondos = "../imagenes/png/fondos/"
    """Ruta de las imágenes de los fondos de pantalla. """
    varios = "../imagenes/png/varios/"
    """Ruta de imágenes variadas. """
    banners = "../imagenes/png/banners/"
    """Ruta de las imágenes de los banner. """
    botones = "../imagenes/png/botones/"
    """Ruta de las imágenes de los botones. """
    anim = "../imagenes/png/animaciones/"
    """Ruta de las imágenes de las animaciones. """
    anim_actual = 0
    """Indica la animación que se esta reproduciendo en un determinado momento. """
    elemento_actual = -1
    """Indica el indice del elemento de la pantalla que esta seleccionado en un determinado momento. """
    numero_elementos = 0  
    """Indica la cantidad de elementos de la pantalla con los que se puede interactuar al usar 
    la navegabilidad por teclado. """
    lista_final = []
    """Lista que contiene todos los elementos de la pantalla accesibles a través de la navegabilidad
    por teclado."""
    lista_botones = []
    """Lista que contiene solo los botones accesibles a través de la navegabilidad por teclado. """
    lista_palabra = []
    """Lista que contiene solo las palabras accesibles a través de la navegabilidad por teclado. """
    rect = pygame.Rect(0, 0, 0, 0)
    """Rectángulo que aparece sobre el elemento actual al usar la navegabilidad por teclado. """
    reloj = pygame.time.Clock()
    """Contador utilizado para sincronizar las animaciones. """
    spserver = Speechserver()
    """Instancia de la clase speechserver, utilizada para enviar información al lector de pantalla. """
    raton = cursor()
    """Instancia de la clase cursor, utilizada para interactuar fácilmente con el ratón. """
    obj_magno = magnificador()
    """Instancia del magnificador de pantalla. """
    grupo_anim = RenderAnim()
    """Grupo en el cual se dibujar las animaciones. """
    grupo_update = RenderAnim()
    """Grupo utilizado para reiniciar varias animaciones simultáneamente. """
    grupo_imagen = RenderAnim()
    """Grupo utilizado para dibujar imágenes de fondo. """
    grupo_botones = RenderBoton()
    """Grupo utilizado para dibujar los botones. """
    grupo_magnificador = Rendermag()
    """Grupo utilizado para dibujar el magnificador de pantalla. """
    grupo_banner = pygame.sprite.Group()
    """Grupo utilizado para dibujar los banner. """
    grupo_tooltip = pygame.sprite.Group()
    """Grupo utilizado para dibujar los tooltip. """
    grupo_mapa = pygame.sprite.OrderedUpdates()
    """Grupo utilizado para dibujar los mapas colisionables. """
    grupo_popup = pygame.sprite.OrderedUpdates()
    """Grupo utilizado para dibujar los mensajes emergentes. """
    grupo_fondotexto = pygame.sprite.GroupSingle()
    """Grupo utilizado para dibujar el fondo de los textos en las pantallas de contenido. """
    grupo_palabras = pygame.sprite.OrderedUpdates()
    """Grupo utilizado para dibujar textos. """
    enable = False
    """Si es True permite cambiar la posición del magnificador de pantalla. 
    Si es falso no se mueve el magnificador. """
    entrada_primera_vez = True
    """Indica la primera vez que se ingresa a una pantalla. Si es False no se ha ingresado, 
    si es True ya fue visitada. """
    deteccion_movimiento = False
    """Indica cuando se utiliza la navegación por teclado para desplazarse por los elementos de la pantalla. """
                
    def limpiar_grupos(self):
        """Limpia los elementos de una pantalla. """
        self.grupo_banner.empty()
        self.grupo_botones.empty()
        self.grupo_imagen.empty()
        self.grupo_palabras.empty()
        self.grupo_fondotexto.empty()
        self.grupo_anim.empty()
        self.grupo_mapa.empty()
        self.grupo_tooltip.empty()
        self.grupo_popup.empty()
        
    def sonido_on(self):
        """Activa un canal de audio para reproducir efectos de sonido. """
        pygame.mixer.init()
        self.canal_audio = pygame.mixer.Channel(0)
        self.canal_audio.set_endevent(pygame.locals.USEREVENT)
        
    def minimag(self, evento):
        """Gestiona los eventos del magnificador de pantalla: activar/desactivar el magnificador de pantalla,
        aumentar y disminuir el zoom.
        
        @param evento: Evento que recibe el magnificador cada vez que la pantalla se actualiza.
        @type evento: pygame.event.Event
        """
        for event in evento:
            if self.parent.config.magnificador:
                (a, b) = pygame.mouse.get_pos()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F5:
                        if self.parent.habilitar == False:
                            self.parent.habilitar = True                        
                            self.grupo_magnificador.add(self.obj_magno)
                        elif self.parent.habilitar == True:
                            self.parent.habilitar = False
                            self.grupo_magnificador.empty()
                    if event.key == pygame.K_PLUS:
                        self.obj_magno.aumentar()
                    elif event.key == pygame.K_MINUS:
                        self.obj_magno.disminuir()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    evento = True
                else:
                    evento = False
                if self.obj_magno.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.enable = True
                    if evento == False:
                        self.obj_magno.rect.left = a - self.obj_magno.w / 2
                        self.obj_magno.rect.top = b - self.obj_magno.h / 2
                else:
                    self.enable = False
    
    def definir_rect (self , rect = 0):
        """Determina la ubicación y dimensiones del rectángulo que indica el elemento actual de la pantalla
        al usar la navegabilidad por teclado.
        
        @change: El rectángulo ahora mide 10 pixeles más de ancho y alto.
        
        @param rect: Contiene las dimensiones y la ubicación del rectángulo que se dibujara. Por defecto su valor
        es 0, lo que indica que el rectángulo no se mostrara en la pantalla.
        @type rect: pygame.Rect
        """
        if rect == 0:
            self.rect = (0, 0, 0, 0)
        else:
            (x,y,w,h) = rect
            self.rect = pygame.Rect(x-5, y-5, w+10, h+10)
            
    def dibujar_rect(self):
        pygame.draw.rect(self.parent.screen, (0,255,0), self.rect, 3)    
        """Dibuja un rectangulo de color verde en la posición y con las dimensiones asignadas en
        'definir_rect()'. """
    def chequeo_palabra(self, lista):
        """
        Verifica si en el texto que se muestra en la pantalla actual, hay palabras interpretables, de ser así
        las agrega en la lista de palabras.
        
        @param lista: Texto que se muestra en una pantalla.
        @type lista: list
        """
        self.lista_palabra = []
        [self.lista_palabra.append(i) for i in lista if i.interpretable]
                
    def chequeo_botones(self, lista):
        """
        Agrega los botones que están presentes en una pantalla en la lista de botones.
        
        @param lista: Botones presentes en la pantalla.
        @type lista: list
        """
        self.lista_botones = []        
        [self.lista_botones.append(j) for j in lista if j.id]
                
    def chequeo_mascaras(self, grupomask):
        """
        Agrega los mapas colisionables a la lista de mascaras.
        
        @param grupomask: Lista de los mapas presentes en la pantalla.
        @type grupomask: list
        """
        self.lista_mascaras = []
        [self.lista_mascaras.append(mask) for mask in grupomask]
                
    def controlador_lector_evento_K_RIGHT(self):
        """
        Gestiona los eventos que se producen cuando se pulsa la flecha derecha del teclado.
        """  
        if self.elemento_actual < self.numero_elementos: 
            self.elemento_actual += 1            
            if self.elemento_actual >= self.numero_elementos:
                self.elemento_actual = self.numero_elementos - 1            
            self.x = self.lista_final[self.elemento_actual]                   
            if self.x.tipo_objeto == "palabra":
                self.definir_rect(self.x.rect)
                self.spserver.processtext(u"explicar la palabra:" + self.x.palabra, self.parent.config.activar_lector)    
                
            elif self.x.tipo_objeto == "mapa":
                self.definir_rect(self.x.rect)
                self.spserver.processtext(self.x.id, self.parent.config.activar_lector) 
                                                     
            elif self.x.tipo_objeto == "boton":
                self.definir_rect(self.x.rect)
                self.spserver.processtext(self.x.tt, self.parent.config.activar_lector)  
                
    def controlador_lector_evento_K_LEFT(self):
        """
        Gestiona los eventos que se producen cuando se pulsa la flecha izquierda del teclado.
        """  
        if self.elemento_actual > 0:
            self.elemento_actual -= 1
            if self.elemento_actual <= 0:
                self.elemento_actual = 0
            self.x = self.lista_final[self.elemento_actual]
            if self.x.tipo_objeto == "palabra":
                self.definir_rect(self.x.rect)
                self.spserver.processtext(u"explicar la palabra:"+ self.x.palabra, self.parent.config.activar_lector)     
            
            elif self.x.tipo_objeto == "mapa":
                self.definir_rect(self.x.rect)
                self.spserver.processtext(self.x.id, self.parent.config.activar_lector) 
                                                     
            elif self.x.tipo_objeto == "boton":
                self.definir_rect(self.x.rect)
                self.spserver.processtext(self.x.tt, self.parent.config.activar_lector)
