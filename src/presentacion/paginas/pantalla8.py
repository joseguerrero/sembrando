#!/usr/bin/env python

import pygame

from librerias import pantalla
from librerias.button import Button
from librerias.texto import texto
from librerias.image import Image
from librerias.animaciones import animacion

from paginas import menucfg
from paginas import pantalla2
from paginas import pantalla9
from paginas import pantalla10

class estado(pantalla.Pantalla):
    def __init__(self, parent, anim_actual = 0):
        """
        Método inicializador de la clase. 
        
        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        @param anim_actual: Código de la ultima animación mostrada en esta pantalla.
        @type anim_actual: int
        """
        
        self.name = "screen_8"
        self.deteccion_movimiento = False
        self.parent = parent
        self.previa = True
        self.anim_actual = anim_actual
        pygame.display.set_caption('Sembrando para el futuro')
        self.background = pygame.image.load(self.fondos + "fondo-agri.png").convert()
        self.anim8 =  animacion("anim8", self.anim + "animacion8.png", 5, 1, 130, 110, -1, True, 8)
        self.anim8_0 =  animacion("anim8_0", self.anim + "animacion8-0.png", 1, 1, 700, 150, -1, False, 18)
        self.caja_texto = Image(0, 332, self.fondos + "caja-texto.png")
        self.banner_agri = Image(0, 0, self.banners + "banner-agri.png")
        self.banner_inf = Image(0, 432, self.banners + "banner-inf.png")
        self.cargar_botones()
        self.cargar_textos()
        self.reloj_anim = pygame.time.Clock()
        self.reloj_anim.tick(30)
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.tiempo = 0      
        self.tractor = -2     
        self.resume()
   
    def cargar_textos(self):
        """
        Carga los textos utilizados en esta pantalla.
        """
        self.texto8_2 = texto(
            32, 
            340, 
            self.parent.text_content["content"][self.name]["text_2"],
            self.parent.config.t_fuente, 
            "normal", 
            992, 
            False
        )
        self.texto8_3 = texto(
            32, 
            340, 
            self.parent.text_content["content"][self.name]["text_3"],
            self.parent.config.t_fuente, 
            "normal", 
            992, 
            False
        )
        self.texto8_4 = texto(
            32, 
            340, 
            self.parent.text_content["content"][self.name]["text_4"],
            self.parent.config.t_fuente, 
            "normal", 
            992, 
            False
        )
    
    def cargar_botones(self):
        """
        Carga los botones utilizados en esta pantalla.
        """
        self.home = Button(889, 440, "home", "Menú", self.botones + "boton-menu.png", 3, None, False, 1)
        self.sig = Button(560, 440, "sig", "Avanzar", self.botones + "boton-avanzar.png", 3, None, False, 1)
        self.volver = Button(320, 445, "volver", "Regresar", self.botones + "boton-regresar.png", 3, None, False, 1)
        self.config = Button(60, 445, "config", "Accesibilidad", self.botones + "boton-acc.png", 3, None, False, 1)
        
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
        self.grupo_anim.add(self.anim8)
        self.grupo_imagen.add(self.anim8_0)
        self.grupo_banner.add(self.banner_agri, self.banner_inf)
        self.grupo_botones.add(self.config, self.sig, self.home)
        self.creado = True
        self.final = False
        if self.anim_actual == 0:
            self.anim_actual = 1
        self.entrada_primera_vez = True
        self.spserver.processtext(u"Pantalla: La Agricultura en Venezuela: ", self.parent.config.activar_lector)
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
                if event.key == pygame.K_RIGHT:
                    self.controlador_lector_evento_K_RIGHT()
                    self.deteccion_movimiento = True
                           
                elif event.key == pygame.K_LEFT:
                    self.controlador_lector_evento_K_LEFT()
                
                elif self.deteccion_movimiento:
                    if event.key == pygame.K_RETURN:
                        if self.x.tipo_objeto == "boton":
                            if self.x.id == "config":
                                self.limpiar_grupos()
                                self.parent.pushState(menucfg.estado(self.parent, self.previa))
                                self.deteccion_movimiento = False
                                
                            elif self.x.id == "sig":
                                if self.anim_actual <= 11: 
                                    self.anim_actual += 1
                                    self.reproducir_animacion(self.anim_actual)
                                self.deteccion_movimiento = False
                                
                            elif self.x.id == "volver":   
                                if self.anim_actual > 0:
                                    self.anim_actual -= 1
                                    self.reproducir_animacion(self.anim_actual)
                                    if self.anim_actual <= 0:
                                        self.anim_actual = 0       
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
                        
            if pygame.sprite.spritecollideany(self.raton, self.grupo_botones):
                sprite = pygame.sprite.spritecollide(self.raton, self.grupo_botones, False)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.spserver.stopserver()
                    if sprite[0].id == "home":
                        self.limpiar_grupos()
                        self.parent.changeState(pantalla2.estado(self.parent))
                    elif sprite[0].id == "config":
                        self.limpiar_grupos()
                        self.parent.pushState(menucfg.estado(self.parent, self.previa))
                    elif sprite[0].id == "sig": 
                        self.repeticion = True
                        self.deteccion_movimiento = False
                        if self.anim_actual <= 11: 
                            self.anim_actual += 1
                            self.reproducir_animacion(self.anim_actual)
                    elif sprite[0].id == "volver":
                        self.deteccion_movimiento = False
                        if self.anim_actual > 0:                                       
                            self.anim_actual -= 1
                            self.reproducir_animacion(self.anim_actual)  
                    elif sprite[0].id == "repe":
                        self.limpiar_grupos()
                        self.resume()
        self.minimag(events)
    
    def update(self):
        """
        Actualiza la posición del cursor, el magnificador de pantalla en caso de que este activado, los
        tooltip de los botones y animaciones o textos correspondientes.
        """
        self.raton.update()
        self.obj_magno.magnificar(self.parent.screen)
        self.grupo_botones.update(self.grupo_tooltip)
        self.anim8_0.rect.move_ip(self.tractor, 0)
        # Movimiento del tractor
        if self.anim8_0.rect.left + self.anim8_0.rect.width +100 < 0:
            self.tractor = self.tractor*-1
            self.anim8_0.image = pygame.transform.flip(self.anim8_0.image, True, False)
            self.anim8_0.image = pygame.transform.smoothscale(self.anim8_0.image, (self.anim8_0.rect.width/2, self.anim8_0.rect.height/2))
            
        if self.anim8_0.rect.left > 1124:
            self.tractor = self.tractor * -1
            self.anim8_0.image = pygame.transform.flip(self.anim8_0.image, True, False)
            self.anim8_0.image = self.anim8_0.img    
        #Automatizado del inicio de pantalla  
        if self.anim_actual == 1 and not self.parent.config.activar_lector:    
            if not self.tiempo < 1000:            
                self.grupo_fondotexto.add(self.caja_texto)
                self.grupo_palabras.add(self.texto8_2.img_palabras)
                self.txt_actual = self.texto8_2.img_palabras            
        self.tiempo += self.reloj_anim.get_time() 

    def reproducir_animacion(self, animacion):   
        """
        Gestiona la reproducción de animaciones, imágenes y texto en esta pantalla.
        @param animacion: Indica la animación que debe reproducirse.
        @type animacion: int
        """
        if animacion == 1:
            self.elemento_actual = -1
            self.grupo_fondotexto.empty()
            self.grupo_tooltip.empty()
            self.grupo_botones.remove(self.volver)
            self.grupo_palabras.empty()            
            if self.parent.config.activar_lector:
                if self.entrada_primera_vez:
                    self.spserver.processtext2(
                        self.parent.text_content["content"][self.name]["text_2"],
                        self.parent.config.activar_lector
                    )
                    self.entrada_primera_vez=False
                else:
                    self.spserver.processtext(
                        self.parent.text_content["content"][self.name]["text_2"],
                        self.parent.config.activar_lector
                    )
                self.grupo_fondotexto.add(self.caja_texto)
                self.grupo_palabras.add(self.texto8_2.img_palabras)
                self.txt_actual = self.texto8_2.img_palabras
                self.chequeo_palabra(self.txt_actual)
               
        elif animacion == 2:
            self.entrada_primera_vez=False
            self.elemento_actual = -1
            self.grupo_palabras.empty()
            self.grupo_botones.empty()
            self.grupo_botones.add(self.config, self.volver, self.sig, self.home)
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto8_3.img_palabras)
            self.txt_actual = self.texto8_3.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_3"],
                self.parent.config.activar_lector
            )
        
        elif animacion == 3:
            self.elemento_actual = -1
            self.grupo_palabras.empty()
            self.grupo_botones.empty()
            self.grupo_botones.add(self.config, self.volver, self.sig, self.home)
            self.grupo_fondotexto.add(self.caja_texto)
            self.grupo_palabras.add(self.texto8_4.img_palabras)
            self.txt_actual = self.texto8_4.img_palabras
            self.chequeo_palabra(self.txt_actual)
            self.spserver.processtext(
                self.parent.text_content["content"][self.name]["text_4"],
                self.parent.config.activar_lector
            )
            
        elif animacion ==4:
            self.limpiar_grupos()
            self.parent.changeState(pantalla9.estado(self.parent))
            
        self.chequeo_botones(self.grupo_botones)
        self.lista_final = self.lista_palabra + self.lista_botones
        self.numero_elementos = len(self.lista_final)
        
    def draw(self):
        """
        Dibuja el fondo de pantalla y los elementos pertenecientes a los grupos de sprites sobre la superficie 
        del manejador de pantallas.
        """
        self.parent.screen.blit(self.background, (0, 0))
        self.grupo_imagen.draw(self.parent.screen)
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
        self.draw_debug_rectangles()

    def ir_glosario(self):
        self.parent.pushState(pantalla10.estado(self.parent))
