#!/usr/bin/env python

import pygame

from librerias import pantalla
from librerias.button import Button
from librerias.texto import texto
from librerias.image import Image


class estado(pantalla.Pantalla):
    def __init__(self, parent):
        """
        Método inicializador de la clase.

        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        """

        self.name = "screen_11"
        self.parent = parent
        self.background = pygame.image.load(self.fondos + "fondo-acc.png").convert()
        self.caja_or = Image(290, 125, self.fondos + "caja.png")
        self.banner_inf = Image(0, 432, self.banners + "banner-inf.png")
        self.banner_or = Image(0, 0, self.banners + "banner-or.png")
        self.banner_or_es = Image(0, 0, self.banners + "banner-or-es.png")
        self.banner_or_pa = Image(0, 0, self.banners + "banner-or-pa.png")
        self.banner_or_doc = Image(0, 0, self.banners + "banner-or-doc.png")
        self.cargar_botones()
        self.cargar_textos()
        self.grupo_palabras.add(self.texto11.img_palabras)
        self.grupo_banner.add(self.banner_or, self.banner_inf)
        self.grupo_botones.add(
            self.boton_or_ninos,
            self.boton_or_docentes,
            self.boton_or_padres,
            self.puerta,
        )

    def cargar_textos(self):
        """
        Carga los textos utilizados en esta pantalla.
        """
        self.spserver.processtext(
            "Pantalla: Orientaciones y Sugerencias: "
            "Pulsa sobre cada botón para que puedas explorar las orientaciones y sugerencias. ",
            self.parent.config.activar_lector,
        )
        self.texto11 = texto(
            400,
            200,
            self.parent.text_content["content"][self.name]["text_1"],
            self.parent.config.t_fuente,
            "instruccion",
            800,
        )
        self.texto11_5_1 = texto(
            300,
            130,
            self.parent.text_content["content"][self.name]["text_5_1"],
            self.parent.config.t_fuente,
            "normal",
            900,
        )
        self.texto11_5_2 = texto(
            300,
            self.texto11_5_1.y + self.texto11_5_1.ancho_final + 10,
            self.parent.text_content["content"][self.name]["text_5_2"],
            self.parent.config.t_fuente,
            "normal",
            900,
        )
        self.texto11_5_3 = texto(
            300,
            self.texto11_5_2.y + self.texto11_5_2.ancho_final + 10,
            self.parent.text_content["content"][self.name]["text_5_3"],
            self.parent.config.t_fuente,
            "normal",
            900,
        )
        self.texto11_6_1 = texto(
            300,
            130,
            self.parent.text_content["content"][self.name]["text_6_1"],
            self.parent.config.t_fuente,
            "normal",
            900,
        )
        self.texto11_6_2 = texto(
            300,
            self.texto11_6_1.y + self.texto11_6_1.ancho_final + 10,
            self.parent.text_content["content"][self.name]["text_6_2"],
            self.parent.config.t_fuente,
            "normal",
            900,
        )
        self.texto11_6_3 = texto(
            300,
            self.texto11_6_2.y + self.texto11_6_2.ancho_final + 10,
            self.parent.text_content["content"][self.name]["text_6_3"],
            self.parent.config.t_fuente,
            "normal",
            900,
        )
        self.texto11_7_1 = texto(
            300,
            130,
            self.parent.text_content["content"][self.name]["text_7_1"],
            self.parent.config.t_fuente,
            "normal",
            900,
        )
        self.texto11_7_2 = texto(
            300,
            self.texto11_7_1.y + self.texto11_7_1.ancho_final + 10,
            self.parent.text_content["content"][self.name]["text_7_2"],
            self.parent.config.t_fuente,
            "normal",
            900,
        )
        self.texto11_7_3 = texto(
            300,
            self.texto11_7_2.y + self.texto11_7_2.ancho_final + 10,
            self.parent.text_content["content"][self.name]["text_7_3"],
            self.parent.config.t_fuente,
            "normal",
            900,
        )

    def cargar_botones(self):
        """
        Carga los botones utilizados en esta pantalla.
        """
        self.boton_or_ninos = Button(
            300,
            440,
            "or-ninos",
            "Orientaciones a la niña, niño y adolescente",
            self.botones + "boton-or-es.png",
            3,
            None,
            False,
            1,
        )
        self.boton_or_docentes = Button(
            500,
            440,
            "or-docentes",
            "Sugerencias pedagógicas",
            self.botones + "boton-or-doc.png",
            3,
            None,
            False,
            1,
        )
        self.boton_or_padres = Button(
            700,
            440,
            "or-padres",
            "Orientaciones a la adulta y al adulto responsable",
            self.botones + "boton-or-pa.png",
            3,
            None,
            False,
            1,
        )
        self.puerta = Button(
            60,
            425,
            "puerta",
            "Regresar",
            self.botones + "boton-puerta.png",
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
        pass

    def handleEvents(self, events):
        """
        Evalúa los eventos que se generan en esta pantalla.

        @param events: Lista de los eventos.
        @type events: list
        """
        for event in events:
            if event.type == pygame.QUIT:
                self.parent.quit()

            if event.type == pygame.KEYDOWN:

                self.chequeo_botones(self.grupo_botones)
                self.lista_final = self.lista_botones
                self.numero_elementos = len(self.lista_final)

                if event.key == pygame.K_ESCAPE:
                    self.limpiar_grupos()
                    self.parent.popState()
                elif event.key == pygame.K_LEFT:
                    self.controlador_lector_evento_K_LEFT()

                elif event.key == pygame.K_RIGHT:
                    self.controlador_lector_evento_K_RIGHT()

                elif event.key == pygame.K_RETURN:
                    self.elemento_actual = -1
                    if self.x.tipo_objeto == "boton":
                        if self.x.id == "or-ninos":
                            self.grupo_palabras.empty()
                            self.grupo_banner.empty()
                            self.grupo_palabras.add(
                                self.texto11_5_1.img_palabras,
                                self.texto11_5_2.img_palabras,
                                self.texto11_5_3.img_palabras,
                            )
                            self.caja_or.resize(
                                height=self.texto11_5_1.ancho_final
                                + self.texto11_5_2.ancho_final
                                + self.texto11_5_3.ancho_final
                                + 30
                            )
                            self.grupo_banner.add(
                                self.banner_or_es, self.caja_or, self.banner_inf
                            )
                            self.spserver.processtext(
                                self.parent.text_content["content"][self.name][
                                    "text_5_1l"
                                ]
                                + self.parent.text_content["content"][self.name][
                                    "text_5_2l"
                                ]
                                + self.parent.text_content["content"][self.name][
                                    "text_5_3l"
                                ]
                                + "Ahora, utiliza las teclas de dirección y explora la siguiente orientación o sugerencia. ",
                                self.parent.config.activar_lector,
                            )

                        elif self.x.id == "or-docentes":
                            self.grupo_palabras.empty()
                            self.grupo_banner.empty()
                            self.grupo_palabras.add(
                                self.texto11_6_1.img_palabras,
                                self.texto11_6_2.img_palabras,
                                self.texto11_6_3.img_palabras,
                            )
                            self.caja_or.resize(
                                height=self.texto11_6_1.ancho_final
                                + self.texto11_6_2.ancho_final
                                + self.texto11_6_3.ancho_final
                                + 30
                            )
                            self.grupo_banner.add(
                                self.banner_or_doc, self.caja_or, self.banner_inf
                            )

                            self.spserver.processtext(
                                self.parent.text_content["content"][self.name][
                                    "text_6_1l"
                                ]
                                + self.parent.text_content["content"][self.name][
                                    "text_6_2l"
                                ]
                                + self.parent.text_content["content"][self.name][
                                    "text_6_3l"
                                ]
                                + "Ahora, utiliza las teclas de dirección y explora la siguiente orientación o sugerencia. ",
                                self.parent.config.activar_lector,
                            )

                        elif self.x.id == "or-padres":
                            self.grupo_palabras.empty()
                            self.grupo_banner.empty()
                            self.grupo_palabras.add(
                                self.texto11_7_1.img_palabras,
                                self.texto11_7_2.img_palabras,
                                self.texto11_7_3.img_palabras,
                            )
                            self.caja_or.resize(
                                height=self.texto11_7_1.ancho_final
                                + self.texto11_7_2.ancho_final
                                + self.texto11_7_3.ancho_final
                                + 30
                            )
                            self.grupo_banner.add(
                                self.banner_or_pa, self.caja_or, self.banner_inf
                            )

                            self.spserver.processtext(
                                self.parent.text_content["content"][self.name][
                                    "text_7_1l"
                                ]
                                + self.parent.text_content["content"][self.name][
                                    "text_7_2l"
                                ]
                                + self.parent.text_content["content"][self.name][
                                    "text_7_3l"
                                ]
                                + "Fin de contenido, regresa al menú. ",
                                self.parent.config.activar_lector,
                            )

                        elif self.x.id == "puerta":
                            self.limpiar_grupos()
                            self.parent.popState()

            if pygame.sprite.spritecollideany(self.raton, self.grupo_botones):
                sprite = pygame.sprite.spritecollide(
                    self.raton, self.grupo_botones, False
                )
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if sprite[0].id == "puerta":
                        self.limpiar_grupos()
                        self.parent.popState()

                    elif sprite[0].id == "or-ninos":
                        self.grupo_palabras.empty()
                        self.grupo_banner.empty()
                        self.grupo_palabras.add(
                            self.texto11_5_1.img_palabras,
                            self.texto11_5_2.img_palabras,
                            self.texto11_5_3.img_palabras,
                        )
                        self.caja_or.resize(
                            height=self.texto11_5_1.ancho_final
                            + self.texto11_5_2.ancho_final
                            + self.texto11_5_3.ancho_final
                            + 30
                        )
                        self.grupo_banner.add(
                            self.banner_or_es, self.caja_or, self.banner_inf
                        )

                    elif sprite[0].id == "or-docentes":
                        self.grupo_palabras.empty()
                        self.grupo_banner.empty()
                        self.grupo_palabras.add(
                            self.texto11_6_1.img_palabras,
                            self.texto11_6_2.img_palabras,
                            self.texto11_6_3.img_palabras,
                        )
                        self.caja_or.resize(
                            height=self.texto11_6_1.ancho_final
                            + self.texto11_6_2.ancho_final
                            + self.texto11_6_3.ancho_final
                            + 30
                        )
                        self.grupo_banner.add(
                            self.banner_or_doc, self.caja_or, self.banner_inf
                        )

                    elif sprite[0].id == "or-padres":
                        self.grupo_palabras.empty()
                        self.grupo_banner.empty()
                        self.grupo_palabras.add(
                            self.texto11_7_1.img_palabras,
                            self.texto11_7_2.img_palabras,
                            self.texto11_7_3.img_palabras,
                        )
                        self.caja_or.resize(
                            height=self.texto11_7_1.ancho_final
                            + self.texto11_7_2.ancho_final
                            + self.texto11_7_3.ancho_final
                            + 30
                        )
                        self.grupo_banner.add(
                            self.banner_or_pa, self.caja_or, self.banner_inf
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
