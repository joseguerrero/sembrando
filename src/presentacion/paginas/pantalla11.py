#!/usr/bin/env python

import pygame
from librerias import pantalla
from librerias.boton import boton
from librerias.texto import texto
from librerias.imagen import imagen

class estado(pantalla.Pantalla):
    def __init__(self, parent):
        """
        Método inicializador de la clase. 
        
        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        """

        self.name = "screen_11"
        self.parent = parent
        self.background = pygame.image.load(self.fondos + "fondo-acc.png").convert()
        self.caja_or = imagen(self.fondos + "caja.png", 290, 125)
        self.banner_inf = imagen(self.banners + "banner-inf.png", 0, 432)
        self.banner_or = imagen(self.banners + "banner-or.png", 0, 0)
        self.banner_or_es = imagen(self.banners + "banner-or-es.png", 0, 0)
        self.banner_or_pa = imagen(self.banners + "banner-or-pa.png", 0, 0)
        self.banner_or_doc = imagen(self.banners + "banner-or-doc.png", 0, 0)
        self.cargar_botones()
        self.cargar_textos()
        self.grupo_palabras.add(self.texto11.img_palabras)
        self.grupo_banner.add(self.banner_or, self.banner_inf)
        self.grupo_botones.add(self.boton_or_ninos, self.boton_or_docentes , self.boton_or_padres, self.puerta)
        
    def cargar_textos(self):
        """
        Carga los textos utilizados en esta pantalla.
        """
        self.spserver.processtext(
            "Pantalla: Orientaciones y Sugerencias: "
            "Pulsa sobre cada botón para que puedas explorar las orientaciones y sugerencias. ", 
            self.parent.config.activar_lector
        )
        self.texto11 = texto(
            400, 
            200, 
            self.parent.text_content["content"][self.name]["text_1"],
            self.parent.config.t_fuente, 
            "instruccion",
            800
        )
        self.texto11_5_1 = texto(
            300, 
            130, 
            self.parent.text_content["content"][self.name]["text_5_1"],
            self.parent.config.t_fuente, 
            "normal",
            900
        )
        self.texto11_5_2 = texto(
            300, 
            self.texto11_5_1.y + self.texto11_5_1.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_5_2"],
            self.parent.config.t_fuente, 
            "normal",
            900
        )
        self.texto11_5_3 = texto(
            300, 
            self.texto11_5_2.y + self.texto11_5_2.ancho_final + 10,
            self.parent.text_content["content"][self.name]["text_5_3"],
            self.parent.config.t_fuente, 
            "normal",
            900
        )
        self.texto11_6_1 = texto(
            300,
            130,
            self.parent.text_content["content"][self.name]["text_6_1"],
            self.parent.config.t_fuente, 
            "normal",
            900
        )
        self.texto11_6_2 = texto(
            300,
            self.texto11_6_1.y + self.texto11_6_1.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_6_2"],
            self.parent.config.t_fuente, 
            "normal",
            900
        )
        self.texto11_6_3 = texto(
            300, 
            self.texto11_6_2.y + self.texto11_6_2.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_6_3"],
            self.parent.config.t_fuente, 
            "normal",
            900
        )
        self.texto11_7_1 = texto(
            300, 
            130, 
            self.parent.text_content["content"][self.name]["text_7_1"],
            self.parent.config.t_fuente, 
            "normal",
            900
        )
        self.texto11_7_2 = texto(
            300, 
            self.texto11_7_1.y + self.texto11_7_1.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_7_2"],
            self.parent.config.t_fuente, 
            "normal",
            900
        )
        self.texto11_7_3 = texto(
            300, 
            self.texto11_7_2.y + self.texto11_7_2.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_7_3"],
            self.parent.config.t_fuente, 
            "normal",
            900
        )
  
    def cargar_botones(self):
        """
        Carga los botones utilizados en esta pantalla.
        """
        self.boton_or_ninos = boton("or-ninos", "Orientaciones a la niña, niño y adolescente", self.botones + "boton-or-es.png", 3 ,300, 440, None, False, 1)
        self.boton_or_docentes =  boton("or-docentes", "Sugerencias pedagógicas", self.botones + "boton-or-doc.png", 3 ,500, 440, None, False, 1)
        self.boton_or_padres = boton("or-padres", "Orientaciones a la adulta y al adulto responsable", self.botones + "boton-or-pa.png", 3 ,700, 440, None, False, 1)
        self.puerta = boton("puerta", "Regresar", self.botones + "boton-puerta.png", 3, 60, 425, None, False, 1)
        
    def start(self):
        pass
 
    def cleanUp(self):
        pass
 
    def pause(self):
        pass
 
    def resume(self):
        pass
    
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
                self.lista_final = self.lista_botones
                self.numero_elementos = len(self.lista_final) 
                
                if  event.key == pygame.K_ESCAPE:
                    self.limpiar_grupos()
                    self.parent.popState()
                elif event.key == pygame.K_LEFT:
                    self.controlador_lector_evento_K_LEFT()
                    
                elif event.key == pygame.K_RIGHT:
                    self.controlador_lector_evento_K_RIGHT()
                    
                elif event.key == pygame.K_RETURN:
                    self.elemento_actual = -1
                    if self.x.tipo_objeto == "boton":
                        if self.x.id == "or-ninos":
                            self.grupo_palabras.empty()
                            self.grupo_banner.empty()
                            self.grupo_palabras.add(self.texto11_5_1.img_palabras, self.texto11_5_2.img_palabras, self.texto11_5_3.img_palabras)
                            self.caja_or.ajustar_alto(self.texto11_5_1.ancho_final + self.texto11_5_2.ancho_final + self.texto11_5_3.ancho_final + 20)
                            self.grupo_banner.add(self.banner_or_es, self.caja_or, self.banner_inf)
                            self.spserver.processtext(
                                self.parent.text_content["content"][self.name]["text_5_1l"] +
                                self.parent.text_content["content"][self.name]["text_5_2l"] +
                                self.parent.text_content["content"][self.name]["text_5_3l"] +
                                "Ahora, utiliza las teclas de dirección y explora la siguiente orientación o sugerencia. ",
                                self.parent.config.activar_lector
                            )
                            
                        elif self.x.id == "or-docentes":
                            self.grupo_palabras.empty()
                            self.grupo_banner.empty()
                            self.grupo_palabras.add(self.texto11_6_1.img_palabras, self.texto11_6_2.img_palabras, self.texto11_6_3.img_palabras)
                            self.caja_or.ajustar_alto(self.texto11_6_1.ancho_final + self.texto11_6_2.ancho_final + self.texto11_6_3.ancho_final + 20)
                            self.grupo_banner.add(self.banner_or_doc, self.caja_or, self.banner_inf)
                            
                            self.spserver.processtext(
                                self.parent.text_content["content"][self.name]["text_6_1l"] +
                                self.parent.text_content["content"][self.name]["text_6_2l"] +
                                self.parent.text_content["content"][self.name]["text_6_3l"] +
                                "Ahora, utiliza las teclas de dirección y explora la siguiente orientación o sugerencia. ",
                                self.parent.config.activar_lector
                            )
                            
                        elif self.x.id == "or-padres":
                            self.grupo_palabras.empty()
                            self.grupo_banner.empty()
                            self.grupo_palabras.add(self.texto11_7_1.img_palabras, self.texto11_7_2.img_palabras, self.texto11_7_3.img_palabras)
                            self.caja_or.ajustar_alto(self.texto11_7_1.ancho_final + self.texto11_7_2.ancho_final + self.texto11_7_3.ancho_final + 20)
                            self.grupo_banner.add(self.banner_or_pa, self.caja_or, self.banner_inf)
                            
                            self.spserver.processtext(
                                self.parent.text_content["content"][self.name]["text_7_1l"] +
                                self.parent.text_content["content"][self.name]["text_7_2l"] +
                                self.parent.text_content["content"][self.name]["text_7_3l"] +
                                "Fin de contenido, regresa al menú. ",
                                self.parent.config.activar_lector
                            )
                            
                        elif self.x.id == "puerta":
                            self.limpiar_grupos()
                            self.parent.popState()
           
            if pygame.sprite.spritecollideany(self.raton, self.grupo_botones):
                sprite = pygame.sprite.spritecollide(self.raton, self.grupo_botones, False)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if sprite[0].id == "puerta":
                        self.limpiar_grupos()
                        self.parent.popState()
                        
                    elif sprite[0].id == "or-ninos":
                        self.grupo_palabras.empty()
                        self.grupo_banner.empty()
                        self.grupo_palabras.add(self.texto11_5_1.img_palabras, self.texto11_5_2.img_palabras, self.texto11_5_3.img_palabras)
                        self.caja_or.ajustar_alto(self.texto11_5_1.ancho_final + self.texto11_5_2.ancho_final + self.texto11_5_3.ancho_final + 20)
                        self.grupo_banner.add(self.banner_or_es, self.caja_or, self.banner_inf)
                    
                    elif sprite[0].id == "or-docentes":
                        self.grupo_palabras.empty()
                        self.grupo_banner.empty()
                        self.grupo_palabras.add(self.texto11_6_1.img_palabras, self.texto11_6_2.img_palabras, self.texto11_6_3.img_palabras)
                        self.caja_or.ajustar_alto(self.texto11_6_1.ancho_final + self.texto11_6_2.ancho_final + self.texto11_6_3.ancho_final + 20)
                        self.grupo_banner.add(self.banner_or_doc, self.caja_or, self.banner_inf)
                    
                    elif sprite[0].id == "or-padres":
                        self.grupo_palabras.empty()
                        self.grupo_banner.empty()
                        self.grupo_palabras.add(self.texto11_7_1.img_palabras, self.texto11_7_2.img_palabras, self.texto11_7_3.img_palabras)
                        self.caja_or.ajustar_alto(self.texto11_7_1.ancho_final + self.texto11_7_2.ancho_final + self.texto11_7_3.ancho_final + 20)
                        self.grupo_banner.add(self.banner_or_pa, self.caja_or, self.banner_inf)
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
        self.grupo_palabras.draw(self.parent.screen)
        self.grupo_tooltip.draw(self.parent.screen)
        if self.parent.habilitar:
            self.grupo_magnificador.draw(self.parent.screen, self.enable)
        self.dibujar_rect()
