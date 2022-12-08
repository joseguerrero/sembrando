#!/usr/bin/env python

import pygame

from librerias import pantalla
from librerias.texto import Text
from librerias.image import Image

from paginas import menucfg
from paginas import pantalla2
from paginas import pantalla6
from paginas import pantalla10

animations = [
    "animation-5",
    "animation-5-0",
    "animation-5-1",
    "animation-5-2",
    "animation-5-3",
]

banners = [
    "banner-inf",
    "banner-repro",
]

buttons = [
    "home",
    "sig",
    "config",
    "volver",
]


class estado(pantalla.Pantalla):
    def __init__(self, parent, anim_actual=0):
        """
        Método inicializador de la clase.

        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        @param anim_actual: Código de la ultima animación mostrada en esta pantalla.
        @type anim_actual: int
        """

        self.name = "screen_5"
        super().__init__(parent, self.name)

        # Animations

        self.anim_actual = anim_actual

        self.load_animations(animations)
        self.load_banners(banners)
        self.load_buttons(buttons)
        self.cargar_textos()

        # Banners
        self.caja_texto = Image(0, 332, self.backgrounds_path + "caja-texto.png")

        self.grupo_update.add(
            self.animation_5, self.animation_5_0, self.animation_5_1, self.animation_5_2
        )

        self.resume()

    def cargar_textos(self):
        """
        Carga los textos utilizados en esta pantalla.
        """
        self.texto5_2 = Text(
            64,
            340,
            self.parent.text_content["content"][self.name]["text_2"],
            self.parent.config.t_fuente,
            "normal",
            960,
            False,
        )
        self.texto5_3 = Text(
            64,
            340,
            self.parent.text_content["content"][self.name]["text_3"],
            self.parent.config.t_fuente,
            "normal",
            960,
            False,
        )
        self.texto5_4 = Text(
            64,
            340,
            self.parent.text_content["content"][self.name]["text_4"],
            self.parent.config.t_fuente,
            "normal",
            960,
            False,
        )
        self.texto5_5 = Text(
            64,
            340,
            self.parent.text_content["content"][self.name]["text_5"],
            self.parent.config.t_fuente,
            "normal",
            960,
            False,
        )
        self.texto5_6 = Text(
            64,
            340,
            self.parent.text_content["content"][self.name]["text_6"],
            self.parent.config.t_fuente,
            "normal",
            960,
            False,
        )

    def resume(self):
        """
        Verifica si se realizaron cambios en la configuración. Carga los valores iniciales de esta pantalla.
        """
        if self.parent.config.texto_cambio == True:
            self.load_buttons(buttons)
            self.cargar_textos()
            self.parent.config.texto_cambio = False
        self.grupo_anim.add(self.animation_5)
        self.grupo_imagen.add(self.animation_5_3)
        self.grupo_banner.add(self.banner_repro, self.banner_inf)
        self.grupo_botones.add(self.config, self.sig, self.volver, self.home)
        self.animation_5.detener()
        self.animation_5_3.detener()
        self.creado = True
        self.final = False
        self.tiempo = 0
        if self.anim_actual == 0:
            self.anim_actual = 1
        self.spserver.processtext(
            "Pantalla: Reproducción de las plantas.", self.parent.config.activar_lector
        )
        self.reproducir_animacion(self.anim_actual)
        self.entrada_primera_vez = True

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
                if event.key == pygame.K_RIGHT:
                    self.deteccion_movimiento = True
                    self.controlador_lector_evento_K_RIGHT()

                elif event.key == pygame.K_LEFT:
                    self.controlador_lector_evento_K_LEFT()

                elif self.deteccion_movimiento:
                    if event.key == pygame.K_RETURN:
                        if self.x.tipo_objeto == "boton":
                            if self.x.id == "sig":
                                if self.anim_actual <= 11:
                                    self.anim_actual += 1
                                    self.reproducir_animacion(self.anim_actual)
                                self.deteccion_movimiento = False

                            elif self.x.id == "volver":
                                self.anim_actual -= 1
                                self.reproducir_animacion(self.anim_actual)
                                if self.anim_actual == 1:
                                    self.grupo_update.update()
                                    self.limpiar_grupos()
                                    self.resume()
                                self.deteccion_movimiento = False

                            elif self.x.id == "config":
                                self.limpiar_grupos()
                                self.parent.pushState(
                                    menucfg.estado(self.parent, self.previa)
                                )
                                self.deteccion_movimiento = False

                            elif self.x.id == "home":
                                self.limpiar_grupos()
                                self.parent.changeState(pantalla2.estado(self.parent))
                                self.deteccion_movimiento = False

                        elif self.x.tipo_objeto == "palabra":
                            self.spserver.processtext(
                                self.parent.text_content["concepts"][self.x.codigo],
                                self.parent.config.activar_lector,
                            )

            if pygame.sprite.spritecollideany(self.raton, self.grupo_palabras):
                sprite = pygame.sprite.spritecollide(
                    self.raton, self.grupo_palabras, False
                )
                if pygame.mouse.get_pressed() == (True, False, False):
                    if sprite[0].tipo_objeto == "palabra":
                        if sprite[0].interpretable == True:
                            self.parent.interpretar(sprite[0].codigo)

            if pygame.sprite.spritecollideany(self.raton, self.grupo_botones):
                sprite = pygame.sprite.spritecollide(
                    self.raton, self.grupo_botones, False
                )
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if sprite[0].id == "home":
                        self.limpiar_grupos()
                        self.parent.changeState(pantalla2.estado(self.parent))

                    elif sprite[0].id == "sig":
                        self.deteccion_movimiento = False
                        if self.anim_actual <= 11:
                            self.anim_actual += 1
                            self.reproducir_animacion(self.anim_actual)

                    elif sprite[0].id == "volver":
                        self.deteccion_movimiento = False
                        self.anim_actual -= 1
                        self.reproducir_animacion(self.anim_actual)

                    elif sprite[0].id == "config":
                        self.limpiar_grupos()
                        self.parent.pushState(menucfg.estado(self.parent, self.previa))
        self.minimag(events)

    def update(self):
        """
        Actualiza la posición del cursor, el magnificador de pantalla en caso de que este activado, los
        tooltip de los botones y animaciones o textos correspondientes.
        """
        self.raton.update()
        self.obj_magno.magnificar(self.parent.screen)
        self.grupo_botones.update(self.grupo_tooltip)
        if self.anim_actual == 1 and not self.parent.config.activar_lector:
            if not self.tiempo < 1000:
                self.grupo_fondotexto.add(self.caja_texto)
                self.grupo_palabras.add(self.texto5_2.img_palabras)
                self.txt_actual = self.texto5_2.img_palabras
                self.chequeo_palabra(self.txt_actual)
                self.animation_5.continuar()
        self.tiempo += self.reloj_anim.get_time()

    def reproducir_animacion(self, animacion):
        """
        Gestiona la reproducción de animaciones, imágenes y texto en esta pantalla.
        @param animacion: Indica la animación que debe reproducirse.
        @type animacion: int
        """
        if animacion == 1:
            self.elemento_actual = -1
            self.lista_palabra = []
            self.grupo_tooltip.empty()
            self.grupo_botones.remove(self.volver)
            if self.parent.config.activar_lector:
                if self.entrada_primera_vez:
                    self.spserver.processtext2(
                        self.parent.text_content["content"][self.name]["text_2"],
                        self.parent.config.activar_lector,
                    )
                    self.entrada_primera_vez = False
                else:
                    self.spserver.processtext(
                        self.parent.text_content["content"][self.name]["text_2"],
                        self.parent.config.activar_lector,
                    )
                self.grupo_fondotexto.add(self.caja_texto)
                self.grupo_palabras.add(self.texto5_2.img_palabras)
                self.txt_actual = self.texto5_2.img_palabras
                self.chequeo_palabra(self.txt_actual)
                self.animation_5.continuar()

        # Mostrar crecimiento animation_5_3
        elif animacion == 2:
            self.entrada_primera_vez = False
            self.elemento_actual = -1
            self.lista_palabra = []
            self.grupo_botones.empty()
            self.grupo_botones.add(self.config, self.volver, self.sig, self.home)
            self.grupo_palabras.empty()
            self.grupo_fondotexto.empty()
            self.animation_5.detener()
            self.animation_5_3.update()
            self.animation_5_3.stop = False
            self.animation_5_3.continuar()
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["anim_1"],
                self.parent.config.activar_lector,
            )

        # Mostrar texto 3
        elif animacion == 3:
            self.elemento_actual = -1
            self.grupo_anim.remove(self.animation_5_0)
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto5_3.img_palabras)
            self.txt_actual = self.texto5_3.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_3"],
                self.parent.config.activar_lector,
            )
            self.animation_5.continuar()

        # Mostrar acercamiento a la animacion 5-0
        elif animacion == 4:
            self.elemento_actual = -1
            self.lista_palabra = []
            self.grupo_palabras.empty()
            self.grupo_fondotexto.empty()
            self.animation_5.detener()
            self.grupo_anim.add(self.animation_5_0)
            self.animation_5_0.update()
            self.animation_5_0.stop = False
            self.animation_5_0.continuar()
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["anim_2"],
                self.parent.config.activar_lector,
            )

        # Texto 4
        elif animacion == 5:
            self.elemento_actual = -1
            self.grupo_anim.remove(self.animation_5_1)
            self.grupo_anim.remove(self.animation_5_0)
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto5_4.img_palabras)
            self.txt_actual = self.texto5_4.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_4"],
                self.parent.config.activar_lector,
            )
            self.animation_5.continuar()

        # Mostrar acercamiento a la animacion 5-1
        elif animacion == 6:
            self.elemento_actual = -1
            self.lista_palabra = []
            self.grupo_palabras.empty()
            self.grupo_fondotexto.empty()
            self.animation_5_1.update()
            self.animation_5_1.stop = False
            self.animation_5.detener()
            self.grupo_anim.add(self.animation_5_1)
            self.animation_5_1.continuar()
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["anim_3"],
                self.parent.config.activar_lector,
            )

        # Texto 5
        elif animacion == 7:
            self.elemento_actual = -1
            self.grupo_anim.remove(self.animation_5_2)
            self.grupo_anim.remove(self.animation_5_1)
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto5_5.img_palabras)
            self.txt_actual = self.texto5_5.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_5"],
                self.parent.config.activar_lector,
            )
            self.animation_5.continuar()

        # Mostrar acercamiento a la animacion 5-2
        elif animacion == 8:
            self.elemento_actual = -1
            self.lista_palabra = []
            self.grupo_palabras.empty()
            self.grupo_fondotexto.empty()
            self.animation_5.detener()
            self.grupo_anim.add(self.animation_5_2)
            self.animation_5_2.update()
            self.animation_5_2.stop = False
            self.animation_5_2.continuar()
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["anim_4"],
                self.parent.config.activar_lector,
            )

        # Texto 6
        elif animacion == 9:
            self.elemento_actual = -1
            self.grupo_botones.add(self.volver)
            self.grupo_anim.remove(self.animation_5_2)
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto5_6.img_palabras)
            self.txt_actual = self.texto5_6.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_6"],
                self.parent.config.activar_lector,
            )
            self.animation_5.continuar()

        elif animacion == 10:
            self.elemento_actual = -1
            self.lista_palabra = []
            self.limpiar_grupos()
            self.parent.changeState(pantalla6.estado(self.parent))

        self.chequeo_botones(self.grupo_botones)
        self.lista_final = self.lista_palabra + self.lista_botones
        self.numero_elementos = len(self.lista_final)

    def ir_glosario(self):
        self.parent.pushState(pantalla10.estado(self.parent))
