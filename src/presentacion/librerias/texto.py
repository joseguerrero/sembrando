#!/usr/bin/env python

import pygame
from .palabra import palabra

class texto():
    """
    Esta clase hace uso de la clase palabras para formar textos y dibujarlos correctamente en la pantalla.
    Los textos generados son justificados automáticamente y sus margenes pueden personalizarse.
    """
    def __init__(self, posx, posy, texto, size, tipo_texto, limite_der, personalizado = True):
        """
        Inicializa el el objeto, define los valores por defecto, calcula la justificación y los margenes
        correspondientes.
        
        @param posx: Coordenada X donde se desea dibujar el texto.
        @type posx: int
        @param posy: Coordenada Y donde se desea dibujar el texto.
        @type posy: int
        @param texto: Texto que se desea imprimir.
        @type texto: str
        @param size: Tamaño del texto que se desea imprimir. Debe estar entre 18 y 22.
        @type size: int
        @param tipo_texto: Clasificación del texto de acuerdo a la función que desempeña.
        @type tipo_texto: str
        @param limite_der: Indica el margen derecho desde donde se comienza a dibujar el texto.
        @type limite_der: int
        @param personalizado: Si es True, los margenes son ajustados manualmente. Si es False, 
        los margenes son ajustados automáticamente según el tipo de texto y la posición.
        @type personalizado: bool
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
        
        for i in self.texto:
            self.buffer += i
            if i == " ":
                if (self.buffer == u"Reproducción " and self.tipo_texto != "texto_act")  or (self.buffer == u"reproducción " and self.tipo_texto != "texto_act"):
                    pass
                else:
                    self.img_palabras.append(palabra(self.buffer.strip(" "), size, self.tipo_texto))
                    self.buffer = ""

        n_lineas = self.calcular_margenes()
        
        if personalizado == True:
            self.limite_izq = posx
            self.limite_der = limite_der
            medidas, ancho, lineas = self.calcular(self.posx, posy)
            self.ancho_final = ancho * lineas
            self.espacio = 6 + medidas[self.nro_linea]
            for i in self.img_palabras:
                if self.posx + i.rect.width > self.limite_der:
                    self.nro_linea += 1
                    self.espacio = 6 + medidas[self.nro_linea]
                    self.posx = self.limite_izq
                    posy += i.rect.height
                i.rect.left = self.posx
                i.rect.top = posy
                self.posx += i.rect.width + self.espacio
                
            width = 0
            for i in self.img_palabras:
                width += i.image.get_width()
            self.rect = pygame.Rect(self.x, self.y, width, self.ancho_final)
                
        elif personalizado == False:
            
            if self.tipo_texto == "instruccion":
                self.limite_izq, self.limite_der = (self.x, limite_der)
                self.posx = self.x + 32
            
            elif n_lineas == 1:
                self.limite_izq, self.limite_der = (256, 768)
                self.posx = 256
            
            elif n_lineas ==  2:
                self.limite_izq, self.limite_der = (192, 832)
                self.posx = 224
            
            elif n_lineas >= 3:
                self.limite_izq, self.limite_der = (32, 992)
                self.posx = 64
              
            else:
                self.limite_izq, self.limite_der = (0, 1024)
                self.posx = 0
            medidas, ancho, lineas = self.calcular(self.posx, posy) 
            ancho_total = ancho * lineas
            posy = 382 - (ancho_total/2)
            if self.tipo_texto == "instruccion":
                posy = self.y
            self.espacio = 6 + medidas[self.nro_linea]
            for i in self.img_palabras:
                if self.posx + i.rect.width > self.limite_der:
                    self.nro_linea += 1
                    self.espacio = 6 + medidas[self.nro_linea]
                    self.posx = self.limite_izq
                    posy += i.rect.height
                i.rect.left = self.posx
                i.rect.top = posy
                self.posx += i.rect.width + self.espacio
            width = 0
            for i in self.img_palabras:
                width += i.image.get_width()
            self.rect = pygame.Rect(self.x, self.y, width, ancho_total)
            
    def calcular_margenes(self):
        """
        Realiza un pre-cálculo usando una ubicación y margenes arbitrarios para determinar la cantidad de lineas
        que ocupa el texto.
        
        @return: El numero de lineas que ocupa el texto.
        @rtype: int
        """
        px = 128
        py = 0
        nro_lineas = 1
        medida_lineas = []
        lim_izq = 128
        lim_der = 896
        ppl = 0
        for i in self.img_palabras:
            if px + i.rect.width > lim_der:
                if ppl == 1 :
                    medida_lineas.append((lim_der - px)/ ppl)
                else:
                    medida_lineas.append((lim_der - px)/ (ppl-1.0))
                ppl = 0
                px = lim_izq
                py += i.rect.height
                nro_lineas += 1
            px += i.rect.width + self.espacio
            ppl += 1
        medida_lineas.append(0)
        return nro_lineas 
    
    def calcular(self, posx, posy):
        """
        Realiza el cálculo de los margenes y número de lineas reales a partir de las coordenadas X e Y.
        
        @param posx: Coordenada X donde se desea dibujar el texto.
        @type posx: int
        @param posy: Coordenada Y donde se desea dibujar el texto.
        @type posy: int
        @return: Un conjunto de valores que comprende: el alto y el ancho de las lineas y el número de lineas.
        @rtype: tuple
        """
        px = posx
        py = posy
        nro_lineas = 0
        medida_lineas = []
        ppl = 0
        ancho = 0
        for i in self.img_palabras:
            if px + i.rect.width > self.limite_der:
                if ppl == 1 :
                    medida_lineas.append((self.limite_der - px)/ ppl)
                else:
                    medida_lineas.append((self.limite_der - px)/ (ppl-1.0))
                ppl = 0
                px = self.limite_izq
                py += i.rect.height
                nro_lineas += 1
            px += i.rect.width + self.espacio
            ancho = i.rect.height
            ppl += 1
        medida_lineas.append(0) 
        return medida_lineas, ancho, nro_lineas +1
    
    def indexar(self, letra):
        """
        Permite destacar o restaurar un texto de tipo indice, suministrando la letra que debe destacarse.
        
        @param letra: Letra que se debe resaltar en el indice.
        @type letra: str
        """
        if self.tipo_texto == "indice":
            for i in self.img_palabras:
                if letra == i.palabra.strip():
                    i.selec = True
                    i.destacar()
                else:
                    i.restaurar()