#!/usr/bin/env python

import pygame

from librerias import  pantalla
from librerias.boton import boton
from librerias.texto import texto
from librerias.imagen import imagen
from librerias.animaciones import animacion
from paginas import pantalla2

class estado(pantalla.Pantalla):
    def __init__(self, parent, previa = False):
        """
        Método inicializador de la clase. 
        
        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        @param previa: Si es True indica que esta pantalla esta apilada sobre otra. Si es False indica que esta
        pantalla fue cargada a través del método changeState del Manejador.
        @type previa: bool
        """
        self.parent = parent
        self.spserver.processtext(u"Configuración de discapacidad auditiva.", False)
        self.previa = previa
        self.fondo_acc = pygame.image.load(self.fondos + "fondo-acc.png").convert()
        self.background = self.fondo_acc
        self.velocidad = boton("velocidad", "none", self.fondos + "velocidad.png", 1,  440, 360, None, False, 1)
        self.banner_inf = imagen(self.banners + "banner-inf.png", 0, 432)
        self.banner_acc_sordo = imagen(self.banners + "banner-acc-sordo.png", 0, 0)
        self.color_mujer = animacion("mujer", self.anim + "color-mujer.png", 9, 3, 730, 160, (21, 76, 75), True, 4)
        self.color_hombre = animacion("hombre", self.anim + "color-hombre.png", 9, 3, 730, 160, (21, 76, 75), True, 4)
        self.si = boton("si", "none", self.botones + "cuadro.png", 1, 430, 120, None, False, 1)
        self.no = boton("no", "none", self.botones + "cuadro.png", 1, 545, 120, None, False, 1)
        self.check_si = boton("check_si", "none", self.botones + "cuadro-1.png" , 1, 430, 120, None, False, 1)
        self.check_no = boton("check_no", "none", self.botones + "cuadro-1.png", 1, 540, 120, None, False, 1)
        self.boton_nina = boton("nina", "none", self.botones + "cuadro.png", 1, 430, 200, None, False, 1)
        self.boton_nino = boton("nino", "none", self.botones + "cuadro.png", 1, 540, 200, None, False, 1)
        self.boton_nina_sel = boton("nina_sel", "none", self.botones + "cuadro-1.png", 1, 430, 200, None, False, 1)
        self.boton_nino_sel = boton("nino_sel", "none", self.botones + "cuadro-1.png", 1, 540, 200, None, False, 1)
        self.puerta = boton("puerta", "Regresar", self.botones + "boton-puerta.png", 3, 60, 425, None, False, 1)
        self.guardar = boton("guardar", "Guardar", self.botones + "boton-guardar.png", 3, 860, 445, None, False, 1)
        self.hoja = boton("hoja", "Velocidad", self.botones + "hoja.png", 1, 499, 370 , None, False, 1)
        self.amarillo = boton("amarillo", "Amarillo", self.botones + "amarilla.png", 1, 425 , 295, None, False, 1)
        self.rosado = boton("rosado", "Rosado", self.botones + "rosada.png", 1, 485 , 295, None, False, 1)
        self.rojo = boton("rojo", "Rojo", self.botones + "roja.png", 1, 485 , 295, None, False, 1)
        self.v_hombre = boton("v-hombre", "Verde", self.botones + "verdeh.png", 1, 545 , 295, None, False, 1)
        self.v_mujer = boton("v-mujer", "Verde", self.botones + "verdem.png", 1, 545 , 295, None, False, 1)
        self.camisas_mujer = [self.amarillo, self.rosado, self.v_mujer]
        self.camisas_hombre = [self.amarillo, self.rojo, self.v_hombre]
        self.acc2_1 = texto(310, 70, u"1.- ¿Te gustaría hacer el recorrido con un intérprete virtual? ", 20,"normal", 700)
        self.acc2_2 = texto(400, 120, u"Sí            No ", 20, "normal", 800)
        self.acc2_3 = texto(310, 150, u"2.- Selecciona el género del intérprete con el que desees hacer el recorrido. ", 20, "normal", 700)
        self.acc2_4 = texto(400, 200, u"F             M ", 20, "normal", 800)
        self.acc2_5m = texto(310, 240, u"3.- Elige el color de la camisa del intérprete virtual.  ", 20, "normal", 700)
        self.acc2_5f = texto(310, 240, u"3.- Elige el color de la camisa de la intérprete virtual.  ", 20, "normal", 700)
        self.acc2_6m = texto(310, 330, u"4.- Elige la velocidad del intérprete virtual. ", 20, "normal", 800)
        self.acc2_6f = texto(310, 330, u"4.- Elige la velocidad de la intérprete virtual. ", 20, "normal", 800)
        self.acc2_7 = texto(200, 400, u"Pulsa sobre el botón guardar para salvar tu configuración. ", 20, "normal", 800)
        self.cargar_preferencias()
            
    def start(self):
        pass
 
    def cleanUp(self):
        pass
 
    def pause(self):
        pass
 
    def resume(self):
        pass
    
    def cargar_preferencias(self):
        """
        Si existe una configuración anterior, cargara los elementos en el mismo orden y posición,
        de lo contrario cargara la posición y valor por defecto de los elementos de la pantalla.
        """
        self.grupo_palabras.add(self.acc2_1.img_palabras, self.acc2_2.img_palabras)
        self.grupo_banner.add(self.banner_acc_sordo, self.banner_inf)
        self.parent.config.consultar()
        if self.parent.config.cache == True:
            if self.parent.config.disc_audi == True:
                self.grupo_botones.add(self.no, self.check_si, self.puerta, self.guardar, self.velocidad, self.hoja)
                if self.parent.config.genero == "Mujer":
                    self.grupo_anim.add(self.color_mujer)
                    self.color_mujer.cambiar_rect(self.parent.config.color)
                    self.grupo_botones.add(self.boton_nino, self.boton_nina_sel, self.amarillo, self.rosado, self.v_mujer)
                    self.grupo_palabras.add(self.acc2_3.img_palabras, self.acc2_4.img_palabras, self.acc2_5f.img_palabras, self.acc2_6f.img_palabras, self.acc2_7.img_palabras)
                elif self.parent.config.genero == "Hombre":
                    self.grupo_anim.add(self.color_hombre)
                    self.color_hombre.cambiar_rect(self.parent.config.color)
                    self.grupo_botones.add(self.boton_nina, self.boton_nino_sel, self.amarillo, self.rojo, self.v_hombre)
                    self.grupo_palabras.add(self.acc2_3.img_palabras, self.acc2_4.img_palabras, self.acc2_5m.img_palabras, self.acc2_6m.img_palabras, self.acc2_7.img_palabras)
                self.color_hombre.cambiar_vel(self.parent.config.vel_anim)
                self.color_mujer.cambiar_vel(self.parent.config.vel_anim)
                self.hoja.mover(self.parent.config.ubx)
            elif self.parent.config.disc_audi == False:
                self.grupo_palabras.add(self.acc2_7.img_palabras)
                self.grupo_botones.add(self.si, self.check_no, self.puerta, self.guardar)
        else:
            self.parent.config.cargar_default()
            self.grupo_botones.add(self.si, self.check_no, self.puerta)
            self.hoja.mover(499)
            self.color_hombre.cambiar_vel(self.parent.config.vel_anim)
            self.color_mujer.cambiar_vel(self.parent.config.vel_anim)
            self.color_hombre.cambiar_rect(self.parent.config.color)
            self.color_mujer.cambiar_rect(self.parent.config.color)
        
    def handleEvents(self, events):
        """
        Evalúa los eventos que se generan en esta pantalla.      

        @param events: Lista de los eventos.
        @type events: list
        """ 
        for event in events:
            if event.type == pygame.QUIT:
                self.parent.quit()
                        
            if pygame.sprite.spritecollideany(self.raton, self.grupo_botones):
                sprite = pygame.sprite.spritecollide(self.raton, self.grupo_botones, False)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if sprite[0].id == "velocidad":
                        (x,_) = pygame.mouse.get_pos()
                        (posx,_,ancho,_) = self.velocidad.rect
                        (_,_, radio,_) = self.hoja.rect
                        if x > posx + (radio/2) and x < posx + ancho - radio/2:
                            factor = ((x - posx) / float(ancho - radio))
                            factor_anim = (posx + ancho - x)/8
                            ux = x - radio/2
                            self.hoja.mover(ux)
                            if factor_anim < 2:
                                factor_anim = 2
                            if factor > 1:
                                factor = 1
                            self.color_mujer.cambiar_vel(int(factor_anim))
                            self.color_hombre.cambiar_vel(int(factor_anim))
                            self.parent.config.vel_anim = factor_anim
                            self.parent.config.velocidad = factor
                            self.parent.config.ubx = ux
                            
                    elif sprite[0].id == "puerta":
                        self.limpiar_grupos()
                        self.parent.config.consultar()
                        self.parent.popState()
                            
                    elif sprite[0].id == "si":
                        self.grupo_botones.remove(self.check_no, self.si, self.guardar)
                        self.grupo_palabras.remove(self.acc2_7.img_palabras)
                        self.grupo_botones.add(self.boton_nino, self.boton_nina, self.check_si, self.no)
                        self.grupo_palabras.add(self.acc2_3.img_palabras, self.acc2_4.img_palabras)
                        self.parent.config.disc_audi = True
                                
                    elif sprite[0].id == "no":
                        self.grupo_anim.empty()
                        self.grupo_botones.remove(self.velocidad, self.hoja, self.check_si, self.no, self.boton_nino, self.boton_nina, \
                        self.boton_nina_sel, self.boton_nino_sel, self.camisas_hombre, self.camisas_mujer)
                        self.grupo_botones.add(self.check_no, self.si, self.guardar)
                        self.grupo_palabras.add(self.acc2_7.img_palabras)
                        self.grupo_palabras.remove(self.acc2_3.img_palabras, self.acc2_4.img_palabras,
                        self.acc2_5f.img_palabras, self.acc2_6f.img_palabras, self.acc2_5m.img_palabras, self.acc2_6m.img_palabras)
                        self.parent.config.disc_audi = False
                                
                    elif sprite[0].id == "nino":
                        self.grupo_anim.empty()
                        self.grupo_palabras.remove(self.acc2_5f.img_palabras, self.acc2_5f.img_palabras,
                                                               self.acc2_6f.img_palabras, self.acc2_5f.img_palabras)
                        self.grupo_anim.add(self.color_hombre)
                        self.color_hombre.detener()
                        self.grupo_palabras.add(self.acc2_5m.img_palabras, self.acc2_7.img_palabras)
                        self.grupo_palabras.remove(self.acc2_6m.img_palabras)
                        self.grupo_botones.remove(self.velocidad, self.hoja, self.camisas_mujer, self.boton_nino, self.boton_nina_sel)
                        self.grupo_botones.add(self.boton_nino_sel, self.boton_nina, self.guardar, self.camisas_hombre)
                        self.parent.config.genero = "Hombre"
                                                                                               
                    elif sprite[0].id == "nina":
                        self.grupo_anim.empty()
                        self.grupo_palabras.remove(self.acc2_5m.img_palabras, self.acc2_5m.img_palabras,
                                                               self.acc2_6m.img_palabras, self.acc2_5m.img_palabras)
                        self.grupo_anim.add(self.color_mujer)
                        self.color_mujer.detener()
                        self.grupo_palabras.add(self.acc2_5f.img_palabras, self.acc2_7.img_palabras)
                        self.grupo_palabras.remove(self.acc2_6m.img_palabras)
                        self.grupo_botones.remove(self.velocidad, self.hoja, self.camisas_hombre, self.boton_nina, self.boton_nino_sel)
                        self.grupo_botones.add(self.boton_nina_sel, self.boton_nino, self.guardar, self.camisas_mujer)
                        self.parent.config.genero = "Mujer"
                            
                    elif sprite[0].id == "amarillo":
                        self.grupo_anim.empty()
                        self.grupo_botones.add(self.velocidad, self.hoja)
                        self.grupo_palabras.remove(self.acc2_6f.img_palabras, self.acc2_6m.img_palabras)
                        if self.parent.config.genero == "Mujer":
                            self.grupo_palabras.add(self.acc2_6f.img_palabras)
                            self.grupo_anim.add(self.color_mujer)
                            self.color_mujer.cambiar_rect(0)
                            self.parent.config.color = self.color_mujer.fila_pos
                            self.color_mujer.continuar()
                        else:
                            self.grupo_palabras.add(self.acc2_6m.img_palabras)
                            self.grupo_anim.add(self.color_hombre)
                            self.color_hombre.cambiar_rect(0)
                            self.parent.config.color = self.color_hombre.fila_pos
                            self.color_hombre.continuar()
                                
                    elif sprite[0].id == "rojo":
                        self.grupo_anim.empty()
                        self.grupo_palabras.remove(self.acc2_6f.img_palabras)
                        self.grupo_botones.add(self.velocidad, self.hoja)
                        self.grupo_anim.add(self.color_hombre)
                        self.grupo_palabras.add(self.acc2_6m.img_palabras)
                        self.color_hombre.cambiar_rect(1)
                        self.parent.config.color = self.color_hombre.fila_pos
                        self.color_hombre.continuar()
                                
                    elif sprite[0].id == "rosado":
                        self.grupo_anim.empty()
                        self.grupo_palabras.remove(self.acc2_6m.img_palabras)
                        self.grupo_botones.add(self.velocidad, self.hoja)
                        self.grupo_anim.add(self.color_mujer)
                        self.grupo_palabras.add(self.acc2_6f.img_palabras)
                        self.color_mujer.cambiar_rect(1)
                        self.parent.config.color = self.color_mujer.fila_pos
                        self.color_mujer.continuar()
                                
                    elif sprite[0].id == "v-hombre":
                        self.grupo_anim.empty()
                        self.grupo_palabras.remove(self.acc2_6f.img_palabras)
                        self.grupo_botones.add(self.velocidad, self.hoja)
                        self.grupo_anim.add(self.color_hombre)
                        self.grupo_palabras.add(self.acc2_6m.img_palabras)
                        self.color_hombre.cambiar_rect(2)
                        self.parent.config.color = self.color_hombre.fila_pos
                        self.color_hombre.continuar()
                                
                    elif sprite[0].id == "v-mujer":
                        self.grupo_anim.empty()
                        self.grupo_palabras.remove(self.acc2_6f.img_palabras)
                        self.grupo_botones.add(self.velocidad, self.hoja)
                        self.grupo_anim.add(self.color_mujer)
                        self.grupo_palabras.add(self.acc2_6f.img_palabras)
                        self.color_mujer.cambiar_rect(2)
                        self.parent.config.color = self.color_mujer.fila_pos
                        self.color_mujer.continuar()
                                                                       
                    elif sprite[0].id == "guardar":
                        if self.parent.config.velocidad == 0.5 and self.parent.config.vel_anim ==  4:
                            self.parent.config.ubx = self.hoja.x
                        self.parent.config.cache = True
                        if self.parent.config.t_fuente != self.parent.config.preferencias["t_fuente"]:
                            self.parent.config.texto_cambio = True
                        self.parent.config.guardar_preferencias()
                        self.limpiar_grupos()
                        if self.parent.primera_vez:
                            self.parent.changeState(pantalla2.estado(self.parent))
                        else:
                            if self.previa:
                                self.parent.VOLVER_PANTALLA_PREVIA = True
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
        self.grupo_anim.draw(self.parent.screen)
        self.grupo_banner.draw(self.parent.screen)
        self.grupo_botones.draw(self.parent.screen)
        self.grupo_palabras.draw(self.parent.screen)
        self.grupo_tooltip.draw(self.parent.screen)
        if self.parent.habilitar:
            self.grupo_magnificador.draw(self.parent.screen, self.enable)
        self.dibujar_rect()