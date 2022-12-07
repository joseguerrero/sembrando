#!/usr/bin/env python

import pygame

from librerias import pantalla
from librerias.button import Button
from librerias.popups import PopUp
from librerias.image import Image
from paginas import pantalla2, menuauditivo, menuvisual


class estado(pantalla.Pantalla):
    def __init__(self, parent, previa=False):
        """
        Método inicializador de la clase.
        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        @param previa: Si es True indica que esta pantalla esta apilada sobre otra. Si es False indica que esta
        pantalla fue cargada a través del método changeState del Manejador.
        @type previa: bool
        """

        self.name = "screen_1"
        self.previa = previa
        self.parent = parent
        self.background = pygame.image.load(self.fondos + "fondo-inicio.png").convert()
        self.fondo_simple = pygame.image.load(
            self.fondos + "fondo-simple.png"
        ).convert()
        self.banner_inf = Image(
            0,
            432,
            self.banners + "banner-inf.png",
        )
        self.banner_config = Image(
            0,
            0,
            self.banners + "banner-acc.png",
        )
        self.cargar_botones()
        self.cargar_img_intrucciones()
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.resume()

    def cargar_img_intrucciones(self):
        """
        Carga las imágenes usadas para las instrucciones iniciales.
        """
        self.img1 = pygame.image.load(self.pops + "touch.png").convert_alpha()
        self.img2 = pygame.image.load(self.pops + "flechas.png").convert_alpha()
        self.img3 = pygame.image.load(self.pops + "enter.png").convert_alpha()
        self.img4 = pygame.image.load(self.pops + "f1.png").convert_alpha()
        self.img5 = pygame.image.load(self.pops + "sordo.png").convert_alpha()
        self.img6 = pygame.image.load(self.pops + "visual.png").convert_alpha()
        self.dic_img = {
            "RATON": self.img1,
            "TECLAS": self.img2,
            "ENTER": self.img3,
            "F1": self.img4,
            "DFA": self.img5,
            "DFV": self.img6,
        }

    def cargar_botones(self):
        """
        Carga los botones utilizados en esta pantalla.
        """
        self.puerta = Button(
            650,
            425,
            "puerta",
            "Regresar",
            self.botones + "boton-puerta.png",
            3,
            None,
            False,
            1,
        )
        self.boton_sordo = Button(
            300,
            440,
            "sordo",
            "Discapacidad auditiva",
            self.botones + "boton-sordo.png",
            3,
            None,
            False,
            1,
        )
        self.boton_visual = Button(
            483,
            430,
            "config-vis",
            "Discapacidad visual",
            self.botones + "boton-visual.png",
            3,
            None,
            False,
            1,
        )
        self.inicio = Button(
            650,
            440,
            "inicio",
            "Inicio",
            self.botones + "boton-inicio.png",
            3,
            None,
            False,
            1,
        )

    def start(self):
        pass

    def cleanUp(self):
        pass

    def pause(self):
        pass

    def resume(self):
        """
        Verifica si es la primera vez que se muestra esta pantalla. Carga los objetos correspondientes
        según el caso.
        """
        if self.parent.VOLVER_PANTALLA_PREVIA:
            self.parent.VOLVER_PANTALLA_PREVIA = False
            self.limpiar_grupos()
            self.parent.popState()
        else:
            if self.parent.primera_vez:
                self.cargar_botones()
                self.grupo_banner.add(self.banner_inf)
                self.grupo_botones.add(self.boton_sordo, self.boton_visual, self.inicio)
                self.popup_ins = PopUp(
                    self.parent,
                    # TODO: If the parent is already being passed we can grab the
                    # text from the parent's dict, we would only need to pass the
                    # screen name and maybe the "popups" key
                    self.parent.text_content["popups"][self.name]["text_1"],
                    "",
                    self.dic_img,
                    self.grupo_popup,
                    2,
                    512,
                    290,
                    100,
                )

                self.popup_ins.agregar_grupo()
                self.spserver.processtext(
                    self.parent.text_content["popups"][self.name]["reader_1"], True
                )
            else:
                self.background = self.fondo_simple
                if self.parent.config.texto_cambio == True:
                    self.cargar_botones()
                    self.parent.config.texto_cambio = False
                self.popup_ins = PopUp(
                    self.parent,
                    self.parent.text_content["popups"][self.name]["text_2"],
                    "",
                    self.dic_img,
                    self.grupo_popup,
                    2,
                    512,
                    270,
                    100,
                )
                self.popup_ins.agregar_grupo()
                self.spserver.processtext(
                    self.parent.text_content["popups"][self.name]["reader_2"], True
                )
                self.grupo_banner.add(self.banner_config, self.banner_inf)
                self.grupo_botones.add(self.boton_sordo, self.boton_visual, self.puerta)

    def handleEvents(self, events):
        """
        Evalúa los eventos que se generan en esta pantalla.

        @param events: Lista de los eventos.
        @type events: list
        """
        self.teclasPulsadas = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                self.parent.quit()

            if event.type == pygame.KEYDOWN:
                self.chequeo_botones(self.grupo_botones)
                self.numero_elementos = len(self.lista_botones)

                if event.key == pygame.K_RIGHT:
                    if self.elemento_actual < self.numero_elementos:
                        self.elemento_actual += 1
                        if self.elemento_actual >= self.numero_elementos:
                            self.elemento_actual = self.numero_elementos - 1
                        self.x = self.lista_botones[self.elemento_actual]
                        self.spserver.processtext(self.x.tt, True)
                        self.definir_rect(self.x.rect)
                        self.deteccion_movimiento = True

                elif event.key == pygame.K_LEFT:
                    if self.elemento_actual > 0:
                        self.elemento_actual -= 1
                        if self.elemento_actual <= 0:
                            self.elemento_actual = 0
                        self.x = self.lista_botones[self.elemento_actual]
                        self.spserver.processtext(self.x.tt, True)
                        self.definir_rect(self.x.rect)
                        self.deteccion_movimiento = True

                elif self.deteccion_movimiento:
                    if event.key == pygame.K_RETURN:
                        self.elemento_actual = -1
                        if self.x.tipo_objeto == "boton":
                            if self.x.id == "sordo":
                                self.limpiar_grupos()
                                self.parent.pushState(
                                    menuauditivo.estado(self.parent, self.previa)
                                )

                            elif self.x.id == "config-vis":
                                self.limpiar_grupos()
                                self.parent.pushState(
                                    menuvisual.estado(self.parent, self.previa)
                                )

                            elif self.x.id == "inicio":
                                self.limpiar_grupos()
                                self.parent.changeState(pantalla2.estado(self.parent))

                            elif self.x.id == "puerta":
                                self.limpiar_grupos()
                                self.parent.popState()

            if pygame.sprite.spritecollideany(self.raton, self.grupo_botones):
                sprite = pygame.sprite.spritecollide(
                    self.raton, self.grupo_botones, False
                )
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.spserver.stopserver()
                    if sprite[0].id == "inicio":
                        self.limpiar_grupos()
                        self.parent.changeState(pantalla2.estado(self.parent))

                    elif sprite[0].id == "puerta":
                        self.limpiar_grupos()
                        self.parent.popState()

                    elif sprite[0].id == "sordo":
                        self.limpiar_grupos()
                        self.parent.pushState(
                            menuauditivo.estado(self.parent, self.previa)
                        )

                    elif sprite[0].id == "config-vis":
                        self.limpiar_grupos()
                        self.parent.pushState(
                            menuvisual.estado(self.parent, self.previa)
                        )
        self.minimag(events)

    def update(self):
        """
        Actualiza la posición del cursor, el magnificador de pantalla en caso de que este activado y los
        tooltip de los botones.
        """
        self.raton.update()
        self.obj_magno.magnificar(self.parent.screen)
        self.grupo_botones.update(self.grupo_tooltip)
