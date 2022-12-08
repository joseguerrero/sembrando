#!/usr/bin/env python

import pygame

from librerias import pantalla
from librerias.texto import Text
from librerias.image import Image

from paginas import pantalla2


banners = [
    "banner-inf",
    "banner-glo",
]

buttons = ["home", "volver"]


class estado(pantalla.Pantalla):
    def __init__(self, parent):
        """
        Método inicializador de la clase.

        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        """

        self.name = "screen_10"
        super().__init__(parent, self.name)

        self.previa = False

        self.caja_concepto = Image(590, 190, self.varios + "caja-concepto.png")

        self.load_banners(banners)
        self.cargar_textos()
        self.load_buttons(buttons)

        inicial = self.parent.config.definicion[0].upper()
        self.abc.indexar(inicial)
        self.grupo_palabras.add(
            self.abc.img_palabras,
            self.indices(inicial, self.parent.config.definicion),
            self.mostrar_concepto(self.parent.config.definicion),
        )
        self.caja_concepto.resize(height=self.concepto.ancho_final)
        self.grupo_palabras.add(self.abc.img_palabras)
        self.grupo_banner.add(self.banner_glo, self.caja_concepto, self.banner_inf)
        self.grupo_botones.add(self.volver, self.home)

    def cargar_textos(self):
        """
        Carga los textos utilizados en esta pantalla.
        """
        self.abc = Text(
            290,
            140,
            "A  B  C  D  E  F  G  H  I  J  K  L  M  N  Ñ  O  P  Q  R  S  T  U  V  W  X  Y  Z ",
            18,
            "indice",
            1010,
        )
        self.concepto = Text(
            600, 200, "", self.parent.config.t_fuente, "concepto", 1000
        )
        self.a_absorber = Text(330, 200, "Absorber ", 22, "definicion", 900)
        self.c_celula = Text(330, 200, "Célula ", 22, "definicion", 900)
        self.c_componentes = Text(330, 250, "Componentes ", 22, "definicion", 900)
        self.f_fotosintesis = Text(330, 200, "Fotosíntesis ", 22, "definicion", 900)
        self.g_germinacion = Text(330, 200, "Germinación ", 22, "definicion", 900)
        self.g_germinar = Text(330, 250, "Germinar ", 22, "definicion", 900)
        self.m_minerales = Text(330, 200, "Mineral ", 22, "definicion", 900)
        self.n_nutrientes = Text(330, 200, "Nutriente ", 22, "definicion", 900)
        self.o_organo = Text(330, 200, "Órgano ", 22, "definicion", 900)
        self.a_asexual = Text(330, 200, "Reproducción asexual ", 22, "definicion", 900)
        self.s_sexual = Text(330, 250, "Reproducción sexual ", 22, "definicion", 900)
        self.t_transformacion = Text(330, 200, "Transformación ", 22, "definicion", 900)
        self.t_transporte = Text(330, 250, "Transportar ", 22, "definicion", 900)

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
                if event.key == pygame.K_ESCAPE:
                    self.limpiar_grupos()
                    self.parent.changeState(pantalla2.estado(self.parent))

            if pygame.sprite.spritecollideany(self.raton, self.grupo_palabras):
                sprite = pygame.sprite.spritecollide(
                    self.raton, self.grupo_palabras, False
                )
                if pygame.mouse.get_pressed() == (True, False, False):
                    if sprite[0].definible == True:
                        self.abc.indexar(sprite[0].palabra)
                        self.grupo_palabras.update(1)
                        sprite[0].selec = True
                        sprite[0].destacar()
                        self.grupo_palabras.empty()
                        self.grupo_banner.remove(self.caja_concepto)
                        self.grupo_palabras.add(
                            self.abc.img_palabras, self.indices(sprite[0].palabra)
                        )
                    if sprite[0].definicion == True:
                        self.grupo_palabras.update(2)
                        sprite[0].selec = True
                        sprite[0].negrita()
                        self.grupo_banner.add(self.caja_concepto)
                        self.grupo_palabras.remove(self.concepto.img_palabras)
                        self.grupo_palabras.add(self.mostrar_concepto(sprite[0].codigo))
                        self.caja_concepto.resize(height=self.concepto.ancho_final)

            if pygame.sprite.spritecollideany(self.raton, self.grupo_botones):
                sprite = pygame.sprite.spritecollide(
                    self.raton, self.grupo_botones, False
                )
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if sprite[0].id == "home":
                        self.limpiar_grupos()
                        self.parent.changeState(pantalla2.estado(self.parent))
                    elif sprite[0].id == "volver":
                        self.limpiar_grupos()
                        self.parent.popState()
        self.minimag(events)

    def update(self):
        """
        Actualiza la posición del cursor, el magnificador de pantalla en caso de que este activado y los
        tooltip de los botones.
        """
        self.raton.update()
        self.obj_magno.magnificar(self.parent.screen)
        self.grupo_botones.update(self.grupo_tooltip)

    def mostrar_concepto(self, palabra):
        """
        Define el concepto que se mostrara en pantalla cuando cargue esta pantalla.
        @return: Texto que conforma el concepto correspondiente.
        @rtype: list
        """

        self.concepto = Text(
            600,
            200,
            self.parent.text_content["concepts"][palabra],
            self.parent.config.t_fuente,
            "concepto",
            1000,
        )
        return self.concepto.img_palabras

    def indices(self, valor, palabra_negrita=""):
        """
        Determina las definiciones que se muestran cuando cargue esta pantalla.
        @return: Lista de las definiciones correspondientes.
        @rtype: list
        """
        indices = {
            "A": (self.a_absorber,),
            "C": (self.c_celula, self.c_componentes),
            "F": (self.f_fotosintesis,),
            "G": (self.g_germinacion, self.g_germinar),
            "M": (self.m_minerales,),
            "N": (self.n_nutrientes,),
            "O": (self.o_organo,),
            "R": (self.a_asexual, self.s_sexual),
            "T": (self.t_transformacion, self.t_transporte),
        }
        palabras = []
        if valor in indices:
            tupla = indices[valor]
            for i in tupla:
                if i.img_palabras[0].codigo == palabra_negrita:
                    i.img_palabras[0].selec = True
                    i.img_palabras[0].negrita()
                else:
                    i.img_palabras[0].selec = False
                    i.img_palabras[0].update(2)
                palabras.append(i.img_palabras)
            return palabras
