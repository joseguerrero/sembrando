#!/usr/bin/env python

import pygame

from librerias import pantalla
from librerias.button import Button
from librerias.popups import PopUp
from librerias.image import Image

from paginas import menucfg
from paginas import pantalla3
from paginas import pantalla5
from paginas import pantalla8
from paginas import pantalla11
from paginas import actividad1
from paginas import actividad2


class estado(pantalla.Pantalla):
    def __init__(self, parent):
        """
        Método inicializador de la clase.

        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        """

        self.name = "screen_2"
        self.parent = parent
        self.previa = True
        self.display_help = False

        self.background = pygame.image.load(self.fondos + "fondo-inicio.png").convert()
        self.banner_inf = Image(0, 432, self.banners + "banner-inf.png")
        self.img1 = pygame.image.load(self.pops + "f1.png").convert_alpha()
        self.dic_img = {"F1": self.img1}
        self.cargar_botones()
        self.cargar_textos()
        self.reloj_anim = pygame.time.Clock()
        self.reloj_anim.tick(30)
        self.tiempo = 0
        self.creado = True
        self.final = False
        self.elemento_actual = -1
        self.deteccion_movimiento = False
        self.resume()

    def show_instructions(self):
        """
        Muestra las instrucciones de uso de la pantalla actual.
        """
        if not self.popup_ins.activo:
            self.popup_ins.agregar_grupo()
            self.spserver.processtext(
                self.parent.text_content["popups"][self.name]["reader_1"],
                self.parent.config.activar_lector,
            )

        else:
            self.popup_ins.eliminar_grupo()
            self.spserver.stopserver()

    def cargar_textos(self):
        """
        Carga los textos utilizados en esta pantalla.
        """
        self.popup_ins = PopUp(
            self.parent,
            self.parent.text_content["popups"][self.name]["text_1"],
            "",
            self.dic_img,
            self.grupo_popup,
            2,
            512,
            265,
            100,
        )

    def cargar_botones(self):
        """
        Carga los botones utilizados en esta pantalla.
        """
        self.nino = Button(
            400,
            150,
            "act1",
            "Siembra la semilla",
            self.botones + "boton-nino.png",
            8,
            None,
            True,
            12,
        )
        self.nina = Button(
            570,
            150,
            "act2",
            "Plantas y números",
            self.botones + "boton-nina.png",
            8,
            None,
            True,
            12,
        )
        self.plantas = Button(
            0,
            80,
            "plantas",
            "Las plantas",
            self.botones + "boton-plantas.png",
            8,
            None,
            False,
            8,
        )
        self.repro = Button(
            700,
            180,
            "repro",
            "Reproducción de las plantas",
            self.botones + "boton-repro.png",
            8,
            None,
            False,
            8,
        )
        self.agri = Button(
            270,
            185,
            "agri",
            "La agricultura en Venezuela",
            self.botones + "boton-agri.png",
            4,
            None,
            False,
            8,
        )
        self.config = Button(
            60,
            445,
            "config",
            "Accesibilidad",
            self.botones + "boton-acc.png",
            3,
            None,
            False,
            1,
        )
        self.orientacion = Button(
            884,
            440,
            "orientacion",
            "Orientaciones y sugerencias",
            self.botones + "boton-or.png",
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
        self.parent.primera_vez = False
        if self.parent.config.texto_cambio == True:
            self.cargar_botones()
            self.cargar_textos()
            self.parent.config.texto_cambio = False

        if self.parent.config.visit["p2"] == False:
            self.parent.config.visit["p2"] = True
            self.show_instructions()
        else:
            self.spserver.processtext(
                "Menú del Recurso", self.parent.config.activar_lector
            )

        self.grupo_banner.add(self.banner_inf)
        self.grupo_botones.add(
            self.plantas,
            self.repro,
            self.agri,
            self.nino,
            self.nina,
            self.config,
            self.orientacion,
        )
        pygame.display.set_caption("Sembrando para el futuro")

    def handleEvents(self, events):
        """
        Evalúa los eventos que se generan en esta pantalla.

        @param events: Lista de los eventos.
        @type events: list
        """
        for event in events:
            self.teclasPulsadas = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                self.parent.quit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                self.show_instructions()

            if event.type == pygame.KEYDOWN and not self.popup_ins.activo:
                self.chequeo_botones(self.grupo_botones)
                self.numero_elementos = len(self.lista_botones)
                self.lista_final = self.lista_botones

                if event.key == pygame.K_RIGHT:
                    self.controlador_lector_evento_K_RIGHT()
                    self.deteccion_movimiento = True

                elif event.key == pygame.K_LEFT:
                    self.controlador_lector_evento_K_LEFT()

                elif self.deteccion_movimiento:
                    if event.key == pygame.K_RETURN:
                        if self.x.tipo_objeto == "boton":

                            if self.x.id == "plantas":
                                self.limpiar_grupos()
                                self.parent.changeState(pantalla3.estado(self.parent))

                            elif self.x.id == "agri":
                                self.limpiar_grupos()
                                self.parent.changeState(pantalla8.estado(self.parent))

                            elif self.x.id == "act1":
                                self.limpiar_grupos()
                                self.parent.pushState(actividad1.estado(self.parent))

                            elif self.x.id == "act2":
                                self.limpiar_grupos()
                                self.parent.pushState(actividad2.actividad(self.parent))

                            elif self.x.id == "repro":
                                self.limpiar_grupos()
                                self.parent.changeState(pantalla5.estado(self.parent))

                            elif self.x.id == "config":
                                self.limpiar_grupos()
                                self.parent.pushState(
                                    menucfg.estado(self.parent, self.previa)
                                )

                            elif self.x.id == "orientacion":
                                self.limpiar_grupos()
                                self.parent.pushState(pantalla11.estado(self.parent))

            if (
                pygame.sprite.spritecollideany(self.raton, self.grupo_botones)
                and not self.popup_ins.activo
            ):
                sprite = pygame.sprite.spritecollide(
                    self.raton, self.grupo_botones, False
                )
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.spserver.stopserver()
                    if sprite[0].id == "orientacion":
                        self.limpiar_grupos()
                        self.parent.pushState(pantalla11.estado(self.parent))
                    elif sprite[0].id == "plantas":
                        self.limpiar_grupos()
                        self.parent.changeState(pantalla3.estado(self.parent))
                    elif sprite[0].id == "repro":
                        self.limpiar_grupos()
                        self.parent.changeState(pantalla5.estado(self.parent))
                    elif sprite[0].id == "agri":
                        self.limpiar_grupos()
                        self.parent.changeState(pantalla8.estado(self.parent))
                    elif sprite[0].id == "config":
                        self.limpiar_grupos()
                        self.parent.pushState(menucfg.estado(self.parent, self.previa))
                    elif sprite[0].id == "act1":
                        self.limpiar_grupos()
                        self.parent.pushState(actividad1.estado(self.parent))
                    elif sprite[0].id == "act2":
                        self.limpiar_grupos()
                        self.parent.pushState(actividad2.actividad(self.parent))
        self.minimag(events)

    def update(self):
        """
        Actualiza la posición del cursor, el magnificador de pantalla en caso de que este activado y los
        tooltip de los botones.
        """
        self.raton.update()
        self.obj_magno.magnificar(self.parent.screen)
        self.grupo_botones.update(self.grupo_tooltip)
