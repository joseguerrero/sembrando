#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from .palabra import palabra

class cajatexto(pygame.sprite.Sprite):
    """
    Esta clase permite manipular el contenido de una caja de texto, gestionando los caracteres ingresados 
    por el teclado y el desplazamiento del texto a medida que la caja se llena.
    """
    def __init__(self, x, y, lista_respuestas, screen, tamano = "high"):
        """
        Método inicializador de la clase.
        
        @param x: Coordenada en X donde se ubicara la caja de texto.
        @type x: int
        @param y: Coordenada en Y donde se ubicara la caja de texto.
        @type y: int
        @param lista_respuestas: Texto que se mostrara en la caja de texto.
        @type lista_respuestas: str
        @param screen: Superficie sobre la cual aparecerá la caja de texto.
        @type screen: pygame.Surface
        @param tamano: Establece el tamaño de la caja de texto. Puede tomar los siguientes valores:
        low: Pequeño, medium: Mediano, high: Grande.
        @type tamano: int
        """
        self.eventlist = [1,2,3,4,5,6,7,8,9,0,"q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
        self.time = pygame.time.Clock()
        self.time.tick(30)
        self.x = 0
        self.indicador =" "
        self.teclado = False
        self.screen = screen
        self.screen_center = screen.get_rect().center
        self.salir = True
        self.rect= pygame.rect
        self.alto = 0
        if tamano =="high": 
            img = pygame.image.load("../imagenes/png/varios/cuadro-texto.png")
            self.ancho = img.get_rect().width
            self.rect = img.get_rect()
        if tamano=="medium":
            img = pygame.image.load("../imagenes/png/varios/cuadro-texto.png")
            self.ancho = img.get_rect().width
            self.rect = img.get_rect()
        if tamano == "low":
            img = pygame.image.load("../imagenes/png/varios/cuadro-texto.png")
            self.ancho = img.get_rect().width 
            self.rect = img.get_rect()
        self.rect.move_ip(x, y)        
        self.palabra = []
        self.palabra_f = str
        self.reloj = pygame.time.Clock()
        self.letras_caja= pygame.sprite.Sprite()
        self.ancho = self.rect.width
        self.respuestas = lista_respuestas
        self.boton = pygame.sprite.Sprite()
        self.boton.rect = (self.rect.left + 80, 0, 60, 30)

    def generador(self, letra):   
        """
        Permite identificar la tecla pulsada.
        
        @param letra: Código correspondiente a la tecla pulsada.
        @type letra: int
        """
        if letra == "+1":
            self.palabra.append(" ")            
        elif letra == "-1": 
            if len(self.palabra) >= 1:
                self.palabra.pop()                
        elif letra == 48:
            self.palabra.append("0")
        elif letra == 49:
            self.palabra.append("1")
        elif letra == 50:
            self.palabra.append("2")
        elif letra == 51:
            self.palabra.append("3")
        elif letra == 52:
            self.palabra.append("4")
        elif letra == 53:
            self.palabra.append("5")                        
        elif letra == 54:
            self.palabra.append("6")    
        elif letra == 55:
            self.palabra.append("7")            
        elif letra == 56:
            self.palabra.append("8")            
        elif letra == 57:
            self.palabra.append("9")
                                 
    def renderizado(self):
        """
        Se encarga de dar formato y renderizar el texto deseado en la superficie seleccionada.
        """
        palabras = ""        
        for i in self.palabra:
            palabras += i
        self.palabra_f = palabras
        palabras += self.indicador
        x = palabra(palabras, 20, "caja_texto")
        self.letras_caja.image = x.get_palabra()
        self.letras_caja.image.set_colorkey((255, 255, 255))
        self.letras_caja.rect = self.letras_caja.image.get_rect()
        rect = ( self.letras_caja.rect.width - self.ancho, 0, self.ancho, self.letras_caja.rect.height )
        if self.letras_caja.rect.width > self.ancho:
            self.letras_caja.image = self.letras_caja.image.subsurface(rect)
        self.letras_caja.rect = x.get_rect()
        self.letras_caja.rect.top = self.rect.top
        self.letras_caja.rect.left = self.rect.left

    def eventos (self, event):
        """
        Se encarga de gestionar los eventos relacionados con la caja de texto.
        
        @param event: Lista que contiene los eventos generados cada vez que se actualiza la pantalla.
        @type event: list 
        @return: Retorna True si el evento recibido es presionar la tecla ENTER.
        @rtype: bool 
        """
        if event.type == pygame.K_ESCAPE:
            self.salir = False      
        if event.type == pygame.QUIT:
            pygame.quit()  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.generador("-1")
            elif event.key == pygame.K_SPACE:
                self.generador ("+1")
            elif event.key == pygame.K_RETURN:
                return True
            else:                                      
                self.generador (event.key)        
        self.renderizado()
    
    def titilar(self):
        """
        Renderiza el carácter '|' sobre la caja de texto cada 600 milisegundos.
        """
        if self.teclado:
            self.x += self.time.get_time()
            if self.x in range (0, 400):
                self.indicador = "|"
            else:
                self.indicador = " "
            if self.x > 600:
                self.x =0
            self.renderizado()
        else:
            self.indicador = " "
            self.renderizado()
    
    def iniciar(self, event, teclado):
        """
        Verifica si se esta ingresando texto en la caja de texto.
        
        @param event: Ultimo evento recibido para ser evaluado.
        @type event: pygame.event.Event
        @param teclado: Determina si se ha escrito algo en la caja de texto.
        @type teclado: bool
        @return: Retorna verdadero si se escribe algo en la caja de texto.
        @rtype: bool
        """
        self.teclado = teclado
        if teclado:
            if self.eventos(event):
                return True

    def reiniciar (self):
        self.palabra = []
        self.palabra_f = ""
    
    def comparador(self):
        if self.respuestas.lower() == self.palabra_f:
            return True
        else:
            return False
        
    def comparador_longitud(self):
        """
        Verifica la cantidad de caracteres de la caja de texto para determinar
        si la respuesta ingresada es de dos caracteres.
        
        @return: Si la caja de texto tiene dos o mas caracteres, retorna True, de lo contrario retorna False.
        @rtype: bool
        """
        if len (self.palabra) >= 2:
            return True
        else:
            return False        
        
    def caja_vacia(self):
        """
        Verifica la cantidad de caracteres de la caja de texto para determinar si esta vacía.
        
        @return: Si la caja de texto esta vacía, retorna True, de lo contrario retorna False.
        @rtype: bool
        """
        if len(self.palabra) < 1:
            return True
        else:
            return False
              
    def get_palabra(self):
        """
        Retorna el texto que se a introducido.
    
        @return: retorna una cadena con el texto introducido.
        @rtype: str
        """
        return self.palabra_f
        
    def get_imagen(self, grupo):
        grupo.add(self.letras_caja)
        
    def set_x(self, x):
        """
        Cambia la posición en el eje X de la caja de texto.

        @param x: Indica la posición en X de la caja de texto. 
        @type x: int
        """
        self.x = x
        
    def set_y (self, y):
        """
        Cambia la posición en el eje Y de la caja de texto.
        
        @param y: Indica la posición en Y de la caja de texto.
        @type y: int 
        """
        self.y = y