#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from librerias import pantalla
from librerias.boton import boton
from librerias.texto import texto
from librerias.imagen import imagen
from librerias.animaciones import animacion

from paginas import menucfg
from paginas import pantalla2
from paginas import pantalla5
from paginas import pantalla10

class estado(pantalla.Pantalla):
    def __init__(self, parent):
        """
        Método inicializador de la clase. 
        
        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        """

        self.name = "screen_6"
        self.deteccion_movimiento = False
        self.parent = parent
        self.previa = True      
        self.background = pygame.image.load(self.fondos + "fondo-repro2.png").convert()
        self.caja_texto = imagen(self.fondos + "caja-texto.png", 0, 332)
        self.anim6 = animacion("anim6", self.anim + "animacion6.png", 3, 1, 630, 50, -1, True, 10)
        self.anim6_2 = animacion("anim6_2", self.anim + "animacion6-2.png", 3, 1, 50, 200, -1, True, 10)
        self.anim6_3 = animacion("anim6_3", self.anim + "animacion6-3.png", 1, 1, 100, 100, -1, True, 2)
        self.anim6_4 = animacion("anim6_4", self.anim + "animacion6-4.png", 4, 1, 350, 80, -1, False, 18)
        self.anim6_5 = animacion("anim6_5", self.anim + "animacion6-5.png", 4, 1, 350, 80, -1, False, 22)
        self.anim6_6 = animacion("anim6_6", self.anim + "animacion6-6.png", 6, 1, 350, 80, -1, False, 18)
        self.cargar_botones()
        self.cargar_textos()
        self.banner_repro = imagen(self.banners + "banner-repro.png", 0, 0)
        self.banner_inf = imagen(self.banners + "banner-inf.png", 0, 432)
        self.rect = pygame.Rect(0,0,0,0)
        self.reloj_anim = pygame.time.Clock()
        self.reloj_anim.tick(30)  
        self.resume()

    def cargar_textos(self):
        """
        Carga los textos utilizados en esta pantalla.
        """
        self.texto6_2 = texto(
            32, 
            340, 
            self.parent.text_content["content"][self.name]["text_2"],
            self.parent.config.t_fuente, 
            "normal", 
            992, 
            False
        )
        self.texto6_3 = texto(
            32, 
            340, 
            self.parent.text_content["content"][self.name]["text_3"],
            self.parent.config.t_fuente, 
            "normal", 
            992, 
            False
        )
        self.texto6_4 = texto(
            32, 
            340, 
            self.parent.text_content["content"][self.name]["text_4"],
            self.parent.config.t_fuente, 
            "normal", 
            992, 
            False
        )
        self.texto7_2 = texto(
            32, 
            340, 
            self.parent.text_content["content"][self.name]["text_5"],
            self.parent.config.t_fuente, 
            "normal", 
            992, 
            False
        )
        self.texto7_3 = texto(
            32, 
            340, 
            self.parent.text_content["content"][self.name]["text_6"],
            self.parent.config.t_fuente, 
            "normal", 
            992, 
            False
        )
        self.texto7_4 = texto(
            32, 
            340, 
            self.parent.text_content["content"][self.name]["text_7"],
            self.parent.config.t_fuente, 
            "normal", 
            992, 
            False
        )
        self.texto7_5 = texto(
            32, 
            340, 
            self.parent.text_content["content"][self.name]["text_8"],
            self.parent.config.t_fuente, 
            "normal", 
            992, 
            False
        )
        self.texto7_6 = texto(
            32, 
            340, 
            self.parent.text_content["content"][self.name]["text_9"],
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
        self.volver = boton("volver", "Regresar", self.botones + "boton-regresar.png", 3, 320, 445, None, False, 1)
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
            self.cargar_botones()
            self.cargar_textos()
            self.parent.config.texto_cambio = False
        self.grupo_anim.add(self.anim6, self.anim6_2)
        self.grupo_imagen.add(self.anim6_2)
        self.grupo_banner.add(self.banner_repro, self.banner_inf)
        self.grupo_botones.add(self.config, self.volver, self.sig, self.home)
        self.anim6.detener()
        self.creado = True
        self.final = False
        self.tiempo = 0        
        if self.anim_actual == 0:
            self.anim_actual = 1
        self.spserver.stopserver()
        self.entrada_primera_vez = True
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
                            
                elif self.deteccion_movimiento:
                    if event.key == pygame.K_RETURN:
                        if self.x.tipo_objeto == "boton":
                            if self.x.id == "sig":
                                self.repeticion = True            
                                if self.anim_actual <= 13: 
                                    self.anim_actual += 1
                                    self.reproducir_animacion(self.anim_actual)
                                self.deteccion_movimiento = False
                                 
                            elif self.x.id == "volver":  
                                self.anim_actual -= 1
                                self.reproducir_animacion(self.anim_actual)
                                self.deteccion_movimiento = False
                                 
                            elif self.x.id == "config":
                                self.limpiar_grupos()
                                self.parent.pushState(menucfg.estado(self.parent, self.previa))
                                self.deteccion_movimiento = False
                                
                            elif self.x.id == "home":
                                self.limpiar_grupos()
                                self.parent.changeState(pantalla2.estado(self.parent)) 
                                self.deteccion_movimiento = False
 
                        elif self.x.tipo_objeto == "palabra":
                            self.spserver.processtext(
                                self.parent.text_content["concepts"][self.x.codigo],
                                self.parent.config.activar_lector
                            )
                        
            if pygame.sprite.spritecollideany(self.raton, self.grupo_palabras):
                sprite = pygame.sprite.spritecollide(self.raton, self.grupo_palabras, False)
                if pygame.mouse.get_pressed() == (True, False, False):
                    if sprite[0].tipo_objeto == "palabra":
                        if sprite[0].interpretable == True:
                            self.parent.interpretar(sprite[0].codigo)
                                    
            if pygame.sprite.spritecollideany(self.raton, self.grupo_botones):
                sprite = pygame.sprite.spritecollide(self.raton, self.grupo_botones, False)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.spserver.stopserver()
                    if sprite[0].id == "home":
                        #self.spserver.stopserver()
                        self.limpiar_grupos()
                        self.parent.changeState(pantalla2.estado(self.parent))
                        
                    elif sprite[0].id == "config":
                        self.limpiar_grupos()
                        self.parent.pushState(menucfg.estado(self.parent, self.previa))
                      
                    elif sprite[0].id == "sig": 
                        if self.anim_actual <= 13: 
                            self.anim_actual += 1
                            self.reproducir_animacion(self.anim_actual)
                    elif sprite[0].id == "volver":                                                 
                        self.anim_actual -= 1
                        self.reproducir_animacion(self.anim_actual)    
        self.minimag(events)                  

    def reproducir_animacion(self, animacion):
        """
        Gestiona la reproducción de animaciones, imágenes y texto en esta pantalla.
        @param animacion: Indica la animación que debe reproducirse.
        @type animacion: int
        """
        if animacion <= 0:
            self.limpiar_grupos()
            self.parent.animacion = 10           
            self.parent.changeState(pantalla5.estado(self.parent, 9))
        elif animacion== 1:
            self.elemento_actual = -1
            self.grupo_anim.remove(self.anim6_3)
                        
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
                    
                self.grupo_anim.add(self.anim6_2)            
                self.grupo_fondotexto.add(self.caja_texto)
                self.grupo_palabras.add(self.texto6_2.img_palabras)
                self.txt_actual = self.texto6_2.img_palabras
                self.chequeo_palabra(self.txt_actual)
                self.anim6.continuar()                

        elif animacion == 2:
            self.entrada_primera_vez=False
            self.elemento_actual = -1
            self.lista_palabra = []
            self.grupo_anim.add(self.anim6)
            self.grupo_palabras.empty()
            self.grupo_fondotexto.empty()
            self.grupo_anim.add(self.anim6_3)
            self.anim6.detener()
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["anim_1"],
                self.parent.config.activar_lector
            )
                
        elif animacion == 3:
            self.elemento_actual = -1
            self.grupo_palabras.empty()
            self.grupo_anim.remove(self.anim6_3)
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto6_3.img_palabras)
            self.txt_actual = self.texto6_3.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_3"],
                self.parent.config.activar_lector
            )
            self.anim6.continuar()
                    
        elif animacion == 4:
            self.elemento_actual = -1
            self.grupo_anim.remove(self.anim6_4)
            self.grupo_palabras.empty()
            self.grupo_anim.remove(self.anim6_3)
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto6_4.img_palabras)
            self.txt_actual = self.texto6_4.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_4"],
                self.parent.config.activar_lector
            )
            self.anim6.continuar()
                    
        elif animacion == 5:
            self.elemento_actual = -1
            self.lista_palabra = []
            self.grupo_palabras.empty()
            self.grupo_fondotexto.empty()
            self.anim6_4.update()
            self.anim6_4.stop = False
            self.grupo_anim.add(self.anim6_4)
            self.anim6.detener()
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["anim_2"],
                self.parent.config.activar_lector
            )
                                                   
        elif animacion == 6:
            self.elemento_actual = -1
            self.grupo_anim.remove(self.anim6_4)
            self.grupo_palabras.remove(self.texto7_3.img_palabras)
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto7_2.img_palabras)
            self.txt_actual = self.texto7_2.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_5"],
                self.parent.config.activar_lector
            )
            self.anim6.continuar()
                
        elif animacion == 7:
            self.elemento_actual = -1
            self.grupo_palabras.empty()
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto7_3.img_palabras)
            self.txt_actual = self.texto7_3.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_6"],
                self.parent.config.activar_lector
            )
            self.anim6.continuar()
                    
        elif animacion == 8:
            self.elemento_actual = -1
            self.grupo_palabras.empty()
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto7_4.img_palabras)
            self.txt_actual = self.texto7_4.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_7"],
                self.parent.config.activar_lector
            )
            self.anim6.continuar()
                    
        elif animacion == 9:
            self.elemento_actual = -1
            self.grupo_anim.remove(self.anim6_5)
            self.grupo_palabras.empty()
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto7_5.img_palabras)
            self.txt_actual = self.texto7_5.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_8"],
                self.parent.config.activar_lector
            )
            self.anim6.continuar()
                    
        elif animacion == 10:
            self.elemento_actual = -1
            self.lista_palabra
            self.grupo_palabras.empty()
            self.grupo_fondotexto.empty()
            self.anim6_5.update()
            self.anim6_5.stop = False
            self.grupo_anim.add(self.anim6_5)
            self.anim6.detener()
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["anim_3"],
                self.parent.config.activar_lector
            )
                    
        elif animacion == 11:
            self.elemento_actual = -1
            self.grupo_anim.remove(self.anim6_6)
            self.grupo_anim.remove(self.anim6_5)
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto7_6.img_palabras)
            self.grupo_botones.add(self.sig)
            self.txt_actual = self.texto7_6.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_9"],
                self.parent.config.activar_lector
            )
            self.anim6.continuar()
                    
        elif animacion == 12:
            self.elemento_actual = -1
            self.grupo_tooltip.empty()
            self.grupo_palabras.empty()
            self.grupo_fondotexto.empty()
            self.anim6_6.update()
            self.anim6_6.stop = False
            self.grupo_botones.remove(self.sig)
            self.grupo_anim.add(self.anim6_6)
            self.anim6.detener()
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["anim_4"],
                self.parent.config.activar_lector
            )

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
                self.grupo_anim.add(self.anim6_2)            
                self.grupo_fondotexto.add(self.caja_texto)
                self.grupo_palabras.add(self.texto6_2.img_palabras)
                self.txt_actual = self.texto6_2.img_palabras
                self.chequeo_palabra(self.txt_actual)
                self.anim6.continuar()
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
        
    def ir_glosario(self):
        self.parent.pushState(pantalla10.estado(self.parent))
