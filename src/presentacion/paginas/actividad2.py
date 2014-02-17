#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from librerias import pantalla
from librerias.textoci import texto2
from librerias.cajatexto import cajatexto
from librerias.popups import PopUp, Button
from librerias.animaciones import animacion
import pantalla2

class actividad(pantalla.Pantalla):
    def __init__(self, parent):
        """
        Método inicializador de la clase.
        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        """
        self.parent = parent
        self.screen = self.parent.screen          
        self.grupo_texto= pygame.sprite.Group()   
        self.grupo_sprite = pygame.sprite.Group()         
        self.menu2 = pygame.image.load(self.varios + "fondoact3.png").convert()
        self.menu3 = self.menu2.subsurface((666, 0, 358, 572))
        self.fondo = pygame.image.load(self.varios + "fondoact3.png").convert()    
        self.teclado = 0
        self.boton = Button("boton", self.parent, "Comprobar")
        self.grupo_boton = pygame.sprite.Group()
        self.grupo_boton.add(self.boton)
        self.img1 = pygame.image.load(self.pops + "enter.png")
        img2 = pygame.image.load(self.pops + "tab.png")
        img3 = pygame.image.load(self.pops + "f1.png")
        img4 = pygame.image.load(self.pops + "esc.png")
        img5 = pygame.image.load(self.pops + "f2.png")
        self.popupbien = PopUp(self.parent ,("prueba",), "Aceptar" ,  self.img1 ,self.grupo_popup)
        self.popupnobien = PopUp(self.parent ,("prueba",), "Aceptar" ,  self.img1 ,self.grupo_popup)        
        self.instruccion1 = u"    Pulsa la tecla F1 para ver las instrucciones. "
        self.texto =  u"    Instrucciones: resuelve los siguientes problemas y verifica la respuesta colocándola en el recuadro. "\
        u"La tecla F2 activa o desactiva la ayuda. "\
        u"ESCAPE te permitirá regresar al menú. "\
        u"Pulsa la tecla F1 para iniciar la actividad. "
        self.imagen_aplaudiendo = pygame.image.load(self.pops + "aplaudiendo.png").convert_alpha() 
        self.imagen_pensando = pygame.image.load(self.pops + "pensando.png").convert_alpha() 
        self.imagen_vacio = pygame.image.load (self.varios + "cuadro-texto-popup.png").convert_alpha()
        self.germinador = pygame.image.load(self.pops + "germinador.png").convert_alpha()
        self.dic = {"ENTER": self.img1, u"TABULACIÓN": img2, "F1": img3, "ESCAPE": img4, "F2": img5}
        self.popup_instruccion_fija = PopUp(self.parent ,self.instruccion1, "Aceptar" ,  self.dic ,self.grupo_popup,2,845,90+self.parent.config.t_fuente,-280)
        self.popupayuda = PopUp(self.parent ,self.texto, "Aceptar" ,  self.dic ,self.grupo_popup,2,512,281,100)
        self.texto_ayuda = u"    Calcula el número total de flores que puedes armar en paquetes de 25 flores. "
        self.popupvacio = PopUp(self.parent ,(self.instruccion1,), "Aceptar" ,  self.img1 ,self.grupo_popup)
        self.popupinstruccion =  PopUp(self.parent ,self.texto_ayuda, "Aceptar" ,  self.dic ,self.grupo_popup,2,512,281)  
        self.popup_instruccion_fija.agregar_grupo()
        self.popupayuda.agregar_grupo()
        self.marcador_instruccion = 0
        self.nivel1()
        self.nivel_cargado = 0
    
    def nivel1(self):
        """
        Carga las imágenes e inicializa los objetos del nivel 1 de la actividad número 2.
        """
        self.nivel = 1
        self.boton_x = pygame.sprite.Sprite()
        self.boton_x.image = pygame.image.load(self.varios + "cerrar.png").convert_alpha()
        self.boton_x.rect = (self.boton_x.image.get_rect())    
        self.boton_x.rect.move_ip(610,11)            
        self.boton_mesa = pygame.sprite.Sprite()
        self.boton_mesa.image = pygame.image.load(self.varios + "mesa.png").convert_alpha()
        self.boton_mesa.rect = ((0,415),self.boton_mesa.image.get_size())            
        self.boton_ayuda= pygame.sprite.Sprite()
        self.boton_ayuda.image = pygame.image.load(self.varios + "ayuda.png").convert_alpha()
        self.boton_ayuda.rect = (self.boton_ayuda.image.get_rect())
        self.boton_ayuda.rect.move_ip(985,500)            
        self.rectangulo_texto = pygame.sprite.Sprite()
        self.rectangulo_texto.image = pygame.image.load(self.varios + "cuadro-texto.png").convert()
        self.rectangulo_texto.rect = self.rectangulo_texto.image.get_rect()
        self.grupo_sprite.add(self.boton_ayuda,self.boton_x,self.rectangulo_texto,self.boton_mesa)
        animacion1 = animacion("anim1", self.varios+"reloj.png",5,1,446,38,None,True,100)
        animacion2 = animacion("anim2",self.varios+"obreros.png",6,1,-76,-39, None,True,6)
        animacion3 = animacion("anim3", self.varios+"caja.png",8, 1,520,355, None,True,36)
        self.grupo_anim.add(animacion1,animacion2,animacion3)
        self.pregunta = u"    Los trabajadores de una floristería tienen que empacar 3.215 flores en paquetes de 25 flores cada uno. "\
        u"¿Cuántas flores sobran después de armar todos los paquetes? "
        self.pregunta_l = u"    Los trabajadores de una floristería tienen que empacar 3215 flores en paquetes de 25 flores cada uno. "\
        u"¿Cuántas flores sobran después de armar todos los paquetes? "
        texto = texto2(700, self.popup_instruccion_fija.tam, self.pregunta, self.parent.config.t_fuente , "normal", 985,0)            
        self.grupo_texto.add(texto.img_palabras)
        self.rectangulo_texto.rect.move_ip(725,self.popup_instruccion_fija.tam + texto.ancho_final + self.parent.config.t_fuente-5)
        self.intr_texto= cajatexto(730,self.popup_instruccion_fija.tam + texto.ancho_final + self.parent.config.t_fuente, "15" , self.screen,"medium")
        self.boton.mover_boton(666+(self.menu3.get_rect().w/2), self.popup_instruccion_fija.tam + texto.ancho_final +80)
        self.texto_bien = u"    ¡Muy bien! Sabías que... un trozo de tallo verde que sea introducido en la tierra para multiplicar una planta tiene por nombre esqueje. "
        self.texto_mal = u"    Recuerda: si se reparte de forma equitativa las flores, podrás saber cuantas cajas lograrás armar. "
        self.texto_vacio = u"    Para continuar deberás contestar correctamente la pregunta. Si la casilla queda vacía no podrás avanzar al siguiente problema. "
        self.texto_ayuda = u"    Calcula el número total de flores que puedes armar en paquetes de 25 flores. "
        self.spserver.processtext(self.texto , self.parent.config.activar_lector)   
        if self.teclado == 0:
            self.teclado = True     

    def nivel2(self):
        """
        Carga las imágenes e inicializa los objetos del nivel 2 de la actividad número 2.
        """
        pygame.event.clear
        self.nivel = 2
        self.grupo_sprite.remove(self.boton_mesa)
        self.grupo_texto.empty()
        self.grupo_anim.empty()
        animacion1 = animacion("anim0_1", self.varios + "animacion4.png",10,1,-40,0,None,True,25)
        self.grupo_anim.add(animacion1)
        self.fondo = pygame.image.load(self.varios+"fondoact4.png").convert()
        self.pregunta = u"    En una cesta hay 60 sobres de semillas, de ellos 1/5 son de pimentón, 1/2 son de girasol y el resto de perejil. ¿Cuántos sobres son de semillas de perejil? "
        texto = texto2(700, self.popup_instruccion_fija.tam, self.pregunta, self.parent.config.t_fuente, "normal", 985)
        self.grupo_texto.add(texto.img_palabras)
        self.pregunta_lector = u"    En una cesta hay 60 sobres de semillas, de ellos un quinto son de pimentón, un medio son de girasol y el resto de perejil. ¿Cuántos sobres son de semilla de perejil? "
        self.rectangulo_texto.rect.y =self.popup_instruccion_fija.tam + texto.ancho_final + self.parent.config.t_fuente-5
        self.intr_texto= cajatexto(730,self.popup_instruccion_fija.tam + texto.ancho_final + self.parent.config.t_fuente, "18" , self.screen,"medium")
        self.boton.mover_boton(666+(self.menu3.get_rect().w/2), self.popup_instruccion_fija.tam + texto.ancho_final +80)        
        self.texto_bien = u"    ¡Excelente! Para evitar la deforestación y contribuir con el cuidado del ambiente, cuando vayas de visita a los parques recoge los desechos que te hayan quedado durante tu visita. "
        self.texto_mal = u"    Recuerda: un sobre esta representado en fracciones como 1/60. "
        self.texto_mal_lector = u"    Recuerda: un sobre está representado en fracciones como 1 entre 60. "
        self.texto_vacio = u"    Para continuar deberás contestar correctamente la pregunta. Si la casilla queda vacía no podrás avanzar al siguiente problema. "
        self.texto_ayuda = u"    Al construir la ecuación utiliza los 60 sobres como la unidad. Luego de hallar el valor en fracciones transformala a números naturales. "
        self.nivel_cargado = 1
        self.spserver.processtext(u"problema número 2:"+self.pregunta_lector  + u"escribe tu respuesta y utiliza la tecla ENTER para confirmar" , self.parent.config.activar_lector)
        if self.teclado == 0:
            self.teclado = True        
        
    def nivel3 (self):
        """
        Carga las imágenes e inicializa los objetos del nivel 3 de la actividad número 2.
        """
        pygame.event.clear
        self.nivel=3        
        self.grupo_texto.empty()
        self.grupo_anim.empty()           
        self.grupo_anim.empty()
        self.fondo = pygame.image.load(self.varios+"fondoact5.png").convert()
        animacion1 = animacion("anim_1", self.varios+"animacion5.png",6,1,-30,44,None,True,25)
        self.grupo_anim.add(animacion1)
        self.pregunta =u"  Una distribuidora de flores recibió 12.831 bolívares por concepto de las ventas durante el mes de marzo. Si vendieron 987 flores, ¿Cuál es el costo de cada flor? "
        self.pregunta_l =u"  Una distribuidora de flores recibió 12831 bolívares por concepto de las ventas durante el mes de marzo. Si vendieron 987 flores, ¿Cuál es el costo de cada flor? "
        texto = texto2(700, self.popup_instruccion_fija.tam, self.pregunta, self.parent.config.t_fuente, "normal", 985)
        self.grupo_texto.add(texto.img_palabras)
        self.rectangulo_texto.rect.y =self.popup_instruccion_fija.tam + texto.ancho_final + self.parent.config.t_fuente-5
        self.intr_texto= cajatexto(730,self.popup_instruccion_fija.tam + texto.ancho_final + self.parent.config.t_fuente, "13" , self.screen,"medium")
        self.boton.mover_boton(666 +(self.menu3.get_rect().w/2), self.popup_instruccion_fija.tam + texto.ancho_final +80)        
        self.texto_bien = u"   ¡Muy bien! ¿Has hecho alguna vez un germinador con semillas de caraota? Con la ayuda de tu maestra o maestro investiga los pasos a seguir para que una semilla se reproduzca y se logre obtener una nueva planta. "
        self.texto_mal = u"    Recuerda: debes separar en partes iguales para obtener el valor de cada flor. "
        self.texto_vacio = u"    Para continuar deberás contestar correctamente la pregunta. Si la casilla queda vacía no podrás avanzar al siguiente problema. "
        self.texto_ayuda = u"    Existe una operación básica que te permite repartir equitativamente una cantidad entre un cierto número. Es el proceso contrario a la multiplicación. "
        self.spserver.processtext(u"problema número 3:"+self.pregunta + u"escribe tu respuesta y utiliza la tecla ENTER para confirmar", self.parent.config.activar_lector)   
        if self.teclado == 0:
            self.teclado = True     
                  
    def click(self, event):
        """
        Verifica cuando se hizo click.

        @param event: Evento que notifica si se hizo click.
        @type event: pygame.event.Event

        @return: True si se realizo el click, sino retorna False.
        @rtype: bool
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pygame.mouse.get_pressed()[0]:
                return True
            else:
                return False
    
    def manejador_popups(self, tipo_mensaje):
        """
        Evalúa el tipo de mensaje que se dibujara en la ventana emergente.
        @param tipo_mensaje: Define el tipo de mensaje que se mostrará. Acepta los siguientes valores:
        "bien", "mal", "vacio", "instruccion".
        @type tipo_mensaje: str
        """
        if not self.popupnobien.activo or not self.popupbien.activo:
            if tipo_mensaje == "bien":
                self.spserver.stopserver()  
                if self.nivel ==3:
                    self.spserver.processtext(self.texto_bien+u"Terminaste todos los problemas! Pulsa enter para volver al menú del recurso.", self.parent.config.activar_lector)           
                    self.popupbien = PopUp(self.parent ,(self.texto_bien,), "Aceptar" ,  (self.germinador,self.imagen_aplaudiendo) ,self.grupo_popup)

                else:
                    self.spserver.processtext(self.texto_bien+u"Pulsa enter para pasar al siguiente problema. ", self.parent.config.activar_lector)
                    self.popupbien = PopUp(self.parent ,(self.texto_bien,), "Aceptar" ,  self.imagen_aplaudiendo ,self.grupo_popup)
                                
                self.popupbien.agregar_grupo()
                                
            
            elif tipo_mensaje == "mal":
                self.popupnobien = PopUp(self.parent ,(self.texto_mal,), "Aceptar" ,  self.imagen_pensando ,self.grupo_popup)
                self.popupnobien.agregar_grupo() 
                self.spserver.stopserver()
                if self.nivel ==2:
                    self.spserver.processtext(u"tu respuesta es: "+ self.intr_texto.palabra_f + self.texto_mal_lector + u"Pulsa enter para continuar", self.parent.config.activar_lector)
                    self.intr_texto.reiniciar()
                else:
                    self.spserver.processtext(u"tu respuesta es: "+ self.intr_texto.palabra_f +self.texto_mal+u" Pulsa enter para continuar", self.parent.config.activar_lector)
                    self.intr_texto.reiniciar()
                
            elif tipo_mensaje == "vacio":
                self.popupvacio = PopUp(self.parent ,(self.texto_vacio,), "Aceptar" ,  self.imagen_vacio,self.grupo_popup)
                self.popupvacio .agregar_grupo()            
                self.spserver.stopserver()
                self.spserver.processtext(self.texto_vacio+u"Pulsa enter para continuar", self.parent.config.activar_lector)                                       
                
            elif tipo_mensaje == "instruccion":
                if self.popupinstruccion.activo:
                    
                    self.spserver.stopserver()
                    self.popupinstruccion.eliminar_grupo()
                    if self.nivel==2:   
                        self.spserver.processtext(self.pregunta_lector + u"escribe tu respuesta y utiliza la tecla ENTER para confirmar", self.parent.config.activar_lector)                                       
                    else:                                       
                        self.spserver.processtext(self.pregunta_l + u"escribe tu respuesta y utiliza la tecla ENTER para confirmar", self.parent.config.activar_lector)
                                                   
                else: 
                    self.popupinstruccion =  PopUp(self.parent ,self.texto_ayuda, "Aceptar" ,  self.dic ,self.grupo_popup,2,512,281)   
                    self.popupinstruccion.agregar_grupo()
                    self.spserver.stopserver()
                    self.spserver.processtext(self.texto_ayuda + u"Pulsa F2 para continuar.", self.parent.config.activar_lector)                                       
    
    def evaluador(self):
        """
        Evalúa si es correcto el contenido de la caja de texto y llama al método manejador_popups(). 
        """
        if self.intr_texto.comparador():
            self.manejador_popups("bien")

        elif self.intr_texto.caja_vacia():
            self.manejador_popups("vacio")

        elif not self.intr_texto.comparador():
            self.manejador_popups("mal")

    def update(self):
        """"
        Actualiza los grupos de sprites y la pantalla.
        """ 
        grupo_cuadro_texto = pygame.sprite.Group()
        self.intr_texto.titilar()
        self.intr_texto.get_imagen(grupo_cuadro_texto)
        self.screen.blit(self.fondo,(0,0))
        self.grupo_anim.draw(self.screen)          
        self.parent.screen.blit (self.menu3 ,(666,0))            
        self.grupo_sprite.draw(self.screen)          
        self.grupo_texto.draw(self.screen)
        self.grupo_boton.draw(self.screen)
        grupo_cuadro_texto.draw(self.screen)
        self.grupo_popup.draw(self.screen)    

    def handleEvents(self, eventos):         
        """
        Evalúa los eventos que se generan en esta pantalla.        
        @param eventos: Lista de los eventos.
        @type eventos: list
        """
        teclasPulsadas = pygame.key.get_pressed()
        for event in eventos:
            if (event.type == pygame.QUIT):
                self.parent.quit()                

            if not self.popupbien.activo and not self.popupnobien.activo and not self.popupvacio.activo:
                
                if self.teclado == 0:
                    self.teclado = True
            if self.popupbien.activo:
                self.popupbien.manejador_eventos(event)
                if not self.popupbien.evaluar_click():
                    self.spserver.stopserver()
                    if self.nivel == 1:
                        self.nivel2()
                    elif self.nivel == 2:
                        self.nivel3()
                    elif self.nivel == 3:
                        self.limpiar_grupos()
                        self.parent.pushState(pantalla2.estado(self.parent))                         

            if self.popupnobien.activo:
                self.popupnobien.manejador_eventos(event)               
                if not self.popupnobien.evaluar_click():
                    self.spserver.stopserver()
                    if self.nivel==2:
                        self.spserver.processtext(self.pregunta_lector+u"escribe tu respuesta y utiliza la tecla ENTER para confirmar", self.parent.config.activar_lector)
                    else:
                        self.spserver.processtext(self.pregunta_l+u"escribe tu respuesta y utiliza la tecla ENTER para confirmar", self.parent.config.activar_lector)             

            if self.popupvacio.activo:   
                self.popupvacio.manejador_eventos(event) 
                pygame.event.clear()         
                if not self.popupvacio.evaluar_click():
                    self.spserver.stopserver()   
                    if self.nivel==2:
                        self.spserver.processtext(self.pregunta_lector+u"escribe tu respuesta y utiliza la tecla ENTER para confirmar", self.parent.config.activar_lector)
                    else:
                        self.spserver.processtext(self.pregunta_l+u"escribe tu respuesta y utiliza la tecla ENTER para confirmar", self.parent.config.activar_lector)             


            if teclasPulsadas[pygame.K_ESCAPE]:
                self.limpiar_grupos()
                self.parent.pushState(pantalla2.estado(self.parent)) 

            if self.click(event):

                if not self.popupayuda.activo and not self.popupbien.activo and not self.popupnobien.activo:

                    if not self.popupinstruccion.activo:
                        if self.rectangulo_texto.rect.collidepoint(pygame.mouse.get_pos()):
                            self.teclado = True
                        else:
                            self.teclado= False

                        if self.boton.rect.collidepoint(pygame.mouse.get_pos()):
                            self.evaluador()                                                                        

                    if self.boton_ayuda.rect.collidepoint(pygame.mouse.get_pos()):                
                        self.manejador_popups("instruccion")

                if self.boton_x.rect.collidepoint(pygame.mouse.get_pos()):
                    self.limpiar_grupos()
                    self.parent.pushState(pantalla2.estado(self.parent)) 

            if event.type == pygame.KEYDOWN:  
                if teclasPulsadas[pygame.K_TAB]:
                    if not self.popupinstruccion.activo and not self.popupayuda.activo and not self.popupbien.activo and not self.popupnobien.activo:
                        if self.teclado == 0:
                            self.teclado = True

                            if self.intr_texto.caja_vacia():
                                self.spserver.stopserver()
                                self.spserver.processtext(u"escribe los números que corresponden a la respuesta correcta." , self.parent.config.activar_lector)                                                      
                            else:
                                self.spserver.stopserver()
                                self.spserver.processtext(u"has escrito el número: "+self.intr_texto.palabra_f , self.parent.config.activar_lector)                                       

                if teclasPulsadas[pygame.K_F2]:
                    if not self.popupayuda.activo and not self.popupbien.activo and not self.popupnobien.activo:
                        self.manejador_popups("instruccion")

                if teclasPulsadas [pygame.K_SPACE]:
                    self.spserver.repetir()                    

                if teclasPulsadas[pygame.K_F1]:
                    self.spserver.stopserver()
                    if self.popupayuda.activo:
                        self.popupayuda.eliminar_grupo()
                        if not self.marcador_instruccion:
                            self.spserver.stopserver()
                            self.spserver.processtext(self.pregunta_l +u"escribe tu respuesta y utiliza la tecla ENTER para confirmar", self.parent.config.activar_lector)
                            self.marcador_instruccion = 1
                        if self.popupayuda.activo:
                            self.popupayuda.eliminar_grupo()
                    else:
                        self.spserver.processtext(self.texto, self.parent.config.activar_lector)
                        self.popupayuda.agregar_grupo()

            if self.intr_texto.iniciar(event, self.teclado):
                self.evaluador()
                self.teclado = 0

    def draw(self):
        pass

    def start(self):
        pass

    def pause(self):
        pass

    def cleanUp(self):
        pass
