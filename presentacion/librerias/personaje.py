#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from eventos import ManejadorEventos

class personaje(pygame.sprite.Sprite):
    """
    Esta clase implementa un personaje que puede ser controlado mediante el teclado, incluye interacción con
    elementos externos y permite cambiar la imagen que lo representa.
    """
    pygame.mixer.init()
    izq = False
    """Indica si la orientación del personaje es hacia la izquierda. """
    ocupado = False
    """Indica si el personaje esta ocupado, de manera que se bloqueen los eventos hasta que se desocupe. """
    chocando = False
    """Indica si el personaje esta chocando con uno o mas elementos externos. """
    dic_der = {}
    """ Diccionario que contiene los rectángulos de las imágenes del personaje orientadas a la derecha."""
    dic_izq = {}
    """ Diccionario que contiene los rectángulos de las imágenes del personaje orientadas a la izquierda."""
    tiempo = 0
    """Se utiliza para sincronizar la reproducción del sonido del personaje. """
    codigo = 0
    """Indica la imagen del personaje que debe mostrarse a medida que progresa. """
    vel_anim = 4
    """Velocidad de movimiento del personaje. """
    fotograma = 0
    """Fotograma actual del personaje. """
    varios = "../imagenes/png/varios/"
    """Ruta de las imágenes del personaje. """
    sonido_choque = pygame.mixer.Sound("../audio/choque.ogg")
    """Sonido que indica que el personaje esta chocando. """
    sonido_caminar = pygame.mixer.Sound("../audio/pasos.ogg")
    """Sonido que indica que el personaje va por el camino correcto. """
    
    def __init__(self, x, y, imagen, frames):
        """
        Método inicializador de la clase.
        
        @param x: Ubicación en la coordenada X del personaje.
        @type x: int
        @param y: Ubicación en la coordenada Y del personaje.
        @type y: int
        @param imagen: Ruta de la imagen que representa al personaje.
        @type imagen: str
        @param frames: Cantidad de fotogramas que contiene la imagen del personaje.
        @type frames: int
        """
        pygame.sprite.Sprite.__init__(self)
        self.dic_imagenes = {
            -1: self.varios + "0.png",
            0: self.varios + "0.png", 1: self.varios + "1.png", 2:self.varios + "2.png", 3: self.varios + "3.png", 
            4: self.varios + "4.png", 5: self.varios + "5.png", 6: self.varios + "6.png", 7: self.varios + "7.png",
            8: self.varios + "8.png", 9: self.varios + "9.png", 10: self.varios + "10.png", 11: self.varios + "11.png",
            12: self.varios + "12.png", 13: self.varios + "13.png", 14: self.varios + "14.png", 15: self.varios + "15.png",
            16: self.varios + "16.png", 17: self.varios + "17.png", 18: self.varios + "18.png", 19: self.varios + "19.png",
            20: self.varios + "20.png", 21: self.varios + "21.png", 22: self.varios + "22.png", 23: self.varios + "23.png",
            24: self.varios + "24.png", 25: self.varios + "25.png", 26: self.varios + "26.png", 27: self.varios + "27.png",
            28: self.varios + "28.png", 29: self.varios + "29.png", 30: self.varios + "30.png", 31: self.varios + "31.png",
            }
        self.posx = x
        self.posy = y
        self.vel = 200
        self.eh = ManejadorEventos()
        self.img_der = pygame.image.load(imagen).convert_alpha()
        self.img_izq = pygame.transform.flip(self.img_der, True, False)
        self.alto = self.img_der.get_height()
        self.ancho = self.img_der.get_width()
        self.frames = frames
        self.calcular_rectangulos()
        self.image = self.img_der
        self.rect2 = self.dic_izq[self.fotograma]
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.rt_car = pygame.Rect(0, 0, 32, 32)
        self.actualizar()
        
    def por_defecto(self, x, y, imagen, frames, limites):
        """
        Establece valores por defecto a los atributos mas importantes del personaje.
        
        @param x: Ubicación en la coordenada X del personaje.
        @type x: int
        @param y: Ubicación en la coordenada Y del personaje.
        @type y: int
        @param imagen: Ruta de la imagen que representa al personaje.
        @type imagen: str
        @param frames: Cantidad de fotogramas que contiene la imagen del personaje.
        @type frames: int
        @param limites: Lista de los objetos con los que puede chocar el personaje.
        @type limites: list
        """
        self.posx = x
        self.posy = y  
        self.cambiar_imagen(imagen)
        self.frames = frames 
        self.limites = limites
        self.vel_anim = 4
        self.codigo = 0
        
    def cambiar_vel(self):
        """
        Reduce la velocidad del personaje 0.5.
        """
        self.vel_anim = self.vel_anim - 0.5
        
    def cambiar_imagen(self, imagen):
        """
        Cambia la imagen que representa al personaje y la ajusta dependiendo de la orientación del mismo.
        @param imagen: Ruta de la nueva imagen que se cargara.
        @param imagen: str
        """
        self.img_der = pygame.image.load(imagen).convert_alpha()
        self.img_izq = pygame.transform.flip(self.img_der, True, False)
        if self.izq:
            self.alto = self.img_izq.get_height()
            self.ancho = self.img_izq.get_width()
            self.calcular_rectangulos()
            self.image = self.img_izq
            self.rect2 = self.dic_izq[self.fotograma]
        else:
            self.alto = self.img_der.get_height()
            self.ancho = self.img_der.get_width()
            self.calcular_rectangulos()
            self.image = self.img_der
            self.rect2 = self.dic_der[self.fotograma]
        self.actualizar()
        
    def reubicar(self, posx, posy):
        """
        Cambia la posición del personaje.
        
        @param posx: Ubicación en la coordenada X del personaje.
        @type posx: int
        @param posy: Ubicación en la coordenada Y del personaje.
        @param posy: int
        """
        self.posx, self.posy = (posx, posy)
        self.actualizar_rects()
        self.actualizar()
    
    def calcular_rectangulos(self):
        """
        Determina las dimensiones de los rectángulos a partir de las imágenes cargadas previamente.
        """
        x = 0
        y = 0
        w = self.ancho / self.frames
        h = self.alto
        for i in range(self.frames):
            self.dic_der[i] = pygame.Rect(x, y, w, h)
            x += w
            self.dic_izq[i] = pygame.Rect(self.ancho - x, y, w, h)
        
    def chdir(self, direction):
        """
        Cambia la dirección del personaje.
        
        @param direction: Indica la nueva dirección del personaje.
        @param direction: str
        """
        if not self.ocupado:
            if direction == 'der':
                if self.izq == True:
                    self.posx = self.posx + (self.ancho/4)
                self.izq = False
                self.image = self.img_der
               
            if direction == 'izq':
                if self.izq == False:
                    self.posx = self.posx - (self.ancho/4)
                self.izq = True
                self.image = self.img_izq
    
    def mover(self, direction): 
        """
        Mueve el personaje.
        
        @param direction: Indica la nueva dirección en la que se mueve personaje.
        @type direction: str
        """
        if not self.ocupado:
            if direction == 'arriba':
                self.posy -= self.vel_anim
                self.sonido_caminar.play()
                self.actualizar_rects()
                self.actualizar()
                
            if direction == 'abajo':
                self.posy += self.vel_anim
                self.sonido_caminar.play()
                self.actualizar_rects()
                self.actualizar()
                
            if direction == 'izq':
                self.posx -= self.vel_anim
                self.sonido_caminar.play()
                self.actualizar_rects()
                self.actualizar()
                
            if direction == 'der':
                self.posx += self.vel_anim
                self.sonido_caminar.play()
                self.actualizar_rects()
                self.actualizar()
        
    def chequear_limites(self, direction):
        """
        Verifica si el personaje choca con algún objeto, en caso de chocar anula el movimiento en la dirección 
        indicada.
        
        @param direction: Indica la dirección del personaje.
        @type direction: str
        """
        if pygame.sprite.spritecollideany(self, self.limites):
            self.sonido_caminar.set_volume(0)
            self.sonido_choque.play()
            self.chocando = True
            if direction == 'arriba':
                dire = 'abajo'
            elif direction == 'abajo':
                dire = 'arriba'
            elif direction == 'izq':
                dire = 'der'
            elif direction == 'der':
                dire = 'izq'
            else:
                dire = 'none'
            self.mover(dire)
        else:
            self.sonido_caminar.set_volume(100)
            self.chocando = False
    
    def update(self):
        """
        Actualiza y monitorea el movimiento, la dirección y colisiones del personaje.
        """
        self.eh.update()
        if self.eh.held(pygame.K_UP):
            direction = 'arriba'
        elif self.eh.held(pygame.K_DOWN):
            direction = 'abajo'
        elif self.eh.held(pygame.K_LEFT):
            direction = 'izq'
        elif self.eh.held(pygame.K_RIGHT):
            direction = 'der'
        else:
            direction = 'none'
        self.chdir(direction)
        self.mover(direction)
        self.chequear_limites(direction)
        
    def actualizar_rects(self):
        """
        Actualiza la imagen que representa al personaje cuando este cambia de orientación.
        """
        if self.izq:
            self.rect.left, self.rect.top = (self.posx + (self.ancho/32)*11, self.posy + 188)
            self.rt_car.left, self.rt_car.top = (self.rect.left - (self.ancho/4), self.posy + 188)
        else:
            self.rect.left, self.rect.top = (self.posx + (self.ancho/32)*3 , self.posy + 188)
            self.rt_car.left, self.rt_car.top = (self.posx + 160, self.posy + 188)
    
    def actualizar(self):
        """
        Actualiza los fotogramas del personaje cuando se mueve, para dar la sensación de que esta caminando.
        """
        if pygame.time.get_ticks() - self.tiempo > self.vel:
            self.tiempo = pygame.time.get_ticks()
            self.fotograma = self.fotograma + 1
            if self.fotograma > self.frames -1:
                self.fotograma = 0
            if self.izq:
                self.rect2 = self.dic_izq[self.fotograma]
            else:
                self.rect.left + (self.ancho/4)
                self.rect2 = self.dic_der[self.fotograma]
                
class RenderChar(pygame.sprite.Group):
    """
    Esta clase es una ligera modificación de la clase pygame.sprite.Group.
    Permite cambiar el fotograma del personaje mientras este se mueve.
    """
    
    def draw(self, surface):
        """
        Dibuja los miembros de un grupo de sprites sobre una superficie.
        
        @param surface: Superficie sobre la que se dibujaran los sprites pertenecientes a este grupo.
        @type surface: pygame.Surface
        """
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            self.spritedict[spr] = surface_blit(spr.image, (spr.posx, spr.posy), spr.rect2)