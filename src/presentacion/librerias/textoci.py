#!/usr/bin/env python

from .palabra import palabra


class texto2:
    def __init__(self, posx, posy, texto, size, tipo_texto, limite_der, dic=0):
        """
        Similar a la clase texto, con la diferencia que este metodo acepta imagenes para ser
        intercaladas en el texto. Los parametros son iguales a la clase texto, exceptuando al parametro dic.
        Esta clase tiene ciertos defectos a la hora de justificar con imagenes en los bordes.
        @param dic: representa un diccionario de la estructura (X:Z) en donde X (tipo string)
        es la palabra del texto a sustituir por la imagen, y Z representa a la imagen (tipo pygame.Surface)
        que sera usada en la posicion de la palabra.
        @type dic: dict
        """
        self.posx = posx
        self.posy = posy
        self.x = posx
        self.y = posy
        self.tipo_texto = tipo_texto
        self.img_palabras = []
        self.texto = texto
        self.buffer = ""
        self.espacio = 6
        self.nro_linea = 0
        self.ancho_final = 0
        self.dic = dic

        for i in self.texto:
            self.buffer += i
            if i == " ":
                if (
                    self.buffer == "Reproducción " and self.tipo_texto != "texto_act"
                ) or (
                    self.buffer == "reproducción " and self.tipo_texto != "texto_act"
                ):
                    pass
                else:
                    self.img_palabras.append(
                        palabra(self.buffer.strip(" "), size, self.tipo_texto)
                    )
                    self.buffer = ""

        self.limite_izq = posx
        self.limite_der = limite_der
        #        medidas, ancho, alto_lineas = self.calcular(self.posx)
        medidas, ancho, alto_lineas = self.calcular2(self.posx)
        self.ancho_final = ancho
        self.espacio = 6 + medidas[self.nro_linea]

        for i in self.img_palabras:
            if (self.posx + i.rect.width > self.limite_der) or (i.palabra == "|"):
                self.nro_linea += 1
                self.espacio = 6 + medidas[self.nro_linea]
                self.posx = self.limite_izq
                #                posy += alto_lineas[self.nro_linea-1]
                posy += alto_lineas
            i.rect.left = self.posx
            #            i.rect.y = posy + alto_lineas[self.nro_linea]/2 - i.rect.h/2
            i.rect.y = posy + alto_lineas / 2 - i.rect.h / 2

            if not self.dic == 0:
                for n in self.dic.keys():
                    if n == i.palabra:
                        i.image = self.dic[n]
                        i.rect.width, i.rect.height = i.image.get_size()
                        i.rect.x = self.posx
                        i.rect.y = posy
            self.posx += i.rect.width + self.espacio

    def calcular(self, posx):
        """
        Calcula la altura de las líneas y la cantidad de lineas que tiene el texto.

        @return: Un conjunto de valores que comprende: la medida de las lineas, el ancho total y el alto
        de cada linea del texto.
        @rtype: tuple
        """
        px = self.posx
        nro_lineas = 0
        medida_lineas = []
        ppl = 0
        ancho = 0
        ancho_total = 0
        altos_lineas = []
        for i in self.img_palabras:
            if (px + i.rect.width > self.limite_der) or (i.palabra == "|"):
                if ppl == 1:
                    medida_lineas.append((self.limite_der - px) / ppl)
                else:
                    medida_lineas.append((self.limite_der - px) / (ppl - 1.0))
                ppl = 0
                px = self.limite_izq
                nro_lineas += 1
                altos_lineas.append(ancho)
                ancho = 0
            if not self.dic == 0:
                for n in self.dic.keys():
                    if n == i.palabra:
                        i.image = self.dic[n]
                        i.rect = i.image.get_rect()

            px += i.rect.width + self.espacio
            if i.rect.h > ancho:
                ancho = i.rect.height
            ppl += 1
        medida_lineas.append(0)
        altos_lineas.append(ancho)
        for i in altos_lineas:
            ancho_total += i
        return medida_lineas, ancho_total, altos_lineas

    def calcular2(self, posx):
        """
        Calcula la altura de las líneas y la cantidad de lineas que tiene el texto.

        @return: Un conjunto de valores que comprende: la medida de las lineas, el ancho total y el alto
        de cada linea del texto.
        @rtype: tuple
        """
        px = self.posx
        nro_lineas = 0
        medida_lineas = []
        ppl = 0
        alto = 0
        ancho = 0
        ancho_total = 0
        altos_lineas = []
        for i in self.img_palabras:
            if not self.dic == 0:
                for n in self.dic.keys():
                    if n == i.palabra:
                        i.image = self.dic[n]
                        i.rect = i.image.get_rect()

            if px + i.rect.width > self.limite_der:
                if ppl == 1:
                    medida_lineas.append((self.limite_der - px) / ppl)
                else:
                    medida_lineas.append((self.limite_der - px) / (ppl - 1.0))
                ppl = 0
                px = self.limite_izq
                nro_lineas += 1
                altos_lineas.append(ancho)
                ancho = 0

            #            if not self.dic == 0 :
            #                for n in self.dic.keys():
            #                    if n == i.palabra:
            #                        i.image = self.dic[n]
            #                        i.rect = i.image.get_rect()

            px += i.rect.width + self.espacio
            if i.rect.h > ancho:
                ancho = i.rect.height
            ppl += 1

        medida_lineas.append(0)
        altos_lineas.append(ancho)
        for i in altos_lineas:
            if i > alto:
                alto = i
        ancho_total = alto * (nro_lineas + 1)
        return medida_lineas, ancho_total, alto
