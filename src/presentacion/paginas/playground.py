#!/usr/bin/env python3

import pygame

from librerias import pantalla
from librerias.button import Button
from librerias.image import Image
from paginas import pantalla2

class estado(pantalla.Pantalla):
    def __init__(self, parent, previa = False):

        self.name = "playground"
        self.previa = previa
        self.parent = parent
        self.background = pygame.image.load(self.fondos + "fondo-inicio.png").convert()
        self.fondo_simple = pygame.image.load(self.fondos + "fondo-simple.png").convert()

        self.banner_inf = Image(0, 432, self.banners + "banner-inf.png")

        # This banner shouldn't be needed here but in the next screen
        self.banner_config = Image(0, 0, self.banners + "banner-acc.png")

        self.load_buttons()

        self.cargar_img_intrucciones()

        self.rect = pygame.Rect(0, 0, 0, 0)

        self.resume()
        
    def cargar_img_intrucciones(self):
        """
        Carga las imágenes usadas para las instrucciones iniciales.
        """
        self.img1 = pygame.image.load(self.pops + "touch.png").convert_alpha()
        self.img2 = pygame.image.load(self.pops + "flechas.png").convert_alpha()
        self.img3 = pygame.image.load(self.pops + "enter.png").convert_alpha()
        self.img4 = pygame.image.load(self.pops + "f1.png").convert_alpha()
        self.img5 = pygame.image.load(self.pops + "sordo.png").convert_alpha()
        self.img6 = pygame.image.load(self.pops + "visual.png").convert_alpha()
        self.dic_img = {
            "RATON": self.img1, 
            "TECLAS": self.img2, 
            "ENTER": self.img3, 
            "F1": self.img4,
            "DFA": self.img5,
            "DFV": self.img6
        }
        
    def load_buttons(self):
        """
        Carga los botones utilizados en esta pantalla.
        """

        self.inicio = Button(650, 440, "inicio", "Inicio", self.botones + "boton-inicio.png", frames=3, frame_speed=1)
        
    def start(self):
        pass
 
    def cleanUp(self):
        pass
 
    def pause(self):
        pass
 
    def resume(self):
        """
        Verifica si es la primera vez que se muestra esta pantalla. Carga los objetos correspondientes
        según el caso.
        """

        self.load_buttons()
        self.grupo_banner.add(self.banner_inf)
        self.grupo_botones.add(self.inicio)

    def handleEvents(self, events):
        """
        Evalúa los eventos que se generan en esta pantalla.        

        @param events: Lista de los eventos.
        @type events: list
        """

        self.teclasPulsadas = pygame.key.get_pressed()
        for event in events:    
            if event.type == pygame.QUIT:
                self.parent.quit()

            if event.type == pygame.KEYDOWN:
                self.chequeo_botones(self.grupo_botones)
                self.numero_elementos = len(self.lista_botones)

                if event.key == pygame.K_RIGHT:
                    if self.elemento_actual < self.numero_elementos:
                        self.elemento_actual += 1
                        if self.elemento_actual >= self.numero_elementos:
                            self.elemento_actual = self.numero_elementos - 1
                        self.x = self.lista_botones[self.elemento_actual]
                        self.spserver.processtext(self.x.tooltip, True)
                        self.definir_rect(self.x.rect)  
                        self.deteccion_movimiento = True  

                elif event.key == pygame.K_LEFT:
                    if self.elemento_actual > 0:
                        self.elemento_actual -= 1
                        if self.elemento_actual <=0:
                            self.elemento_actual = 0
                        self.x = self.lista_botones[self.elemento_actual]
                        self.spserver.processtext(self.x.tt, True)
                        self.definir_rect(self.x.rect)
                        self.deteccion_movimiento = True

                elif self.deteccion_movimiento:   
                    if event.key == pygame.K_RETURN:
                        self.elemento_actual = -1
                        if self.x.tipo_objeto == "boton":
                            if self.x.id == "inicio":
                                self.limpiar_grupos()
                                self.parent.changeState(pantalla2.estado(self.parent))  
                                
                            elif self.x.id == "puerta":
                                self.limpiar_grupos()
                                self.parent.popState()

            if pygame.sprite.spritecollideany(self.raton, self.grupo_botones):
                sprite = pygame.sprite.spritecollide(self.raton, self.grupo_botones, False)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.spserver.stopserver()
                    if sprite[0].id == "inicio":
                        self.limpiar_grupos()
                        self.parent.changeState(pantalla2.estado(self.parent))

                    elif sprite[0].id == "puerta":
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
        
    def draw(self):
        """
        Dibuja el fondo de pantalla y los elementos pertenecientes a los grupos de sprites sobre la superficie 
        del manejador de pantallas.
        """

        self.parent.screen.blit(self.background, (0, 0))
        self.grupo_banner.draw(self.parent.screen)
        self.grupo_botones.draw(self.parent.screen)
        self.grupo_fondotexto.draw(self.parent.screen)
        self.grupo_palabras.draw(self.parent.screen)
        self.grupo_tooltip.draw(self.parent.screen)
        self.grupo_popup.draw(self.parent.screen)
        if self.parent.habilitar:
            self.grupo_magnificador.draw(self.parent.screen, self.enable)   
        self.dibujar_rect()
        self.draw_debug_rectangles()
