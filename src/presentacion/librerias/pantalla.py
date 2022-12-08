#!/usr/bin/env python

import pygame

from librerias.animations import Animation, RenderAnim
from librerias.image import Image
from librerias.cursor import cursor
from librerias.button import Button, RenderButton
from librerias.speechserver import Speechserver
from librerias.magnificador import magnificador, Rendermag
from librerias.assets_data import *


class Pantalla(object):
    """
    Esta clase es una plantilla con atributos y funciones comunes para las pantallas que componen el ReDA
    "Sembrando para el futuro".
    """

    x = ""
    """Indica el objeto actual cuando se utiliza la navegación por teclado. """
    pops = "../imagenes/png/popups/"
    """Ruta de las imágenes de los pop-ups. """

    animations_path = "../imagenes/png/animations/"
    backgrounds_path = "../imagenes/png/backgrounds/"
    banners_path = "../imagenes/png/banners/"
    buttons_path = "../imagenes/png/buttons/"

    varios = "../imagenes/png/varios/"
    """Ruta de imágenes variadas. """

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
    """Contador utilizado para sincronizar las animationes. """
    spserver = Speechserver()
    """Instancia de la clase speechserver, utilizada para enviar información al lector de pantalla. """
    raton = cursor()
    """Instancia de la clase cursor, utilizada para interactuar fácilmente con el ratón. """
    obj_magno = magnificador()
    """Instancia del magnificador de pantalla. """
    grupo_anim = RenderAnim()
    """Grupo en el cual se dibujar las animationes. """
    grupo_update = RenderAnim()
    """Grupo utilizado para reiniciar varias animationes simultáneamente. """
    grupo_imagen = RenderAnim()
    """Grupo utilizado para dibujar imágenes de fondo. """
    grupo_botones = RenderButton()
    """Grupo utilizado para dibujar los botones. """
    grupo_magnificador = Rendermag()
    """Grupo utilizado para dibujar el magnificador de pantalla. """
    grupo_banner = pygame.sprite.Group()
    """Grupo utilizado para dibujar los banner. """
    grupo_tooltip = pygame.sprite.Group()
    """Grupo utilizado para dibujar los tooltip. """

    grupo_cuadro_texto = pygame.sprite.Group()

    text_button_group = pygame.sprite.Group()

    grupo_mapa = pygame.sprite.OrderedUpdates()
    """Grupo utilizado para dibujar los mapas colisionables. """
    grupo_popup = pygame.sprite.OrderedUpdates()
    """Grupo utilizado para dibujar los mensajes emergentes. """
    grupo_fondotexto = pygame.sprite.GroupSingle()
    """Grupo utilizado para dibujar el fondo de los textos en las pantallas de contenido. """
    grupo_palabras = pygame.sprite.OrderedUpdates()
    """Grupo utilizado para dibujar textos. """

    debug_groups = [
        grupo_imagen,
        grupo_botones,
        text_button_group,
        grupo_banner,
        grupo_tooltip,
        grupo_popup,
        grupo_palabras,
        grupo_cuadro_texto,
    ]

    enable = False
    """Si es True permite cambiar la posición del magnificador de pantalla. 
    Si es falso no se mueve el magnificador. """
    entrada_primera_vez = True
    """Indica la primera vez que se ingresa a una pantalla. Si es False no se ha ingresado, 
    si es True ya fue visitada. """
    deteccion_movimiento = False
    """Indica cuando se utiliza la navegación por teclado para desplazarse por los elementos de la pantalla. """

    def __init__(self, parent, screen_id):
        self.parent = parent
        self.load_background(screen_id)
        self.previa = True
        self.reloj_anim = pygame.time.Clock()
        self.reloj_anim.tick(30)
        self.rect = pygame.Rect(0, 0, 0, 0)

    def load_animations(self, animation_ids):
        for id in animation_ids:
            x, y = animations.get(id).get("coordinates")
            columns = animations.get(id).get("columns")
            rows = animations.get(id).get("rows")
            colorkey = animations.get(id).get("colorkey")
            loop = animations.get(id).get("loop")
            frames = animations.get(id).get("frames")
            filename = animations.get(id).get("filename")
            attribute_name = id.replace("-", "_")
            setattr(
                self,
                attribute_name,
                Animation(
                    id,
                    self.animations_path + filename,
                    columns,
                    rows,
                    x,
                    y,
                    colorkey,
                    loop,
                    frames,
                ),
            )

    def load_background(self, screen_id):
        self.background = pygame.image.load(
            self.backgrounds_path + backgrounds.get(screen_id)
        ).convert()

    def load_buttons(self, button_ids):
        for id in button_ids:
            x, y = buttons.get(id).get("coordinates")
            tooltip = buttons.get(id).get("tooltip")
            colorkey = buttons.get(id).get("colorkey")
            loop = buttons.get(id).get("loop")
            frames = buttons.get(id).get("frames")
            frame_speed = buttons.get(id).get("frame_speed")
            filename = buttons.get(id).get("filename")
            attribute_name = id.replace("-", "_")
            setattr(
                self,
                attribute_name,
                Button(
                    x,
                    y,
                    id,
                    tooltip,
                    self.buttons_path + filename,
                    frames,
                    colorkey,
                    loop,
                    frame_speed,
                ),
            )

    def load_banners(self, banner_ids):
        for id in banner_ids:
            x, y = banners.get(id).get("coordinates")
            filename = banners.get(id).get("filename")
            attribute_name = id.replace("-", "_")
            setattr(self, attribute_name, Image(x, y, self.banners_path + filename))

    def load_images(self, image_ids):
        for id in image_ids:
            filename = images.get(id)
            attribute_name = id.replace("-", "_")
            setattr(
                self,
                attribute_name,
                pygame.image.load(self.pops + filename).convert_alpha(),
            )

    def limpiar_grupos(self):
        """Limpia los elementos de una pantalla."""
        self.grupo_banner.empty()
        self.grupo_botones.empty()
        self.text_button_group.empty()
        self.grupo_imagen.empty()
        self.grupo_palabras.empty()
        self.grupo_fondotexto.empty()
        self.grupo_anim.empty()
        self.grupo_mapa.empty()
        self.grupo_tooltip.empty()
        self.grupo_popup.empty()
        self.grupo_cuadro_texto.empty()

    def sonido_on(self):
        """Activa un canal de audio para reproducir efectos de sonido."""
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
                if (
                    self.obj_magno.rect.collidepoint(pygame.mouse.get_pos())
                    and pygame.mouse.get_pressed()[0]
                ):
                    self.enable = True
                    if evento == False:
                        self.obj_magno.rect.left = a - self.obj_magno.w / 2
                        self.obj_magno.rect.top = b - self.obj_magno.h / 2
                else:
                    self.enable = False

    def definir_rect(self, rect=0):
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
            (x, y, w, h) = rect
            self.rect = pygame.Rect(x - 5, y - 5, w + 10, h + 10)

    def dibujar_rect(self):
        pygame.draw.rect(self.parent.screen, (0, 255, 0), self.rect, 3)
        """Dibuja un rectangulo de color verde en la posición y con las dimensiones asignadas en
        'definir_rect()'. """

    def draw(self):
        """
        Dibuja el fondo de pantalla y los elementos pertenecientes a los grupos de sprites sobre la superficie
        del manejador de pantallas.
        """

        self.parent.screen.blit(self.background, (0, 0))
        self.grupo_imagen.draw(self.parent.screen)
        self.grupo_anim.draw(self.parent.screen)
        self.grupo_banner.draw(self.parent.screen)
        self.grupo_botones.draw(self.parent.screen)
        self.grupo_fondotexto.draw(self.parent.screen)
        self.grupo_palabras.draw(self.parent.screen)
        self.grupo_tooltip.draw(self.parent.screen)
        self.grupo_popup.draw(self.parent.screen)
        if self.parent.habilitar:
            self.grupo_magnificador.draw(self.parent.screen, self.enable)
        if self.deteccion_movimiento:
            self.dibujar_rect()
        self.draw_debug_rectangles()

    def draw_debug_rectangles(self):
        if self.parent.DRAW_DEBUG_RECTANGLES:
            debug_rectangles = [
                object.rect for group in self.debug_groups for object in group
            ]
            for rectangle in debug_rectangles:
                pygame.draw.rect(self.parent.screen, (255, 0, 0), rectangle, 3)

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
                self.spserver.processtext(
                    "explicar la palabra:" + self.x.palabra,
                    self.parent.config.activar_lector,
                )

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
                self.spserver.processtext(
                    "explicar la palabra:" + self.x.palabra,
                    self.parent.config.activar_lector,
                )

            elif self.x.tipo_objeto == "mapa":
                self.definir_rect(self.x.rect)
                self.spserver.processtext(self.x.id, self.parent.config.activar_lector)

            elif self.x.tipo_objeto == "boton":
                self.definir_rect(self.x.rect)
                self.spserver.processtext(self.x.tt, self.parent.config.activar_lector)

    def start(self):
        pass

    def cleanUp(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass
