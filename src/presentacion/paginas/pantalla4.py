#!/usr/bin/env python

import pygame

from librerias import pantalla
from librerias.texto import Text
from librerias.image import Image

from paginas import menucfg
from paginas import pantalla2
from paginas import pantalla3
from paginas import pantalla10

animations = [
    "animation-4",
    "animation-4-1",
    "animation-4-2",
    "animation-4-3",
    "animation-4-4",
]

banners = [
    "banner-inf",
    "banner-partes",
]

buttons = [
    "home",
    "volver",
    "config",
    "sig",
]


class estado(pantalla.Pantalla):
    def __init__(self, parent):
        """
        Método inicializador de la clase.

        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        """

        self.name = "screen_4"
        super().__init__(parent, self.name)

        self.load_animations(animations)
        self.load_banners(banners)
        self.load_buttons(buttons)
        self.cargar_textos()

        # Add to the banners group

        self.caja_texto = Image(0, 332, self.backgrounds_path + "caja-texto.png")

        self.grupo_update.add(
            self.animation_4,
            self.animation_4_1,
            self.animation_4_2,
            self.animation_4_3,
            self.animation_4_4,
        )

        self.resume()

    def cargar_textos(self):
        """
        Carga los textos utilizados en esta pantalla.
        """
        self.texto4_2 = Text(
            64,
            340,
            self.parent.text_content["content"][self.name]["text_2"],
            self.parent.config.t_fuente,
            "normal",
            960,
            False,
        )
        self.texto4_3 = Text(
            64,
            340,
            self.parent.text_content["content"][self.name]["text_3"],
            self.parent.config.t_fuente,
            "normal",
            960,
            False,
        )
        self.texto4_4 = Text(
            64,
            340,
            self.parent.text_content["content"][self.name]["text_4"],
            self.parent.config.t_fuente,
            "normal",
            960,
            False,
        )
        self.texto4_5 = Text(
            64,
            340,
            self.parent.text_content["content"][self.name]["text_5"],
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
        self.grupo_banner.add(self.banner_partes, self.banner_inf)
        self.grupo_anim.add(self.animation_4)
        self.grupo_botones.add(self.config, self.volver, self.sig, self.home)
        self.creado = True
        self.final = False
        self.tiempo = 0
        self.animation_4.detener()
        if self.anim_actual == 0:
            self.anim_actual = 1
        self.spserver.processtext(
            "Pantalla: Partes de una planta", self.parent.config.activar_lector
        )
        self.reproducir_animacion(self.anim_actual)

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
                self.lista_final = self.lista_palabra + self.lista_botones
                self.numero_elementos = len(self.lista_final)

                if event.key == pygame.K_RIGHT:
                    self.deteccion_movimiento = True
                    self.controlador_lector_evento_K_RIGHT()

                elif event.key == pygame.K_LEFT:
                    self.controlador_lector_evento_K_LEFT()
                    self.deteccion_movimiento = True

                elif self.deteccion_movimiento:
                    if event.key == pygame.K_RETURN:
                        if self.x.tipo_objeto == "boton":
                            self.deteccion_movimiento = False
                            if self.x.id == "sig":
                                if self.anim_actual <= 7:
                                    self.anim_actual += 1
                                    self.reproducir_animacion(self.anim_actual)

                            elif self.x.id == "volver":
                                self.anim_actual -= 1
                                self.reproducir_animacion(self.anim_actual)
                                if self.anim_actual == 1:
                                    self.grupo_update.update()
                                    self.limpiar_grupos()
                                    self.resume()

                            elif self.x.id == "config":
                                self.limpiar_grupos()
                                self.parent.pushState(
                                    menucfg.estado(self.parent, self.previa)
                                )

                            elif self.x.id == "home":
                                self.limpiar_grupos()
                                self.parent.changeState(pantalla2.estado(self.parent))

                        elif self.x.tipo_objeto == "palabra":
                            self.deteccion_movimiento = False
                            self.spserver.processtext(
                                self.parent.text_content["concepts"][self.x.codigo],
                                self.parent.config.activar_lector,
                            )

            if pygame.sprite.spritecollideany(self.raton, self.grupo_palabras):
                sprite = pygame.sprite.spritecollide(
                    self.raton, self.grupo_palabras, False
                )
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if sprite[0].tipo_objeto == "palabra":
                        if sprite[0].interpretable == True:
                            self.parent.interpretar(sprite[0].codigo)

            if pygame.sprite.spritecollideany(self.raton, self.grupo_botones):
                sprite = pygame.sprite.spritecollide(
                    self.raton, self.grupo_botones, False
                )
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.spserver.stopserver()
                    if sprite[0].id == "home":
                        self.limpiar_grupos()
                        self.parent.changeState(pantalla2.estado(self.parent))
                    elif sprite[0].id == "config":
                        self.limpiar_grupos()
                        self.parent.pushState(menucfg.estado(self.parent, self.previa))
                    elif sprite[0].id == "repe":
                        self.grupo_update.update()
                        self.limpiar_grupos()
                        self.resume()
                    elif sprite[0].id == "sig":
                        self.deteccion_movimiento = False
                        if self.anim_actual <= 7:
                            self.anim_actual += 1
                            self.reproducir_animacion(self.anim_actual)
                    elif sprite[0].id == "volver":
                        self.deteccion_movimiento = False
                        self.anim_actual -= 1
                        self.reproducir_animacion(self.anim_actual)
                        if self.anim_actual == 1:
                            self.grupo_update.update()
                            self.limpiar_grupos()
                            self.resume()
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
                self.grupo_palabras.add(self.texto4_2.img_palabras)
                self.txt_actual = self.texto4_2.img_palabras
                self.chequeo_palabra(self.txt_actual)
                self.animation_4.continuar()

        self.tiempo += self.reloj_anim.get_time()

    def reproducir_animacion(self, animacion):
        """
        Gestiona la reproducción de animaciones, imágenes y texto en esta pantalla.
        @param animacion: Indica la animación que debe reproducirse.
        @type animacion: int
        """
        if animacion <= 0:
            self.limpiar_grupos()
            self.parent.changeState(pantalla3.estado(self.parent))

        if animacion == 1:
            self.elemento_actual = -1
            self.grupo_anim.remove(self.animation_4_1)
            self.grupo_palabras.empty()

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
                self.grupo_palabras.add(self.texto4_2.img_palabras)
                self.txt_actual = self.texto4_2.img_palabras
                self.chequeo_palabra(self.txt_actual)
                self.animation_4.continuar()

        # Anim
        if animacion == 2:
            self.elemento_actual = -1
            self.lista_palabra = []
            self.grupo_palabras.empty()
            self.grupo_fondotexto.empty()
            self.animation_4.detener()
            self.grupo_anim.add(self.animation_4_1)
            self.animation_4_1.update()
            self.animation_4_1.stop = False
            self.animation_4_1.continuar()
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["anim_1"],
                self.parent.config.activar_lector,
            )

        # Explicacion
        if animacion == 3:
            self.elemento_actual = -1
            self.grupo_anim.empty()
            self.grupo_palabras.empty()
            self.grupo_anim.add(self.animation_4)
            self.animation_4.continuar()
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto4_3.img_palabras)
            self.txt_actual = self.texto4_3.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_3"],
                self.parent.config.activar_lector,
            )

        # Anim
        if animacion == 4:
            self.elemento_actual = -1
            self.lista_palabra = []
            self.grupo_palabras.empty()
            self.grupo_fondotexto.empty()
            self.animation_4.detener()
            self.grupo_anim.add(self.animation_4_2)
            self.animation_4_2.update()
            self.animation_4_2.stop = False
            self.animation_4_2.continuar()
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["anim_2"],
                self.parent.config.activar_lector,
            )

        # Explicacion
        if animacion == 5:
            self.elemento_actual = -1
            self.grupo_anim.empty()
            self.grupo_palabras.empty()
            self.grupo_anim.add(self.animation_4)
            self.animation_4.continuar()
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto4_4.img_palabras)
            self.txt_actual = self.texto4_4.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_4"],
                self.parent.config.activar_lector,
            )

        # Anim
        if animacion == 6:
            self.elemento_actual = -1
            self.lista_palabra = []
            self.grupo_palabras.empty()
            self.grupo_fondotexto.empty()
            self.animation_4.detener()
            self.grupo_anim.add(self.animation_4_3)
            self.animation_4_3.update()
            self.animation_4_3.stop = False
            self.animation_4_3.continuar()
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["anim_3"],
                self.parent.config.activar_lector,
            )

        # Explicacion
        if animacion == 7:
            self.elemento_actual = -1
            self.grupo_anim.empty()
            self.grupo_palabras.empty()
            self.grupo_anim.add(self.animation_4)
            self.animation_4.continuar()
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_botones.add(self.sig)
            self.grupo_palabras.add(self.texto4_5.img_palabras)
            self.txt_actual = self.texto4_5.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_5"],
                self.parent.config.activar_lector,
            )

        if animacion == 8:
            self.elemento_actual = -1
            self.lista_palabra = []
            self.grupo_tooltip.empty()
            self.grupo_palabras.empty()
            self.grupo_fondotexto.empty()
            self.animation_4.detener()
            self.grupo_anim.add(self.animation_4_4)
            self.animation_4_4.update()
            self.animation_4_4.stop = False
            self.animation_4_4.continuar()
            self.grupo_botones.remove(self.sig)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["anim_4"],
                self.parent.config.activar_lector,
            )

    def ir_glosario(self):
        self.parent.pushState(pantalla10.estado(self.parent))
