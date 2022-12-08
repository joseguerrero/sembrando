#!/usr/bin/env python

import pygame

from librerias import pantalla
from librerias.texto import Text
from librerias.image import Image

from paginas import menucfg
from paginas import pantalla2
from paginas import pantalla4
from paginas import pantalla10

animations = [
    "animation-3",
]

banners = [
    "banner-inf",
    "banner-plantas",
]

buttons = [
    "home",
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

        self.name = "screen_3"
        super().__init__(parent, self.name)

        # Add to the banners

        self.caja_texto = Image(0, 332, self.backgrounds_path + "caja-texto.png")

        self.load_animations(animations)
        self.load_banners(banners)
        self.load_buttons(buttons)
        self.cargar_textos()

        self.resume()

    def cargar_textos(self):
        """
        Carga los textos utilizados en esta pantalla.
        """
        self.texto3_2 = Text(
            32,
            340,
            self.parent.text_content["content"][self.name]["text_2"],
            self.parent.config.t_fuente,
            "normal",
            992,
            False,
        )

    def resume(self):
        """
        Verifica si se realizaron cambios en la configuración. Carga los valores iniciales de esta pantalla.
        """
        if self.parent.config.texto_cambio == True:
            self.cargar_textos()
            self.load_buttons(buttons)
            self.parent.config.texto_cambio = False
        self.grupo_anim.add(self.animation_3)
        self.grupo_banner.add(self.banner_plantas, self.banner_inf)
        self.grupo_botones.add(self.config, self.sig, self.home)
        self.tiempo = 0
        self.creado = True
        self.final = False
        self.animation_3.detener()
        self.spserver.stopserver()
        self.entrada_primera_vez = True
        self.spserver.processtext(
            "Pantalla: Las Plantas", self.parent.config.activar_lector
        )
        if self.parent.config.activar_lector:
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
                            if self.x.id == "config":
                                self.limpiar_grupos()
                                self.parent.pushState(
                                    menucfg.estado(self.parent, self.previa)
                                )

                            elif self.x.id == "sig":
                                self.ampliar()
                                self.limpiar_grupos()
                                self.parent.changeState(pantalla4.estado(self.parent))

                            elif self.x.id == "home":
                                self.limpiar_grupos()
                                self.parent.changeState(pantalla2.estado(self.parent))

                        elif self.x.tipo_objeto == "palabra":
                            self.spserver.processtext(
                                self.parent.text_content["concepts"][self.x.codigo],
                                self.parent.config.activar_lector,
                            )
                        self.deteccion_movimiento = False

                elif event.key == pygame.K_SPACE:
                    self.spserver.processtext(
                        self.parent.text_content["content"][self.name]["text_2"],
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
                    if sprite[0].id == "sig":
                        self.deteccion_movimiento = False
                        if self.anim_actual <= 3:
                            self.anim_actual += 1
                            self.reproducir_animacion(self.anim_actual)

                    elif sprite[0].id == "config":
                        self.limpiar_grupos()
                        self.parent.pushState(menucfg.estado(self.parent, self.previa))

                    elif sprite[0].id == "home":
                        self.limpiar_grupos()
                        self.parent.changeState(pantalla2.estado(self.parent))
                    elif sprite[0].id == "repe":
                        self.limpiar_grupos()
                        self.resume()
        self.minimag(events)

    def reproducir_animacion(self, animacion):
        """
        Gestiona la reproducción de animaciones, imágenes y texto en esta pantalla.
        @param animacion: Indica la animación que debe reproducirse.
        @type animacion: int
        """
        if animacion == 0:
            self.elemento_actual = -1
            self.animation_3.continuar()
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto3_2.img_palabras)
            self.txt_actual = self.texto3_2.img_palabras
            self.chequeo_palabra(self.txt_actual)

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
                self.animation_3.continuar()
                self.grupo_fondotexto.add(self.caja_texto)
                self.grupo_palabras.add(self.texto3_2.img_palabras)
                self.txt_actual = self.texto3_2.img_palabras
                self.chequeo_palabra(self.txt_actual)

        if animacion == 1:
            self.spserver.stopserver()
            self.elemento_actual = -1
            self.ampliar()
            self.limpiar_grupos()
            self.parent.changeState(pantalla4.estado(self.parent))

        self.chequeo_botones(self.grupo_botones)
        self.lista_final = self.lista_botones + self.lista_palabra
        self.lista_final = self.lista_palabra + self.lista_botones
        self.numero_elementos = len(self.lista_final)

    def update(self):
        """
        Actualiza la posición del cursor, el magnificador de pantalla en caso de que este activado, los
        tooltip de los botones y animaciones o textos correspondientes.
        """
        self.raton.update()
        self.obj_magno.magnificar(self.parent.screen)
        self.grupo_botones.update(self.grupo_tooltip)
        if not self.parent.config.activar_lector:
            if not self.tiempo < 1000:
                self.animation_3.continuar()
                self.grupo_fondotexto.add(self.caja_texto)
                self.grupo_palabras.add(self.texto3_2.img_palabras)
                self.txt_actual = self.texto3_2.img_palabras
                self.chequeo_palabra(self.txt_actual)
        self.tiempo += self.reloj_anim.get_time()

    def draw(self):
        """
        Dibuja el fondo de pantalla y los elementos pertenecientes a los grupos de sprites sobre la superficie
        del manejador de pantallas.
        """
        self.parent.screen.blit(self.background, (0, 0))
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

    def ampliar(self):
        """
        Produce un efecto de acercamiento hacia la esquina inferior derecha de la pantalla.
        """
        rx = self.background.get_width()
        ry = self.background.get_height()
        div = self.mcd(rx, ry)
        px = 0
        py = 0
        vx = 1
        vy = 1
        esc = 1.0 / div
        for _ in range(1, div + 1):
            px -= rx / div
            py -= ry / div
            vx += esc
            vy += esc
            fondo_amp = pygame.transform.smoothscale(
                self.background, (int(rx * vx), int(ry * vy))
            )
            self.parent.screen.blit(fondo_amp, (px, py))
            pygame.time.delay(30)
            pygame.display.update()

    def mcd(self, x, y):
        if y == 0:
            return x
        else:
            return self.mcd(y, x % y)

    def ir_glosario(self):
        self.parent.pushState(pantalla10.estado(self.parent))
