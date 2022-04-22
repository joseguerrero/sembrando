#!/usr/bin/env python

import pygame

from librerias import pantalla
from librerias.textopopups import p1_vis
from librerias.button import Button
from librerias.texto import texto
from librerias.popups import PopUp
from librerias.image import Image
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
        self.previa = previa
        self.fondo_acc = pygame.image.load(self.fondos + "fondo-acc-visual.png").convert()
        self.background = self.fondo_acc
        self.banner_inf = Image(0, 432, self.banners + "banner-inf.png")
        self.banner_acc_visual = Image(0, 0, self.banners + "banner-acc-visual.png")
        self.puerta = Button(60, 425, "puerta", "Regresar", self.botones + "boton-puerta.png", 3, None, False, 1)
        self.guardar = Button(860, 445, "guardar", "Guardar", self.botones + "boton-guardar.png", 3, None, False, 1)
        
        # Botones magnificador
        self.img1 = pygame.image.load(self.pops + "f5.png").convert_alpha()
        self.img2 = pygame.image.load(self.pops + "mas.png").convert_alpha()
        self.img3 = pygame.image.load(self.pops + "menos.png").convert_alpha()
        cont_img = {"F5": self.img1, "MAS": self.img2, "MENOS": self.img3}
        self.onmag = Button(130, 120, "onmag", "none", self.botones + "cuadro.png", 1, None, False, 1)
        self.onmag_si = Button(130, 120, "onmag-si", "none", self.botones + "cuadro-1.png", 1, None, False, 1)
        self.offmag = Button(245, 120, "offmag", "none", self.botones + "cuadro.png", 1, None, False, 1)
        self.offmag_si = Button(245, 120, "offmag-si", "none", self.botones + "cuadro-1.png", 1, None, False, 1)
        self.popup_mag = PopUp(parent, p1_vis["texto_mag"], "", cont_img , self.grupo_popup, 2, 730, 230, -50)
        
        # Botones tamaño de letra
        self.tam18 = Button(130, 200, "18", "none", self.botones + "cuadro.png", 1, None, False, 1)
        self.tam18_sel = Button(130, 200, "18-si", "none", self.botones + "cuadro-1.png", 1, None, False, 1)
        self.tam20 = Button(210, 200, "20", "none", self.botones + "cuadro.png", 1, None, False, 1)
        self.tam20_sel = Button(210, 200, "20-si", "none", self.botones + "cuadro-1.png", 1, None, False, 1)
        self.tam22 = Button(290, 200, "22", "none", self.botones + "cuadro.png", 1, None, False, 1)
        self.tam22_sel = Button(290, 200, "22-si", "none", self.botones + "cuadro-1.png", 1, None, False, 1)
        
        # Botones Sintetizador de voz
        self.lector = Button(130, 295, "lector", "none", self.botones + "cuadro.png", 1, None, False, 1)
        self.lector_si =Button(130, 295, "lector-si", "none", self.botones + "cuadro-1.png", 1, None, False, 1)
        self.oflector = Button(245, 295, "oflector", "none", self.botones + "cuadro.png", 1, None, False, 1)
        self.oflector_si = Button(245, 295, "oflector-si", "none", self.botones + "cuadro-1.png", 1, None, False, 1)
        
        # Botones audio
        self.vbaja = Button(93, 390, "vbaja", "none", self.botones + "cuadro.png", 1, None, False, 1)
        self.vbaja_sel = Button(93, 390, "vbaja-si", "none", self.botones + "cuadro-1.png", 1, None, False, 1)
        self.vmedia = Button(208, 390, "vmedia", "none", self.botones + "cuadro.png", 1, None, False, 1)
        self.vmedia_sel = Button(208, 390, "vmedia-si", "none", self.botones + "cuadro-1.png", 1, None, False, 1)
        self.vrapida = Button(332, 390, "vrapida", "none", self.botones + "cuadro.png", 1, None, False, 1)
        self.vrapida_sel = Button(332, 390, "vrapida-si", "none", self.botones + "cuadro-1.png", 1, None, False, 1)
        
        # Configuracion accesibilidad visual textos
        self.acc3_1 = texto(10, 70, u"1.- ¿Te gustaría hacer el recorrido con un Magnificador de Pantalla? ", 20, "normal", 400)
        self.acc3_2 = texto(100, 120, u"Sí             No ", 20, "normal", 500)
        self.acc3_3 = texto(10, 250, u"3.- ¿Deseas activar el lector de pantalla? ", 20, "normal", 400)
        self.acc3_4 = texto(100, 300, u"Sí             No ", 20, "normal", 500)
        self.acc3_5 = texto(10, 340, u"4.- Elije la velocidad del lector de pantalla. ", 20, "normal", 400)
        self.acc3_6 = texto(40, 390, u"Lenta         Media         Rápida ", 20, "normal", 500)
        self.acc3_7 = texto(200, 400, u"Pulsa sobre el botón guardar para salvar tu configuración. ", 20, "normal", 500)
        self.acc3_8 = texto(10, 160, u"2.- Elige el tamaño de la letra. ", 20,"normal", 400)
        self.acc3_9 = texto(100, 200, u"18         20        22 ", 20, "normal", 400)
        instrucciones = u"Pantalla: Discapacidad visual: Instrucciones: pulsa las teclas uno, 2, o 3, para seleccionar la opcion de tu preferencia, en cada una de las siguientes preguntas, o pulsa la tecla escape para volver al menú: "
        self.pregunta1 = u"¿Deseas activar el lector de pantalla? Si deseas activarlo presiona uno. Si no deseas activarlo pulsa 2. "
        self.pregunta2 = u"Elige la velocidad del lector de pantalla: Si deseas velocidad lenta, pulsa uno. Velocidad media, pulsa 2. Velocidad rápida, pulsa 3."
        self.cargar_preferencias()
        self.spserver.stopserver()
        self.opcion = 1
        self.spserver.processtext(instrucciones + self.pregunta1, True)
        
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
        self.grupo_palabras.add(self.acc3_1.img_palabras, self.acc3_2.img_palabras, self.acc3_3.img_palabras, self.acc3_4.img_palabras, self.acc3_8.img_palabras, self.acc3_9.img_palabras)
        self.grupo_banner.add(self.banner_acc_visual, self.banner_inf)
        self.parent.config.consultar()
        if self.parent.config.cache == True:
            self.grupo_botones.add(self.puerta)
            if self.parent.config.magnificador:
                self.grupo_botones.add(self.onmag_si, self.offmag)
                self.popup_mag.agregar_grupo()
            else:
                self.grupo_botones.add(self.onmag, self.offmag_si)                                 
                self.popup_mag.eliminar_grupo()
                
            if self.parent.config.t_fuente == 18:
                self.grupo_botones.add(self.tam18_sel, self.tam20, self.tam22)
            elif self.parent.config.t_fuente == 20:
                self.grupo_botones.add(self.tam18, self.tam20_sel, self.tam22)
            elif self.parent.config.t_fuente == 22:
                self.grupo_botones.add(self.tam18, self.tam20, self.tam22_sel)
            
            if self.parent.config.activar_lector == True:
                self.grupo_botones.add(self.lector_si, self.oflector)
                self.grupo_palabras.add(self.acc3_5.img_palabras, self.acc3_6.img_palabras)
                if self.parent.config.synvel == "baja":
                    self.grupo_botones.add(self.vbaja_sel, self.vmedia, self.vrapida)
                elif self.parent.config.synvel == "media":
                    self.grupo_botones.add(self.vbaja, self.vmedia_sel, self.vrapida)
                elif self.parent.config.synvel == "rapida":
                    self.grupo_botones.add(self.vbaja, self.vmedia, self.vrapida_sel)
            else:
                self.grupo_botones.add(self.lector, self.oflector_si)
                self.grupo_palabras.remove(self.acc3_5.img_palabras, self.acc3_6.img_palabras)
        else:
            self.grupo_botones.add(self.puerta, self.onmag, self.offmag_si, self.tam18_sel, self.tam20, self.tam22, self.lector, self.oflector_si )
    
    def manejador_preguntas(self, tecla):
        """
        Determina que instrucción leerá el sintetizador de pantalla mientras el usuario configura esta pantalla. 
        """
        if self.opcion == 1:
            if tecla == 1:
                self.spserver.stopserver()
                self.grupo_botones.remove(self.lector, self.oflector_si, self.guardar)
                self.grupo_botones.add(self.lector_si, self.oflector, self.vbaja_sel, self.vmedia, self.vrapida, self.guardar)
                self.grupo_palabras.add(self.acc3_5.img_palabras, self.acc3_6.img_palabras)                       
                self.parent.config.activar_lector = True
                self.spserver.processtext(self.pregunta2, True)
                self.opcion += 1
                
            elif tecla == 2:
                self.opcion = 3
                self.grupo_botones.remove(self.lector_si, self.oflector, self.vbaja, self.vbaja_sel, self.vmedia, self.vmedia_sel, self.vrapida, self.vrapida_sel, self.guardar)
                self.grupo_palabras.remove(self.acc3_5.img_palabras, self.acc3_6.img_palabras)
                self.grupo_botones.add(self.lector, self.oflector_si, self.guardar)
                self.parent.config.activar_lector = False
                self.spserver.processtext(u"Has configurado el lector de pantalla exitosamente, presiona enter para continuar. ", True)
                
        elif self.opcion == 2:
            if tecla == 1:
                self.grupo_botones.remove(self.vbaja, self.vmedia_sel, self.vrapida, self.vrapida_sel, self.guardar)
                self.grupo_botones.add(self.vbaja_sel, self.vmedia, self.vrapida, self.guardar)
                self.parent.config.synvel = "baja"
                
            elif tecla == 2:
                self.grupo_botones.remove(self.vbaja, self.vbaja_sel, self.vmedia, self.vrapida, self.vrapida_sel, self.guardar)
                self.grupo_botones.add(self.vbaja, self.vmedia_sel, self.vrapida, self.guardar)
                self.parent.config.synvel = "media"
                                
            elif tecla == 3:
                self.grupo_botones.remove(self.vbaja, self.vbaja_sel, self.vmedia, self.vmedia_sel, self.vrapida, self.guardar)
                self.grupo_botones.add(self.vbaja, self.vmedia, self.vrapida_sel, self.guardar)
                self.parent.config.synvel = "rapida"
            self.opcion += 1
            self.spserver.processtext(u"Has configurado el lector de pantalla exitosamente, presiona enter para continuar.", True)
                
        elif self.opcion == 3:
            if tecla ==4:
                self.parent.config.cache = True
                if self.parent.config.t_fuente != self.parent.config.preferencias["t_fuente"]:
                    self.parent.config.texto_cambio = True
                self.parent.config.guardar_preferencias()
                self.spserver.actualizar_servidor()
                self.limpiar_grupos()
                if self.parent.primera_vez:
                    self.parent.changeState(pantalla2.estado(self.parent))
                else:
                    if self.previa:
                        self.parent.VOLVER_PANTALLA_PREVIA = True
                    self.parent.popState()
    
    def handleEvents(self, events):
        """
        Evalúa los eventos que se generan en esta pantalla.        

        @param events: Lista de los eventos.
        @type events: list
        """ 
        for event in events:
            if event.type == pygame.QUIT:
                self.parent.quit()
                
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    self.limpiar_grupos()
                    self.parent.config.consultar()
                    if self.previa:
                        self.parent.VOLVER_PANTALLA_PREVIA = True
                    self.parent.popState()  
                elif event.key == 49:            
                    self.manejador_preguntas(1)
                elif event.key == 50:
                    self.manejador_preguntas(2)
                elif event.key == 51:
                    self.manejador_preguntas(3)                    
                elif event.key == pygame.K_RETURN:
                    self.manejador_preguntas(4)
            
            if pygame.sprite.spritecollideany(self.raton, self.grupo_botones):
                sprite = pygame.sprite.spritecollide(self.raton, self.grupo_botones, False)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                
                    if sprite[0].id == "puerta":
                        self.limpiar_grupos()
                        self.parent.config.consultar()
                        self.parent.popState()
                                     
                    elif sprite[0].id == "18":
                        self.grupo_botones.remove(self.tam18, self.tam20_sel, self.tam22_sel)
                        self.grupo_botones.add(self.tam18_sel, self.tam20, self.tam22, self.guardar)
                        self.parent.config.t_fuente = 18
                                
                    elif sprite[0].id == "20":
                        self.grupo_botones.remove(self.tam18_sel, self.tam20, self.tam22_sel)
                        self.grupo_botones.add(self.tam18, self.tam20_sel, self.tam22, self.guardar)
                        self.parent.config.t_fuente = 20
                            
                    elif sprite[0].id == "22":    
                        self.grupo_botones.remove(self.tam18_sel, self.tam20_sel, self.tam22)
                        self.grupo_botones.add(self.tam18, self.tam20, self.tam22_sel, self.guardar)
                        self.parent.config.t_fuente = 22
                                           
                    elif sprite[0].id == "onmag":
                        self.grupo_botones.remove(self.onmag, self.offmag_si)
                        self.grupo_botones.add(self.onmag_si, self.offmag, self.guardar)
                        self.popup_mag.agregar_grupo()
                        self.parent.config.magnificador = True
                        
                    elif sprite[0].id == "offmag":
                        self.grupo_botones.remove(self.onmag_si, self.offmag)
                        self.grupo_botones.add(self.onmag, self.offmag_si, self.guardar)
                        self.popup_mag.eliminar_grupo()
                        self.parent.config.magnificador = False
                        
                    elif sprite[0].id == "oflector":
                        self.grupo_botones.remove(self.lector_si, self.oflector, self.vbaja, self.vbaja_sel, self.vmedia, self.vmedia_sel, self.vrapida, self.vrapida_sel, self.guardar)
                        self.grupo_palabras.remove(self.acc3_5.img_palabras, self.acc3_6.img_palabras)
                        if self.parent.config.synvel != self.parent.config.preferencias["synvel"]:
                            self.parent.config.synvel = self.parent.config.preferencias["synvel"]
                        self.grupo_botones.add(self.lector, self.oflector_si, self.guardar)
                        self.parent.config.activar_lector = False
                        
                    elif sprite[0].id == "lector":
                        self.grupo_botones.remove(self.lector, self.oflector_si, self.guardar)
                        if self.parent.config.synvel == "baja":
                            self.grupo_botones.add(self.lector_si, self.oflector, self.vbaja_sel, self.vmedia, self.vrapida, self.guardar)
                        elif self.parent.config.synvel == "media":
                            self.grupo_botones.add(self.lector_si, self.oflector, self.vbaja, self.vmedia_sel, self.vrapida, self.guardar)
                        elif self.parent.config.synvel == "rapida":
                            self.grupo_botones.add(self.lector_si, self.oflector, self.vbaja, self.vmedia, self.vrapida_sel, self.guardar)
                        self.grupo_palabras.add(self.acc3_5.img_palabras, self.acc3_6.img_palabras)                       
                        self.parent.config.activar_lector = True
                        
                    elif sprite[0].id == "vbaja":
                        self.grupo_botones.remove(self.vbaja, self.vmedia_sel, self.vrapida, self.vrapida_sel, self.guardar)
                        self.grupo_botones.add(self.vbaja_sel, self.vmedia, self.vrapida, self.guardar)
                        self.parent.config.synvel = "baja"
                            
                    elif sprite[0].id == "vmedia":
                        self.grupo_botones.remove(self.vbaja, self.vbaja_sel, self.vmedia, self.vrapida, self.vrapida_sel, self.guardar)
                        self.grupo_botones.add(self.vbaja, self.vmedia_sel, self.vrapida, self.guardar)
                        self.parent.config.synvel = "media"
                             
                    elif sprite[0].id == "vrapida":
                        self.grupo_botones.remove(self.vbaja, self.vbaja_sel, self.vmedia, self.vmedia_sel, self.vrapida, self.guardar)
                        self.grupo_botones.add(self.vbaja, self.vmedia, self.vrapida_sel, self.guardar)
                        self.parent.config.synvel = "rapida"
                                                                           
                    elif sprite[0].id == "guardar":
                        self.spserver.stopserver()
                        self.parent.config.cache = True
                        if self.parent.config.t_fuente != self.parent.config.preferencias["t_fuente"]:
                            self.parent.config.texto_cambio = True
                        self.parent.config.guardar_preferencias()
                        self.spserver.actualizar_servidor()
                        self.limpiar_grupos()
                        if self.parent.primera_vez:
                            self.parent.changeState(pantalla2.estado(self.parent))
                        else:
                            if self.previa:
                                self.parent.VOLVER_PANTALLA_PREVIA = True
                            self.parent.popState()
                            
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
        self.grupo_popup.draw(self.parent.screen)
        self.grupo_tooltip.draw(self.parent.screen)
        self.dibujar_rect()
        self.draw_debug_rectangles()
