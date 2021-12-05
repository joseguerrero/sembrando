#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from librerias import pantalla
from librerias.boton import boton
from librerias.texto import texto
from librerias.popups import PopUp
from librerias.imagen import imagen

from librerias.imgfondo import fondo
from librerias.pixelperfect import *
from librerias.textopopups import p9
from librerias.objmask import object_mask
from paginas import menucfg
from paginas import pantalla2
from paginas import pantalla8
from paginas import pantalla10

class estado(pantalla.Pantalla):
    def __init__(self, parent):
        """
        Método inicializador de la clase. 
        
        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        """

        self.name = "screen_9"
        self.parent = parent
        self.previa = True
        self.deteccion_movimiento = False
        self.fondo_texto = False
        self.background = pygame.image.load(self.fondos + "fondo-mapa2.png")
        self.banner_siembra = imagen(self.banners + "banner-siembra.png", 0, 0)
        self.banner_inf = imagen(self.banners + "banner-inf.png", 0, 432)
        self.mouse = object_mask("Cursor", 850, 512, self.varios + "puntero.png")
        # Para mantener las piezas del mapa bien ubicadas no se deben modificar los valores x e y de las regiones, solo de zulia.         
        self.zulia = object_mask(u"región zuliana", 13, 140, self.varios + "zulia-des.png", self.varios + "zulia-act.png")
        self.occ = object_mask(u"región occidental", self.zulia.rect.left + 55, self.zulia.rect.top - 6, self.varios + "occ-des.png", self.varios + "occ-act.png")
        self.central = object_mask(u"región central", self.zulia.rect.left + 115, self.zulia.rect.top + 37, self.varios + "central-des.png", self.varios + "central-act.png")
        self.capital = object_mask(u"región capital", self.zulia.rect.left + 152, self.zulia.rect.top + 32, self.varios + "capital-des.png", self.varios + "capital-act.png")
        self.ori = object_mask(u"región nor oriental", self.zulia.rect.left +195, self.zulia.rect.top + 29, self.varios + "ori-des.png", self.varios + "ori-act.png")
        self.andes = object_mask(u"región los andes", self.zulia.rect.left + 23, self.zulia.rect.top + 48, self.varios + "andes-des.png", self.varios + "andes-act.png")
        self.llanos = object_mask(u"región los llanos", self.zulia.rect.left + 26, self.zulia.rect.top + 47, self.varios + "llanos-des.png", self.varios + "llanos-act.png")
        self.guayana = object_mask(u"región guayana", self.zulia.rect.left + 140, self.zulia.rect.top + 48, self.varios + "guayana-des.png", self.varios + "guayana-act.png")
        self.insu = object_mask(u"región insular", self.zulia.rect.left + 149, self.zulia.rect.top - 6, self.varios + "insular-des.png", self.varios + "insular-act.png")
        self.limites1 = pygame.image.load(self.varios + "limitemar.png").convert_alpha()
        self.limites2 = pygame.image.load(self.varios + "limitemar2.png").convert_alpha()
        self.zona_r = pygame.image.load(self.varios + "zona-recla.png").convert_alpha()
        self.n_estados = pygame.image.load(self.varios + "nombre-estados.png").convert_alpha()
        self.cargar_botones()
        self.cargar_textos()
        self.resume()
        self.bg = fondo(573, 377)
    
    def cargar_textos(self):
        """
        Carga los textos utilizados en esta pantalla.
        """
        self.texto9_2_1 = texto(
            490,
            60, 
            self.parent.text_content["content"][self.name]["text_2_1"] , 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_2_2 = texto(
            490,
            self.texto9_2_1.y + self.texto9_2_1.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_2_2"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_2_3 = texto(
            490,
            self.texto9_2_2.y + self.texto9_2_2.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_2_3"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_2_4 = texto(
            490,
            self.texto9_2_3.y + self.texto9_2_3.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_2_4"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        
        self.texto9_3_1 = texto(
            490,
            60, 
            self.parent.text_content["content"][self.name]["text_3_1"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_3_2 = texto(
            490,
            self.texto9_3_1.y + self.texto9_3_1.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_3_2"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_3_3 = texto(
            490,
            self.texto9_3_2.y + self.texto9_3_2.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_3_3"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        
        self.texto9_4_1 = texto(
            490,
            60, 
            self.parent.text_content["content"][self.name]["text_4_1"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_4_2 = texto(
            490,
            self.texto9_4_1.y + self.texto9_4_1.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_4_2"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_4_3 = texto(
            490,
            self.texto9_4_2.y + self.texto9_4_2.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_4_3"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        
        self.texto9_5_1 = texto(
            490,
            60, 
            self.parent.text_content["content"][self.name]["text_5_1"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_5_2 = texto(
            490,
            self.texto9_5_1.y + self.texto9_5_1.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_5_2"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_5_3 = texto(
            490,
            self.texto9_5_2.y + self.texto9_5_2.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_5_3"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_6_1 = texto(
            490,
            60, 
            self.parent.text_content["content"][self.name]["text_6_1"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_6_2 = texto(
            490,
            self.texto9_6_1.y + self.texto9_6_1.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_6_2"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_6_3 = texto(
            490,
            self.texto9_6_2.y + self.texto9_6_2.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_6_3"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        
        self.texto9_7_1 = texto(
            490,
            60, 
            self.parent.text_content["content"][self.name]["text_7_1"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_7_2 = texto(
            490,
            self.texto9_7_1.y + self.texto9_7_1.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_7_2"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_7_3 = texto(
            490,
            self.texto9_7_2.y + self.texto9_7_2.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_7_3"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        
        self.texto9_8_1 = texto(
            490,
            60, 
            self.parent.text_content["content"][self.name]["text_8_1"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_8_2 = texto(
            490,
            self.texto9_8_1.y + self.texto9_8_1.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_8_2"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_8_3 = texto(
            490,
            self.texto9_8_2.y + self.texto9_8_2.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_8_3"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        
        self.texto9_9_1 = texto(
            490,
            60, 
            self.parent.text_content["content"][self.name]["text_9_1"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_9_2 = texto(
            490,
            self.texto9_9_1.y + self.texto9_9_1.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_9_2"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_9_3 = texto(
            490,
            self.texto9_9_2.y + self.texto9_9_2.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_9_3"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        
        self.texto9_10_1 = texto(
            490,
            60, 
            self.parent.text_content["content"][self.name]["text_10_1"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_10_2 = texto(
            490,
            self.texto9_10_1.y + self.texto9_10_1.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_10_2"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_10_3 = texto(
            490,
            self.texto9_10_2.y + self.texto9_10_2.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_10_3"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        self.texto9_10_4 = texto(
            490,
            self.texto9_10_3.y + self.texto9_10_3.ancho_final + 10, 
            self.parent.text_content["content"][self.name]["text_10_4"], 
            self.parent.config.t_fuente, 
            "normal", 
            1000
        )
        
        self.popup_ins1 = PopUp(self.parent, (p9["texto1"] , ), "", None , self.grupo_popup, 1, 750, 400, -100)
        self.popup_ins1.agregar_grupo()
        
    def cargar_botones(self):    
        """
        Carga los botones utilizados en esta pantalla.
        """
        self.home = boton("home", "Menú", self.botones + "boton-menu.png", 3, 889, 440, None, False, 1)
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
        self.popup_ins1.agregar_grupo()
        self.capital.apagar()
        self.ori.apagar()
        self.zulia.apagar()
        self.occ.apagar()
        self.andes.apagar()
        self.llanos.apagar()
        self.central.apagar()
        self.guayana.apagar()
        self.grupo_banner.add(self.banner_siembra, self.banner_inf)
        self.grupo_botones.add(self.config, self.volver, self.home)
        self.grupo_mapa.add(self.zulia, self.occ, self.central, self.insu, self.capital, self.ori, self.andes, self.llanos, self.guayana)
        self.spserver.processtext(
            u"Pantalla: La Agricultura en Venezuela: ", 
            self.parent.config.activar_lector
        )        
        self.spserver.processtext(
            p9["lector1"], 
            self.parent.config.activar_lector
        )
        
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
                self.chequeo_mascaras(self.grupo_mapa)
                self.chequeo_botones(self.grupo_botones)
                self.lista_final = self.lista_palabra + self.lista_mascaras + self.lista_botones
                self.numero_elementos = len(self.lista_final)
                
                if event.key == pygame.K_RIGHT:
                    self.fondo_texto = False
                    self.grupo_palabras.empty()
                    self.deteccion_movimiento = True
                    self.controlador_lector_evento_K_RIGHT()
                    
                elif event.key == pygame.K_LEFT:
                    self.fondo_texto = False
                    self.grupo_palabras.empty()
                    self.controlador_lector_evento_K_LEFT()
                    
                if self.deteccion_movimiento:
                    if event.key == pygame.K_RETURN:
                        if self.x.tipo_objeto == "mapa":
                            self.fondo_texto = True
                            
                            if self.x.id == u"región capital":
                                self.grupo_palabras.empty()
                                self.central.apagar()
                                self.llanos.apagar()
                                self.zulia.apagar()
                                self.ori.apagar()
                                self.occ.apagar()
                                self.andes.apagar()
                                self.llanos.apagar()
                                self.capital.iluminar()
                                self.insu.apagar()
                                self.grupo_palabras.add(self.texto9_2_1.img_palabras, self.texto9_2_2.img_palabras, self.texto9_2_3.img_palabras, self.texto9_2_4.img_palabras)
                                self.spserver.processtext(
                                    self.parent.text_content["content"][self.name]["text_2_1l"] +  self.texto9_2_2.texto + self.texto9_2_3.texto + self.texto9_2_4.texto, 
                                    self.parent.config.activar_lector
                                )
                                                      
                            elif self.x.id == u"región central":
                                self.grupo_palabras.empty()
                                self.capital.apagar()
                                self.llanos.apagar()
                                self.zulia.apagar()
                                self.ori.apagar()
                                self.occ.apagar()
                                self.andes.apagar()
                                self.llanos.apagar()
                                self.central.iluminar()
                                self.insu.apagar()
                                self.grupo_palabras.add(self.texto9_3_1.img_palabras, self.texto9_3_2.img_palabras, self.texto9_3_3.img_palabras)
                                self.spserver.processtext(
                                    self.parent.text_content["content"][self.name]["text_3_1l"] + self.texto9_3_2.texto + self.texto9_3_3.texto, 
                                    self.parent.config.activar_lector
                                )
                                
                            if self.x.id == u"región los llanos":
                                self.grupo_palabras.empty()
                                self.capital.apagar()
                                self.central.apagar()
                                self.ori.apagar()
                                self.zulia.apagar()
                                self.occ.apagar()
                                self.andes.apagar()
                                self.llanos.iluminar()
                                self.insu.apagar()
                                self.grupo_palabras.add(self.texto9_4_1.img_palabras, self.texto9_4_2.img_palabras, self.texto9_4_3.img_palabras)
                                self.spserver.processtext(
                                    self.parent.text_content["content"][self.name]["text_4_1l"] +  self.texto9_4_2.texto + self.texto9_4_3.texto, 
                                    self.parent.config.activar_lector
                                )
                                
                            if self.x.id == u"región occidental":
                                self.grupo_palabras.empty()
                                self.capital.apagar()
                                self.llanos.apagar()
                                self.central.apagar()
                                self.ori.apagar()
                                self.zulia.apagar()
                                self.andes.apagar()
                                self.occ.iluminar()
                                self.llanos.apagar()
                                self.guayana.apagar()
                                self.insu.apagar()
                                self.grupo_palabras.add(self.texto9_5_1.img_palabras, self.texto9_5_2.img_palabras, self.texto9_5_3.img_palabras)
                                self.spserver.processtext(
                                    self.parent.text_content["content"][self.name]["text_5_1l"] + self.texto9_5_2.texto + self.texto9_5_3.texto, 
                                    self.parent.config.activar_lector
                                )
                                
                            if self.x.id == u"región zuliana":
                                self.grupo_palabras.empty()
                                self.capital.apagar()
                                self.llanos.apagar()
                                self.central.apagar()
                                self.ori.apagar()
                                self.zulia.iluminar()
                                self.occ.apagar()
                                self.andes.apagar()
                                self.llanos.apagar()
                                self.guayana.apagar()
                                self.insu.apagar()
                                self.grupo_palabras.add(self.texto9_6_1.img_palabras, self.texto9_6_2.img_palabras, self.texto9_6_3.img_palabras)
                                self.spserver.processtext(
                                    self.parent.text_content["content"][self.name]["text_6_1l"] + self.texto9_6_2.texto + self.texto9_6_3.texto, 
                                    self.parent.config.activar_lector
                                )
                                
                            if self.x.id == u"región los andes":
                                self.grupo_palabras.empty()
                                self.capital.apagar()
                                self.llanos.apagar()
                                self.central.apagar()
                                self.zulia.apagar()
                                self.ori.apagar()
                                self.occ.apagar()
                                self.andes.iluminar()
                                self.llanos.apagar()
                                self.guayana.apagar()
                                self.insu.apagar()
                                self.grupo_palabras.add(self.texto9_7_1.img_palabras, self.texto9_7_2.img_palabras, self.texto9_7_3.img_palabras)
                                self.spserver.processtext(
                                    self.parent.text_content["content"][self.name]["text_7_1l"] + self.texto9_7_2.texto + self.texto9_7_3.texto, 
                                    self.parent.config.activar_lector
                                )
                                
                            if self.x.id == u"región nor oriental":
                                self.grupo_palabras.empty()
                                self.capital.apagar()
                                self.llanos.apagar()
                                self.central.apagar()
                                self.ori.iluminar()
                                self.zulia.apagar()
                                self.occ.apagar()
                                self.andes.apagar()
                                self.guayana.apagar()
                                self.insu.apagar()
                                self.grupo_palabras.add(self.texto9_8_1.img_palabras, self.texto9_8_2.img_palabras, self.texto9_8_3.img_palabras)
                                self.spserver.processtext(
                                    self.parent.text_content["content"][self.name]["text_8_1l"] + self.texto9_8_2.texto + self.texto9_8_3.texto, 
                                    self.parent.config.activar_lector
                                )
                            
                            if self.x.id == u"región guayana":
                                self.grupo_palabras.empty()
                                self.capital.apagar()
                                self.llanos.apagar()
                                self.central.apagar()
                                self.ori.apagar()
                                self.occ.apagar()
                                self.zulia.apagar()
                                self.andes.apagar()
                                self.llanos.apagar()
                                self.insu.apagar()
                                self.guayana.iluminar()
                                self.grupo_palabras.add(self.texto9_9_1.img_palabras, self.texto9_9_2.img_palabras, self.texto9_9_3.img_palabras)
                                self.spserver.processtext(
                                    self.parent.text_content["content"][self.name]["text_9_1l"] + self.texto9_9_2.texto + self.texto9_9_3.texto, 
                                    self.parent.config.activar_lector
                                )
                                
                                
                            if self.x.id == u"región insular":
                                self.grupo_palabras.empty()
                                self.capital.apagar()
                                self.llanos.apagar()
                                self.central.apagar()
                                self.ori.apagar()
                                self.occ.apagar()
                                self.zulia.apagar()
                                self.andes.apagar()
                                self.llanos.apagar()
                                self.guayana.apagar()
                                self.insu.iluminar()
                                self.grupo_palabras.add(self.texto9_10_1.img_palabras, self.texto9_10_2.img_palabras, self.texto9_10_3.img_palabras, self.texto9_10_4.img_palabras )
                                self.spserver.processtext(
                                    self.parent.text_content["content"][self.name]["text_10_1l"] + self.texto9_10_2.texto + self.texto9_10_3.texto + self.texto9_10_4.texto, 
                                    self.parent.config.activar_lector
                                )
                    
                        elif self.x.tipo_objeto == "boton":
                            if self.x.id == "volver":
                                self.limpiar_grupos()
                                self.parent.animacion = 3         
                                self.parent.changeState(pantalla8.estado(self.parent, 3))   
                                                         
                            elif self.x.id == "config":
                                self.limpiar_grupos()
                                self.parent.pushState(menucfg.estado(self.parent, self.previa))  
                                
                            elif self.x.id == "home":
                                self.limpiar_grupos()
                                self.parent.changeState(pantalla2.estado(self.parent))
                    
            lista = spritecollide_pp(self.mouse, self.grupo_mapa)         
            if not lista == []:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.deteccion_movimiento = False
                    self.fondo_texto = True
                    if lista[0].id == u"región capital":
                        self.central.apagar()
                        self.llanos.apagar()
                        self.ori.apagar()
                        self.occ.apagar()
                        self.zulia.apagar()
                        self.andes.apagar()
                        self.llanos.apagar()
                        self.capital.iluminar()
                        self.insu.apagar()
                        self.grupo_palabras.empty()
                        self.grupo_palabras.add(self.texto9_2_1.img_palabras, self.texto9_2_2.img_palabras, self.texto9_2_3.img_palabras , self.texto9_2_4.img_palabras)
                            
                    if lista[0].id == u"región central":
                        self.capital.apagar()
                        self.llanos.apagar()
                        self.ori.apagar()
                        self.occ.apagar()
                        self.zulia.apagar()
                        self.andes.apagar()
                        self.llanos.apagar()
                        self.central.iluminar()
                        self.insu.apagar()
                        self.grupo_palabras.empty()
                        self.grupo_palabras.add(self.texto9_3_1.img_palabras, self.texto9_3_2.img_palabras, self.texto9_3_3.img_palabras)
                            
                    if lista[0].id == u"región los llanos":
                        self.capital.apagar()
                        self.central.apagar()
                        self.llanos.iluminar()
                        self.zulia.apagar()
                        self.ori.apagar()
                        self.occ.apagar()
                        self.andes.apagar()
                        self.insu.apagar()
                        self.grupo_palabras.empty()
                        self.grupo_palabras.add(self.texto9_4_1.img_palabras, self.texto9_4_2.img_palabras, self.texto9_4_3.img_palabras)
                        
                    if lista[0].id == u"región occidental":
                        self.capital.apagar()
                        self.llanos.apagar()
                        self.ori.apagar()
                        self.central.apagar()
                        self.zulia.apagar()
                        self.occ.iluminar()
                        self.llanos.apagar()
                        self.guayana.apagar()
                        self.andes.apagar()
                        self.insu.apagar()
                        self.grupo_palabras.empty()
                        self.grupo_palabras.add(self.texto9_5_1.img_palabras, self.texto9_5_2.img_palabras, self.texto9_5_3.img_palabras)
                    
                    if lista[0].id == u"región zuliana":
                        self.capital.apagar()
                        self.llanos.apagar()
                        self.central.apagar()
                        self.ori.apagar()
                        self.zulia.iluminar()
                        self.occ.apagar()
                        self.andes.apagar()
                        self.llanos.apagar()
                        self.guayana.apagar()
                        self.insu.apagar()
                        self.grupo_palabras.empty()
                        self.grupo_palabras.add(self.texto9_6_1.img_palabras, self.texto9_6_2.img_palabras, self.texto9_6_3.img_palabras)
                    
                    if lista[0].id == u"región los andes":
                        self.capital.apagar()
                        self.llanos.apagar()
                        self.central.apagar()
                        self.guayana.apagar()
                        self.zulia.apagar()
                        self.ori.apagar()
                        self.occ.apagar()
                        self.andes.iluminar()
                        self.llanos.apagar()
                        self.insu.apagar()
                        self.grupo_palabras.empty()
                        self.grupo_palabras.add(self.texto9_7_1.img_palabras, self.texto9_7_2.img_palabras, self.texto9_7_3.img_palabras)
                        
                    if lista[0].id == u"región nor oriental":
                        self.capital.apagar()
                        self.central.apagar()
                        self.ori.iluminar()
                        self.llanos.apagar()
                        self.guayana.apagar()
                        self.zulia.apagar()
                        self.occ.apagar()
                        self.andes.apagar()
                        self.insu.apagar()
                        self.grupo_palabras.empty()
                        self.grupo_palabras.add(self.texto9_8_1.img_palabras, self.texto9_8_2.img_palabras, self.texto9_8_3.img_palabras)
                        
                    if lista[0].id == u"región guayana":
                        self.capital.apagar()
                        self.llanos.apagar()
                        self.central.apagar()
                        self.ori.apagar()
                        self.zulia.apagar()
                        self.occ.apagar()
                        self.andes.apagar()
                        self.guayana.iluminar()
                        self.insu.apagar()
                        self.grupo_palabras.empty()
                        self.grupo_palabras.add(self.texto9_9_1.img_palabras, self.texto9_9_2.img_palabras, self.texto9_9_3.img_palabras)
                    
                    if lista[0].id == u"región insular":
                        self.capital.apagar()
                        self.llanos.apagar()
                        self.central.apagar()
                        self.ori.apagar()
                        self.zulia.apagar()
                        self.occ.apagar()
                        self.andes.apagar()
                        self.guayana.apagar()
                        self.insu.iluminar()
                        self.grupo_palabras.empty()
                        self.grupo_palabras.add(self.texto9_10_1.img_palabras, self.texto9_10_2.img_palabras, self.texto9_10_3.img_palabras, self.texto9_10_4.img_palabras)
                    
                    
            elif not self.deteccion_movimiento:
                self.fondo_texto = False
                self.capital.apagar()
                self.central.apagar()
                self.guayana.apagar()
                self.andes.apagar()
                self.zulia.apagar()
                self.occ.apagar()
                self.ori.apagar()
                self.llanos.apagar()
                self.grupo_palabras.empty()
                self.grupo_fondotexto.empty()
                
            if pygame.sprite.spritecollideany(self.raton, self.grupo_botones):
                sprite = pygame.sprite.spritecollide(self.raton, self.grupo_botones, False)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if sprite[0].id == "volver":
                        self.limpiar_grupos()
                        self.parent.animacion = 3         
                        self.parent.changeState(pantalla8.estado(self.parent, 3))
                    
                    elif sprite[0].id == "config":
                        self.limpiar_grupos()
                        self.parent.pushState(menucfg.estado(self.parent, self.previa))
                    
                    elif sprite[0].id == "home":
                        self.limpiar_grupos()
                        self.parent.changeState(pantalla2.estado(self.parent))
        self.minimag(events)

    def update(self):
        """
        Actualiza la posición del cursor, el magnificador de pantalla en caso de que este activado, los
        tooltip de los botones y animaciones o textos correspondientes.
        """
        self.raton.update()
        self.obj_magno.magnificar(self.parent.screen)
        self.grupo_botones.update(self.grupo_tooltip)
        self.mouse.rect.center = pygame.mouse.get_pos()
        
    def draw(self):
        """
        Dibuja el fondo de pantalla y los elementos pertenecientes a los grupos de sprites sobre la superficie 
        del manejador de pantallas.
        """
        self.parent.screen.blit(self.background, (0, 0))
        self.grupo_banner.draw(self.parent.screen)
        self.parent.screen.blit(self.zona_r, (320, 233))
        self.parent.screen.blit(self.limites1, (50, 60))
        self.parent.screen.blit(self.limites2, (305, 145))
        self.grupo_mapa.draw(self.parent.screen)
        self.grupo_popup.draw(self.parent.screen)
        if self.fondo_texto:
            self.parent.screen.blit(self.bg.img, (451, 55))
        self.grupo_botones.draw(self.parent.screen)
        self.grupo_fondotexto.draw(self.parent.screen)
        self.grupo_palabras.draw(self.parent.screen)
        self.grupo_tooltip.draw(self.parent.screen)
        
        self.parent.screen.blit(self.n_estados, (40, 95))
        if self.parent.habilitar:
            self.grupo_magnificador.draw(self.parent.screen, self.enable)
        if self.deteccion_movimiento:
            self.dibujar_rect()
    
    def ir_glosario(self):
        self.parent.pushState(pantalla10.estado(self.parent))
