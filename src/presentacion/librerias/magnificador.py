#!/usr/bin/env python

import pygame

class magnificador(pygame.sprite.Sprite):
    """
    Esta clase implementa un magnificador de pantalla que puede amplificar, disminuir y cambiar
    su ubicación en la pantalla.
    """
    def __init__(self):
        """
        Método inicializador de la clase.
        """
        pygame.sprite.Sprite.__init__(self)
        self.escala = 1
        self.zoom = 1
        self.w = 256
        self.h = 256
        self.cxp = 1024
        self.cyp = 572
        self.ampliador = pygame.Surface((self.w,self.h))
        self.sup_final = pygame.Surface
        self.rect = pygame.Rect((0,232), (self.w, self.h))
        
    def magnificar(self, ventana):
        """
        Ejecuta una secuencia de pasos para mostrar una región ampliada de la pantalla.
        Primero obtiene la posición del cursor en la pantalla, verifica el valor de la escala y el zoom, 
        seguidamente calcula los limites y por ultimo muestra la superficie del magnificador.
        
        @param ventana: Superficie de la pantalla que se desea amplificar o disminuir.
        @type ventana: pygame.Surface
        """
        x, y = pygame.mouse.get_pos()
        if self.escala >= 3 and self.zoom >= 4:
            self.escala = 3
            self.zoom = 4
        elif self.escala <= 1 and self.zoom <= 1:
            self.escala = 1
            self.zoom = 1       
    
        if self.escala == 1:
            self.ampliador = pygame.Surface((self.w / self.zoom, self.h / self.zoom))
            if x >= self.cxp - self.w / (2 * self.zoom):
                x = self.cxp - self.w / (2 * self.zoom)
            if y >= self.cyp - self.h / (2 * self.zoom):
                y = self.cyp - self.h / (2 * self.zoom)
            if x <= self.w / (2 * self.zoom):
                x = self.w / (2 * self.zoom)
            if y <= self.h / (2 * self.zoom):
                y = self.h / (2 * self.zoom)
            self.ampliador.blit(ventana, (0, 0), ((x - (self.w / (2 * self.zoom))), (y - (self.h / (2 * self.zoom))), self.w, self.h))
            self.sup_final = self.ampliador    
        
        elif self.escala == 2:
            self.ampliador = pygame.Surface((self.w / self.zoom, self.h / self.zoom))
            if x >= self.cxp - self.w / (2 * self.zoom):
                x = self.cxp - self.w / (2 * self.zoom)
            if y >= self.cyp - self.h / (2 * self.zoom):
                y = self.cyp - self.h / (2 * self.zoom)
            if x <= self.w / (2 * self.zoom):
                x = self.w / (2 * self.zoom)
            if y <= self.h / (2 * self.zoom):
                y = self.h / (2 * self.zoom)
            self.ampliador.blit(ventana, (0, 0), ((x - (self.w / (2 * self.zoom))), (y - (self.h / (2 * self.zoom))), self.w / self.zoom, self.h / self.zoom))
            sup_escalax2 = pygame.transform.scale2x(self.ampliador)
            self.sup_final = pygame.transform.smoothscale(sup_escalax2, (self.w, self.h))                
        
        elif self.escala == 3:
            self.ampliador = pygame.Surface((self.w / self.zoom, self.h / self.zoom))
            if x >= self.cxp - self.w / (2 * self.zoom):
                x = self.cxp - self.w / (2 * self.zoom)
            if y >= self.cyp - self.h / (2 * self.zoom):
                y = self.cyp - self.h / (2 * self.zoom)
            if x <= self.w / (2 * self.zoom):
                x = self.w / (2 * self.zoom)
            if y <= self.h / (2 * self.zoom):
                y = self.h / (2 * self.zoom)  
            self.ampliador.blit(ventana, (0, 0), ((x - (self.w / (2 * self.zoom))), (y - (self.h / (2 * self.zoom))), self.w / self.zoom, self.h / self.zoom))
            sup_escalax2 = pygame.transform.scale2x(self.ampliador)
            sup_escalax4 = pygame.transform.scale2x(sup_escalax2)
            self.sup_final = pygame.transform.smoothscale(sup_escalax4, (self.w, self.h))  
        self.image = self.sup_final

    def aumentar(self):
        """
        Aumenta el zoom del magnificador.
        """
        self.escala = self.escala + 1
        self.zoom = (2 ** self.escala) / 2
        
    def disminuir(self):
        """
        Disminuye el zoom del magnificador.
        """
        self.escala = self.escala - 1
        self.zoom = (self.zoom / 2)
   
class Rendermag(pygame.sprite.Group):
    """
    Esta clase es una ligera modificación de la clase pygame.sprite.Group. 
    Dibuja el magnificador sobre la pantalla. 
    """
    def draw(self, surface, mov):
        """
        Dibuja los miembros de un grupo de sprites sobre una superficie.
        
        @param surface: Superficie sobre la que se dibujara el magnificador.
        @type surface: pygame.Surface
        @param mov: Determina si el magnificador esta en movimiento. Si es True, dibuja un rectángulo
        negro sobre el magnificador, lo cual indica que esta cambiando de posición.
        @type mov: bool
        """
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            self.spritedict[spr] = surface_blit(spr.image, spr.rect)
            pygame.draw.rect(surface, (0, 0, 0), spr.rect, 2)
            if mov:
                pygame.draw.rect(surface, (0, 0, 0), spr.rect)