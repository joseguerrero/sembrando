#!/usr/bin/env python

import pygame

from librerias import pantalla
from librerias.boton import boton
from librerias.texto import texto
from librerias.imagen import imagen
from librerias.animaciones import animacion

from paginas import menucfg
from paginas import pantalla2
from paginas import pantalla4
from paginas import pantalla10

class estado(pantalla.Pantalla):
    def __init__(self, parent):
        """
        Método inicializador de la clase. 
        
        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        """

        self.name = "screen_3"
        self.deteccion_movimiento = False
        self.parent = parent
        self.previa = True
        self.background = pygame.image.load(self.fondos + "fondo-plantas.png").convert()
        self.anim1 = animacion("anim1", self.anim + "animacion3.png", 8, 1, 100, 200, -1, True, 5)
        self.caja_texto = imagen(self.fondos + "caja-texto.png", 0, 332)
        self.banner_plantas = imagen(self.banners + "banner-plantas.png", 0, 0)
        self.banner_inf = imagen(self.banners + "banner-inf.png", 0, 432)
        self.cargar_textos()
        self.cargar_botones()
        self.reloj_anim = pygame.time.Clock()
        self.reloj_anim.tick(30)
        self.resume() 
        
    def cargar_textos(self):
        """
        Carga los textos utilizados en esta pantalla.
        """
        self.texto3_2 = texto(
            32,
            340,
            self.parent.text_content["content"][self.name]["text_2"],
            self.parent.config.t_fuente,
            "normal",
            992,
            False
        )
    
    def cargar_botones(self):
        """
        Carga los botones utilizados en esta pantalla.
        """
        self.home = boton("home", "Menú", self.botones + "boton-menu.png", 3, 889, 440, None, False, 1)
        self.sig = boton("sig", "Avanzar", self.botones + "boton-avanzar.png", 3, 560, 440, None, False, 1)
        self.config = boton("config", "Accesibilidad", self.botones + "boton-acc.png", 3 ,60, 445, None, False, 1)
    
    def start(self):
        pass
 
    def cleanUp(self):
        pass
 
    def pause(self):
        pass
 
    def resume(self):
        """
        Verifica si se realizaron cambios en la configuración. Carga los valores iniciales de esta pantalla.
        """
        if self.parent.config.texto_cambio == True:
            self.cargar_textos()
            self.cargar_botones()
            self.parent.config.texto_cambio = False
        self.grupo_anim.add(self.anim1)
        self.grupo_banner.add(self.banner_plantas, self.banner_inf)
        self.grupo_botones.add(self.config, self.sig, self.home)
        self.tiempo = 0
        self.creado = True
        self.final = False
        self.anim1.detener()
        self.spserver.stopserver()
        self.entrada_primera_vez = True        
        self.spserver.processtext(
            "Pantalla: Las Plantas",
            self.parent.config.activar_lector
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
                                self.parent.pushState(menucfg.estado(self.parent, self.previa)) 
                                 
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
                                self.parent.config.activar_lector
                            )
                        self.deteccion_movimiento = False

                elif event.key == pygame.K_SPACE:
                    self.spserver.processtext(
                        self.parent.text_content["content"][self.name]["text_2"],
                        self.parent.config.activar_lector
                    ) 
                    
            if pygame.sprite.spritecollideany(self.raton, self.grupo_palabras):
                sprite = pygame.sprite.spritecollide(self.raton, self.grupo_palabras, False)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if sprite[0].tipo_objeto == "palabra":
                        if sprite[0].interpretable == True:
                            self.parent.interpretar(sprite[0].codigo)

            if pygame.sprite.spritecollideany(self.raton, self.grupo_botones):
                sprite = pygame.sprite.spritecollide(self.raton, self.grupo_botones, False)
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
            self.anim1.continuar()
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto3_2.img_palabras)
            self.txt_actual = self.texto3_2.img_palabras
            self.chequeo_palabra(self.txt_actual)
            
            if self.parent.config.activar_lector:
                if self.entrada_primera_vez:
                    self.spserver.processtext2(
                        self.parent.text_content["content"][self.name]["text_2"],
                        self.parent.config.activar_lector
                    )
                    self.entrada_primera_vez = False
                else:
                    self.spserver.processtext(
                        self.parent.text_content["content"][self.name]["text_2"],
                        self.parent.config.activar_lector
                    )
                self.anim1.continuar()
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
                self.anim1.continuar()
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
        if self.parent.habilitar:
            self.grupo_magnificador.draw(self.parent.screen, self.enable)
        if self.deteccion_movimiento:
            self.dibujar_rect()
        
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
        esc = 1.0/div 
        for _ in range(1, div+1):
            px -= rx/div
            py -= ry/div
            vx += esc
            vy += esc
            fondo_amp = pygame.transform.smoothscale(self.background, (int(rx*vx), int(ry*vy)))
            self.parent.screen.blit(fondo_amp, (px,py))
            pygame.time.delay(30)
            pygame.display.update()
    
    def mcd(self, x, y):
        if y == 0:
            return x
        else:
            return self.mcd(y, x % y)
        
    def ir_glosario(self):
        self.parent.pushState(pantalla10.estado(self.parent))
