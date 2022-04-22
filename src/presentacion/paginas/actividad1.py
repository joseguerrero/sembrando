#!/usr/bin/env python

import random
import pygame

from librerias import pantalla
from librerias.prp import prp
from librerias.popups import PopUp
from librerias.cursor import cursor
from librerias.image import Image
from librerias.object import GameObject
from librerias.limite import limite
from librerias.marcador import marcador
from librerias.button import Button, RenderButton
from librerias.personaje import personaje, RenderChar
from librerias.animaciones import animacion, RenderAnim

class estado(pantalla.Pantalla):
    tiempo = 0
    reloj = pygame.time.Clock()
    anim_fondo = RenderAnim()
    grupo_botones = RenderButton()
    grupo_personaje = RenderChar()
    sprite = pygame.sprite.Sprite()
    marcador = pygame.sprite.Sprite()
    limites = pygame.sprite.Group()
    grupo_objetos = pygame.sprite.Group()
    grupo_marcadores = pygame.sprite.Group()
    grupo_popup =  pygame.sprite.OrderedUpdates()
    grupo_imagenes = pygame.sprite.OrderedUpdates()
    foobar = True
    ayuda = False
    choque = False
    marker = False
    completado = False
    final_cont  = True
    inicio_cont = False
    texto_visible = False
    leer_ubicacion = False
    servidor_callado = True
    explicar_sonidos = False
    nivel = 1
    respuesta = 2
    vel_nube = -2
    nivel_actual = 1
    
    def __init__(self, parent):
        """
        Método inicializador de la clase. 
        
        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        """
        self.apla = pygame.image.load(self.pops + "aplaudiendo.png").convert_alpha()
        self.pensa = pygame.image.load(self.pops + "pensando.png").convert_alpha()
        poporquidea = pygame.image.load(self.pops + "orquidea.png").convert_alpha()
        popapamate = pygame.image.load(self.pops + "popupapamate.png").convert_alpha()
        poparaguaney = pygame.image.load(self.pops + "popuparaguaney.png").convert_alpha()
        popclorofila = pygame.image.load(self.pops + "popupclorofila.png").convert_alpha()
        popinjerto = pygame.image.load(self.pops + "popupinjerto.png").convert_alpha()
        poprepro = pygame.image.load(self.pops + "popupreproduccion.png").convert_alpha()
        popportu = pygame.image.load(self.pops + "portu.png").convert_alpha()
        popacodo = pygame.image.load(self.pops + "popuacodo.png").convert_alpha()
        popmango = pygame.image.load(self.pops + "popumango.png").convert_alpha()
        popyuca = pygame.image.load(self.pops + "popuyuca.png").convert_alpha()
        self.img_pistas = {
            0: poparaguaney,
            1: popapamate,
            2: popclorofila,
            3: poporquidea,
            4: poprepro,
            5: popyuca,
            6: popmango,
            7: popportu,
            8: popacodo,
            9: popinjerto
        }
        esc = pygame.image.load(self.pops + "esc.png").convert_alpha()
        raton = pygame.image.load(self.pops + "touch.png").convert_alpha()
        salir = pygame.image.load(self.pops + "boton-salir.png").convert_alpha()
        enter = pygame.image.load(self.pops + "enter.png").convert_alpha()
        teclado = pygame.image.load(self.pops + "flechas.png").convert_alpha()
        f1 = pygame.image.load(self.pops + "f1.png").convert_alpha()
        self.img_textos = {"ENTER" : enter, "TECLADO": teclado, "F1": f1, "ESC": esc, "SALIR": salir, "RATON":raton}
        self.raton = cursor()
        self.parent = parent
        self.visor = self.parent.screen
        pygame.display.set_caption('Siembra la semilla')
        self.flecha_verde = pygame.image.load(self.varios + "flecha-verde.png").convert_alpha()
        self.preguntas = prp()
        self.casa = Image(0, 70, self.varios + "casa.png")
        self.poste = Image(880, 0, self.varios + "poste.png")
        self.tractor = Image(840, 80, self.varios +"tractor.png")
        self.pala = GameObject(590, 380, self.varios + "pala.png", "la pala. ")
        self.abono = GameObject(900, 305, self.varios + "abono.png", "el abono. ")
        self.carre = GameObject(200, 80, self.varios + "carre.png", "la carretilla. ")
        self.insec = GameObject(760, 140, self.varios + "insec.png", u"el controlador biológico. ")
        self.regadera = GameObject(792, 270, self.varios + "regadera.png", "la regadera. ")
        self.semillas = GameObject(450, 200, self.varios + "semillas.png", "las semillas. ")
        self.nubes = animacion("nubes", self.varios + "nubes.png", 1, 1, 30, -15, -1, False, 18)
        self.salir = Button(830, 60, "salir", "Salir", self.botones + "boton-salir.png", 1, -1, False, 1)
        self.flecha = animacion("flecha", self.varios + "flecha-verde.png", 3, 1, 800, 350, -1, True, 6)
        self.flores = animacion("flores", self.varios + "campo-flores.png", 4, 1, 758, 290, -1, False, 18)
        self.siembra = animacion("siembra", self.varios + "cinta-campesino.png", 3, 1, 680, 250, -1, True, 9)
        self.granjero = personaje(200, 128, self.varios + "0.png", 2)
        self.popup_respuesta = PopUp(parent, ("Respuesta " ), "Aceptar", self.flecha_verde, self.grupo_popup)
        self.popup_pregunta = PopUp(parent, ("Pregunta ", "p1 ", "p2 ", "p3 " ), "Aceptar", 0, self.grupo_popup, 1)
        self.popup_ayuda = PopUp(parent, self.preguntas.instruc[0], "", self.img_textos , self.grupo_popup, 2, 512, 214, 100)
        self.popup_instruc = PopUp(parent, u"    Pulsa la tecla F1 para activar o desactivar las instrucciones del juego. ", "", self.img_textos , self.grupo_popup, 2, 240, 482, -160)
        self.popup_final1 = PopUp(self.parent, (u"    ¡Muy bien! Has finalizado el primer nivel. ", ), "Aceptar", self.apla, self.grupo_popup)
        self.update()
        
    def limpiar_grupos(self):
        """Limpia los elementos de una pantalla. """
        self.grupo_personaje.empty()
        self.grupo_imagenes.empty()
        self.grupo_objetos.empty()
        self.grupo_personaje.empty()
        self.grupo_botones.empty()
        self.anim_fondo.empty()
        self.grupo_popup.empty()
        
    def nivel1(self):
        """
        Carga las imágenes e inicializa los objetos del nivel 1 de la actividad número 1.
        """
        self.preguntas.__init__()
        self.nivel_actual = 1
        self.completado = False
        self.foobar = True
        self.ayuda = False
        self.fondo = pygame.image.load(self.varios + "fondo1.png").convert()
        self.limpiar_grupos()
        self.anim_fondo.empty()
        self.poste.relocate(880, 0)
        self.tractor.relocate(840, 80)
        self.semillas.relocate(450, 200)
        self.regadera.relocate(880, 270)
        self.meta = pygame.Rect(800, 470, 50, 100)
        self.grupo_marcadores.empty()
        self.m_semilla = marcador((357, 314, 20, 20), "semilla")
        self.sem_rec = marcador((357, 234, 20, 20), "semilla1")
        self.m_rega = marcador((664, 314, 20, 20), "regadera")
        self.rega_rec = marcador((786, 314, 20, 20), "regadera1")
        self.m_pala = marcador((501, 314, 20, 20), "pala")
        self.grupo_marcadores.add(self.m_semilla, self.m_rega)
        self.limites.empty()
        self.limites.add(limite((167, 267, 170, 20), 1), limite((317, 196, 20, 91), 2), limite((317, 196, 113, 20), 3),
                         limite((410, 196, 20, 91), 4), limite((410, 267, 430, 20), 5), limite((167, 267, 20, 117), 6),
                         limite((820, 267, 20, 117), 7), limite((167, 364, 310, 20), 8), limite((550, 364, 290, 20), 9), 
                         limite((457, 364, 20, 208), 10), limite((550, 364, 20, 122), 11), limite((550, 466, 169, 20), 12), 
                         limite((699, 466, 20, 106), 13), limite((457, 552, 262, 20), 14) )
        self.granjero.por_defecto(170, 128, self.varios + "0.png", 2, self.limites)
        self.grupo_personaje.add(self.granjero)
        self.granjero.actualizar_rects()
        self.grupo_objetos.add(self.semillas, self.regadera, self.pala)
        self.grupo_imagenes.add(self.tractor, self.poste, self.casa)
        self.grupo_botones.add(self.salir)
        self.anim_fondo.add(self.nubes, self.flores)
        self.popup_instruc.agregar_grupo()
        self.flores.detener()
        self.mostrar_ayuda()
        if self.parent.config.activar_lector:
            self.limites.add(limite((477, 365, 73, 20), 15))
        
    def nivel2(self):
        """
        Carga las imágenes e inicializa los objetos del nivel 1 de la actividad número 1.
        """
        self.nivel_actual = 2
        self.completado = False
        self.foobar = True
        self.ayuda = False
        self.fondo = pygame.image.load(self.varios + "fondo2.png").convert()
        self.limpiar_grupos()
        self.poste.relocate(880, -70)
        self.tractor.relocate(840, 20)
        self.semillas.relocate(290, 300)
        self.regadera.relocate(495, 125)
        self.meta = pygame.Rect(800, 400, 50, 80)
        self.grupo_marcadores.empty()
        self.m_sem_car = marcador((206, 246, 20, 20), "sem_car")
        self.m_rega = marcador((424, 246, 20, 20), "regadera")
        self.m_pala = marcador((510, 246, 20, 20), "pala")
        self.m_insec = marcador((645, 246, 20, 20), "insec")
        self.m_abono = marcador((808, 246, 20, 20), "abono")
        self.sem_rec = marcador((206, 315, 20, 20), "semillas1")
        self.rega_rec = marcador((424, 180, 20, 20), "regadera1")
        self.carre_rec = marcador((206, 180, 20, 20), "carretilla1")
        self.insect_rec = marcador((645, 180, 20, 20), "insect1")
        self.abono_rec = marcador((808, 315, 20, 20), "abono1")
        self.limites.empty()
        self.limites.add(limite((153, 124, 20, 259), 1), limite((153, 124, 113, 20), 2), limite((246, 124, 20, 92), 3), 
                         limite((246, 196, 151, 20), 4), limite((377, 124, 20, 92), 5), limite((377, 124, 113, 20), 6),
                         limite((470, 124, 20, 92), 7), limite((470, 196, 148, 20), 8), limite((598, 124, 20, 92), 9),
                         limite((598, 124, 117, 20), 10), limite((695, 124, 20, 92), 11), limite((695, 196, 177, 20), 12), 
                         limite((852, 196, 20, 187), 13), limite((760, 363, 112, 20), 13), limite((760, 293, 20, 90), 14), 
                         limite((555, 293, 225, 20), 15), limite((555, 293, 20, 120), 16), limite((555, 393, 170, 20), 17), 
                         limite((705, 393, 20, 118), 18), limite((463, 491, 262, 20), 19), limite((463, 293, 20, 218), 20), 
                         limite((246, 293, 237, 20), 21), limite((246, 293, 20, 90), 22), limite((153, 363, 113, 20), 23),
                         )
        self.granjero.por_defecto(150, 50, self.varios + "-1.png", 2, self.limites)
        self.granjero.actualizar_rects()
        self.granjero.codigo = -1
        self.grupo_personaje.add(self.granjero)
        self.grupo_objetos.add(self.carre, self.pala, self.regadera, self.semillas, self.abono, self.insec)
        self.grupo_imagenes.add(self.tractor, self.poste)
        self.anim_fondo.add(self.nubes, self.flores)
        self.popup_instruc.agregar_grupo()
        self.grupo_botones.add(self.salir)
        self.flores.detener()
        if self.parent.config.activar_lector:
            self.limites.add(limite((483, 294, 72, 20), 24)) # Ladrillo invisible
            self.pista_sonidos()
        
    def mostrar_ayuda(self):
        """
        Muestra las instrucciones de uso de la actividad 1.
        """
        if self.ayuda == False:
            self.popup_ayuda.agregar_grupo()
            self.spserver.processtext(self.preguntas.instruc[1], self.parent.config.activar_lector)
            self.ayuda = True
        else:
            self.popup_ayuda.eliminar_grupo()
            self.spserver.stopserver()
            self.ayuda = False
            if self.popup_pregunta.activo:
                self.leer_respuestas(self.preguntas.dic_pre[self.preguntas.valor], self.preguntas.dic_res[self.preguntas.valor], True)
            elif self.popup_respuesta.activo:
                self.spserver.processtext(self.preguntas.dic_pistas[self.preguntas.valor][self.cache_click] + "Pulsa Enter para continuar. ", self.parent.config.activar_lector)
                
    def pista_sonidos(self):
        """
        Indica el momento en el que inicia un contador para sincronizar el sintetizador de voz
        con los sonidos de instrucción.
        """
        self.contador = pygame.time.Clock()
        self.contador.tick(30)
        self.inicio_cont = True
        self.final_cont = False
        
    def handleEvents(self, eventos):         
        """
        Evalúa los eventos que se generan en esta pantalla.        

        @param eventos: Lista de los eventos.
        @type eventos: list
        """  
        self.teclasPulsadas = pygame.key.get_pressed()
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                self.parent.popState()
                
            if evento.type == pygame.QUIT:
                self.parent.quit()
   
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_F1:
                if not self.completado:
                    self.mostrar_ayuda()
                
                if not self.explicar_sonidos and self.parent.config.activar_lector:
                    self.popup_ayuda.eliminar_grupo()
                    self.draw()
                    self.pista_sonidos()
                    self.explicar_sonidos = True
                
            if pygame.sprite.spritecollideany(self.raton, self.grupo_botones):
                sprite = pygame.sprite.spritecollide(self.raton, self.grupo_botones, False)
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if sprite[0].id == "salir":
                        self.parent.popState()
            
            if self.popup_pregunta.activo and not self.popup_ayuda.activo:
                self.popup_respuesta = PopUp(self.parent, ("Respuesta " ), "Aceptar", self.flecha_verde, self.grupo_popup)
                self.popup_pregunta.manejador_eventos(evento)       
                if self.teclasPulsadas[pygame.K_1] and self.choque:
                    self.evaluar_respuesta(0)
                elif self.teclasPulsadas[pygame.K_2] and self.choque:
                    self.evaluar_respuesta(1)
                elif self.teclasPulsadas[pygame.K_3] and self.choque:
                    self.evaluar_respuesta(2)
                elif self.popup_pregunta.evaluar_click() != -1:
                    self.evaluar_respuesta(self.popup_pregunta.evaluar_click())
            
            if self.popup_respuesta.activo and not self.popup_ayuda.activo:
                self.popup_pregunta.manejador_eventos(evento)
                self.popup_respuesta.manejador_eventos(evento)
                self.popup_pregunta.activo = False
                self.granjero.ocupado = True
                if self.teclasPulsadas[pygame.K_RETURN] or self.popup_respuesta.evaluar_click() != -1:
                    if self.respuesta == 1: 
                        self.actualizar_pj()
                        self.popup_respuesta.eliminar_grupo()
                        self.popup_pregunta.eliminar_grupo()
                    elif self.respuesta == 0: 
                        self.popup_pregunta.activo = True    
                        self.leer_respuestas(self.preguntas.dic_pre[self.preguntas.valor], self.preguntas.dic_res[self.preguntas.valor], True)
                        self.popup_respuesta.eliminar_grupo()
                    self.granjero.ocupado = False
                    self.respuesta = 2
        
            if self.popup_final1.activo:
                self.granjero.ocupado = True
                self.popup_final1.manejador_eventos(evento)
                if self.teclasPulsadas[pygame.K_RETURN] or self.popup_final1.evaluar_click() != -1:
                    self.popup_final1.eliminar_grupo()
                    self.granjero.ocupado = False
                    self.nivel = 2
                    
        if not self.popup_ayuda.activo and not self.completado :
            self.granjero.update()
        self.detectar_colision()
        self.colision_marcador()
        if self.parent.config.activar_lector:
            self.actualizar_marcadores()
        self.contar()
        self.logica()
        
    def update(self):
        """
        Verifica el cambio de nivel de la actividad 1.
        """
        if self.nivel == 1:
            self.nivel1()
            self.nivel = 0
        elif self.nivel == 2:
            self.nivel2()
            self.nivel = 0
            
    def contar(self):
        """
        Una vez se llama la función pista_sonidos(), se mide el tiempo transcurrido y en los intervalos definidos
        se enviá información al sintetizador de voz, seguidamente se reproduce el sonido asociado a la 
        instrucción.
        """
        if self.inicio_cont and not self.final_cont:
            if self.nivel_actual == 1:
                self.granjero.ocupado = True
                if self.tiempo > 21000:
                    self.tiempo = 0
                    self.ayuda = False
                    self.final_cont = True
                    self.granjero.ocupado = False
                else:
                    self.tiempo += self.contador.get_time()
                    
                if self.tiempo in range(1033, 1066):
                    self.ayuda = True
                    self.spserver.processtext(u"Este sonido te indica que vas por el camino correcto. ", self.parent.config.activar_lector)
                    
                elif self.tiempo in range(6000, 6033):
                    self.granjero.sonido_caminar.play(5)
                     
                elif self.tiempo in range(8000, 8033):
                    self.spserver.processtext(u"Este sonido te indica que has encontrado un obstáculo. ", self.parent.config.activar_lector)
                    
                elif self.tiempo in range(13000, 13033):
                    self.granjero.sonido_choque.play(5)
                    
                elif self.tiempo in range(14000, 14033):
                    self.spserver.processtext(u"Te encuentras en el primer nivel, muévete hacia la derecha para comenzar. ", self.parent.config.activar_lector)
                    
            elif self.nivel_actual == 2:
                self.granjero.ocupado = True
                if self.tiempo > 13000:
                    self.tiempo = 0
                    self.ayuda = False
                    self.final_cont = True
                    self.granjero.ocupado = False
                    self.grupo_marcadores.add(self.m_sem_car, self.m_rega, self.m_abono, self.m_insec)
                else:
                    self.tiempo += self.contador.get_time()
                
                if self.tiempo in range(1033, 1066):
                    self.ayuda = True
                    self.spserver.processtext(u"Te encuentras en el nivel 2. Busca la carretilla " 
                                              u"y luego recolecta los elementos necesarios para la siembra. ",
                                              self.parent.config.activar_lector)
                
    def logica(self): 
        """
        Define y gestiona las condiciones para completar los niveles 1 y 2 de la actividad 1.
        """       
        if (self.granjero.codigo == 7 and self.nivel_actual == 1) or (self.nivel_actual == 2 and self.granjero.codigo >= 31):  
            if not self.completado:
                self.anim_fondo.add(self.flecha)
                if self.parent.config.activar_lector and self.foobar:
                    self.ayuda = True
                    self.spserver.processtext(u"Has recolectado todos los elementos de este nivel, avanza hasta el sembradío para completar la siembra. " , self.parent.config.activar_lector)
                    if self.nivel_actual == 1:
                        self.granjero.relocate(460, 300)
                    elif self.nivel_actual == 2:
                        self.granjero.relocate(460, 260)
                    self.foobar = False
                    
        if self.marker and self.parent.config.activar_lector:
            self.leer_marcador()
        else:
            self.leer_ubicacion = False
              
        if self.choque:
            self.mostrar_pregunta()
        else:
            if not self.ayuda and not self.marker and self.spserver.hablando:
                self.spserver.stopserver()
                
            self.texto_visible = False
            self.popup_pregunta.eliminar_grupo()
           
        if self.meta.colliderect(self.granjero.rt_car) and self.granjero.codigo == 7 and self.nivel_actual == 1:
            self.flores.continuar()
            self.anim_fondo.add(self.siembra)
            self.anim_fondo.remove(self.flecha)
            self.grupo_personaje.remove(self.granjero)
            self.meta = pygame.Rect(0, 0, 1, 1)
            self.completado = True
            self.ayuda = True
            self.popup_final1.agregar_grupo()
            self.spserver.processtext(u"¡Muy bien! Has finalizado el primer nivel. Pulsa Enter para continuar. " , self.parent.config.activar_lector)
            
        if self.meta.colliderect(self.granjero.rt_car) and self.granjero.codigo == 31 and self.nivel_actual == 2:
            self.flores.continuar()
            self.anim_fondo.add(self.siembra)
            self.anim_fondo.remove(self.flecha)
            self.grupo_personaje.remove(self.granjero)
            self.meta = pygame.Rect(0, 0, 1, 1)
            self.completado = True
            self.ayuda = True
            self.popup_instruc.eliminar_grupo()
            self.popup_instruc = PopUp(self.parent, u"    ¡Excelente! Pulsa la tecla ESC o sobre el botón SALIR para ir al menú principal. ", "", self.img_textos , self.grupo_popup, 2, 240, 440, -160)
            self.popup_instruc.agregar_grupo()
            self.spserver.processtext(u"¡Excelente! Pulsa la tecla escape " 
            u"o sobre el botón salir para ir al menú principal. ", self.parent.config.activar_lector)
            
    def evaluar_respuesta(self, valor):
        """
        Verifica si la opción seleccionada es la correcta. Muestra un mensaje emergente indicando si es o no 
        correcto, adicionalmente si esta activado el sintetizador de voz, leerá el contenido del mensaje 
        emergente.
        
        @param valor: Opción elegida por el usuario.
        @type valor: int
        """
        self.cache_click = valor
        try:
            respuesta = self.preguntas.dic_res[self.preguntas.valor][valor]
            if respuesta == self.preguntas.r_correcta[self.preguntas.valor]:
                self.respuesta = 1
                self.popup_respuesta = PopUp(self.parent, (self.preguntas.dic_pistas[self.preguntas.valor][valor], ), "Aceptar", ( self.img_pistas[self.preguntas.valor], self.apla)  , self.grupo_popup, 0 , 512, 400 )
            else:
                self.respuesta = 0
                self.popup_respuesta = PopUp(self.parent, (self.preguntas.dic_pistas[self.preguntas.valor][valor], ), "Aceptar",  self.pensa, self.grupo_popup, 0, 512, 400)
            self.spserver.processtext(self.preguntas.dic_pistas[self.preguntas.valor][valor] + "Pulsa Enter para continuar. ", self.parent.config.activar_lector)            
            self.popup_respuesta.agregar_grupo()
        except:
            print("Valor fuera de rango")
    
    def det_msj_n1(self):
        """
        Determina la instrucción que leerá el sintetizador de voz al pasar sobre un marcador
        de posición del nivel 1, a partir del código del personaje.
        @return: Código correspondiente a la instrucción que leerá el sintetizador de voz.
        @rtype: int 
        """
        if self.marcador.id == "semilla":
            if self.granjero.codigo in [0,2]:
                return 0
            elif self.granjero.codigo == 1:
                return 1 
            else:
                return 2
          
        elif self.marcador.id == "regadera":
            if self.granjero.codigo in [0,1]:
                return 0
            elif self.granjero.codigo == 2:
                return 1
            else:
                return 2
        
        elif self.marcador.id == "pala":
            if self.granjero.codigo >= 3:
                return 0
            else:
                return 1
            
        elif self.marcador.id in ["semilla1", "regadera1"]:
            return 0
        
        else:
            return 0
        
    def det_msj_n2(self):
        """
        Determina la instrucción que leerá el sintetizador de voz al pasar sobre un marcador
        de posición del nivel 2, a partir del código del personaje.
        @return: Código correspondiente a la instrucción que leerá el sintetizador de voz.
        @rtype: int 
        """
        if self.marcador.id == "sem_car":
            if self.granjero.codigo == -1:
                return 2
            elif self.granjero.codigo in range(0, 31, 2):
                return 0
            else:
                return 1
        
        elif self.marcador.id == "regadera":
            if self.granjero.codigo in [0, 1, 4, 5, 8, 9, 12, 13, 16, 17, 20, 21, 24, 25, 28, 29]:
                return 0
            elif self.granjero.codigo in [3, 9, 13, 21, 25 ]:
                return 1
            else:
                return 2
        
        elif self.marcador.id == "pala":
            if self.granjero.codigo == 27:
                return 0
            else:
                return 1
        
        elif self.marcador.id == "abono":
            if self.granjero.codigo in range(0, 8) or self.granjero.codigo in range(16, 24):
                return 0
            elif self.granjero.codigo != 19:
                return 1
            else:
                return 2
        
        elif self.marcador.id == "insec":
            if self.granjero.codigo < 16:
                return 0
            elif self.granjero.codigo not in [3, 7, 11, 15, 19, 23, 27]:
                return 1
            elif self.granjero.codigo == 19:
                return 2
            else:
                return 3
        
        elif self.marcador.id in ["abono1", "insect1", "regadera1", "semillas1", "carretilla1"]:
            return 0    
        
        else:
            return 0
            
    def leer_marcador(self):
        """
        Solicita el sintetizador de voz que lea la instrucción correspondiente al marcador donde esta ubicado
        el personaje.
        """
        if not self.leer_ubicacion:
            if self.nivel_actual == 1:
                self.spserver.processtext(self.preguntas.marcas_n1[self.marcador.id][self.det_msj_n1()], self.parent.config.activar_lector)
            elif self.nivel_actual == 2:
                self.spserver.processtext(self.preguntas.marcas_n2[self.marcador.id][self.det_msj_n2()], self.parent.config.activar_lector)
            self.leer_ubicacion = True
            
    def leer_respuestas(self, pregunta, respuestas, repetir = False):
        """
        Solicita al sintetizador de voz que lea una cadena de texto compuesta por: La indicación del elemento
        encontrado, el enunciado y las respuestas posibles.
        @param pregunta: Enunciado correspondiente al objeto encontrado.
        @type pregunta: str
        @param respuestas: Lista de respuestas posibles.
        @type respuestas: list
        @param repetir: Indica si se debe repetir, en caso de que la respuesta sea incorrecta.
        @type repetir: bool
        """
        texto = u""
        for i in respuestas:
            texto += u"opción número:" + i
        if repetir:
            final = u"Selecciona la opción que corresponde al siguiente enunciado: " +  pregunta + u":" + texto
        else:
            final = u"Has encontrado: " + self.sprite.nombre + u"Selecciona la opción que corresponde al siguiente enunciado:" +  pregunta + u":" + texto
        self.spserver.processtext(final, self.parent.config.activar_lector)
        
    def actualizar_pj(self):
        """
        Actualiza la imagen y código del personaje. Elimina el objeto encontrado del grupo de sprites.
        """
        self.granjero.codigo += self.sprite.aumento
        self.preguntas.quitar_pregunta(self.preguntas.valor)
        self.granjero.cambiar_imagen(self.granjero.dic_imagenes[self.granjero.codigo])
        self.grupo_objetos.remove(self.sprite)
        if self.nivel_actual == 1:
            if self.granjero.codigo in [1, 3, 5]:
                self.grupo_marcadores.add(self.sem_rec)
            if self.granjero.codigo in [2, 3, 6]: 
                self.grupo_marcadores.add(self.rega_rec)
                
        if self.nivel_actual == 2:
            if self.granjero.codigo == 0:
                self.grupo_marcadores.add(self.carre_rec)
            if self.granjero.codigo in range(1, 32, 2):
                self.grupo_marcadores.add(self.sem_rec)
            if self.granjero.codigo not in [0, 1, 4, 5, 8, 9, 12, 13, 16, 17, 20, 21, 24, 25, 28, 29]:
                self.grupo_marcadores.add(self.rega_rec)
            if self.granjero.codigo in range(8, 15) or self.granjero.codigo in range(24, 31):
                self.grupo_marcadores.add(self.abono_rec)
            if self.granjero.codigo in range(17, 31):
                self.grupo_marcadores.add(self.insect_rec)
                
    def actualizar_marcadores(self):
        """
        Actualiza la instrucción de los marcadores de posición en función del código del personaje.
        """
        if self.nivel_actual == 1:
            if self.granjero.codigo == 3 and self.m_pala not in self.grupo_marcadores.sprites():
                self.grupo_marcadores.add(self.m_pala)
                [self.limites.remove(i) for i in self.limites.sprites() if i.id == 15]
        elif self.nivel_actual == 2:
            if self.granjero.codigo == 27 and self.m_pala not in self.grupo_marcadores.sprites():
                self.grupo_marcadores.add(self.m_pala)
                [self.limites.remove(i) for i in self.limites.sprites() if i.id == 24]
        
    def mostrar_pregunta(self):
        """
        Muestra un mensaje emergente con el enunciado correspondiente al objeto encontrado.
        En el nivel 2 este mensaje solo aparece si se ha recogido previamente la carretilla.
        """
        if not self.texto_visible:
            if self.granjero.codigo >= 0 or self.sprite.nombre == "la carretilla. ":
                r1 = random.randint(0, len(self.preguntas.nros) - 1)
                aleatorio = self.preguntas.nros[r1]
                self.leer_respuestas(self.preguntas.dic_pre[aleatorio], self.preguntas.dic_res_lector[aleatorio])
                self.preguntas.valor = aleatorio
                self.popup_pregunta = PopUp(self.parent, (self.preguntas.dic_pr[aleatorio]), "Aceptar", 0, self.grupo_popup, 1)
                self.popup_pregunta.agregar_grupo()
                self.texto_visible = True

    def detectar_colision(self):
        """
        Indica si existe una colisión entre el personaje y los objetos que se pueden recoger.
        De esta manera se determina cuando se deben mostrar los mensajes emergentes y cual sera su contenido.
        """
        if self.granjero.rt_car.collidelist(self.grupo_objetos.sprites()) != -1:
            self.sprite = self.grupo_objetos.sprites()[self.granjero.rt_car.collidelist(self.grupo_objetos.sprites())]
            self.choque = True
        else:
            self.choque = False
    
    def colision_marcador(self):
        """
        Indica si existe una colisión entre el personaje y los marcadores de posición.
        De esta manera se determina cuando se debe solicitar al sintetizador de voz que lea las instrucciones
        correspondientes.
        """
        if self.granjero.rect.collidelist(self.grupo_marcadores.sprites()) != -1:
            self.marcador = self.grupo_marcadores.sprites()[self.granjero.rect.collidelist(self.grupo_marcadores.sprites())]
            self.marker = True
        else:
            self.marker = False
    
    def animar_fondo(self):
        """
        Cada vez que la pantalla se actualiza, desplaza ligeramente la posición de la nube para simular un 
        movimiento constante en el fondo.
        """
        self.nubes.rect.move_ip(self.vel_nube, 0)
        if self.nubes.rect.left + self.nubes.rect.width + 100 < 0:
            self.nubes.mover(1024)
            
    def dibujar_rectangulos(self, lista):
        """
        Dibuja los rectángulos de una lista de objetos de la actividad. Permite al programador ubicar 
        facilmente los objetos en la pantalla. 
        @param lista: Una lista de objetos que tengan al menos el atributo rect.
        @type lista: list
        """
        for i in lista:
            pygame.draw.rect(self.visor, (255, 0, 0), i, 1)

    def draw(self):
        """
        Dibuja el fondo de pantalla y los elementos pertenecientes a los grupos de sprites sobre la superficie 
        del manejador de pantallas.
        """
        self.animar_fondo()
        self.raton.update()
        self.visor.blit(self.fondo, (0, 0))
        self.anim_fondo.draw(self.visor)
        self.grupo_imagenes.draw(self.visor)
        self.grupo_objetos.draw(self.visor)
        self.grupo_botones.draw(self.visor)
        self.grupo_personaje.draw(self.visor)
        #self.dibujar_rectangulos(self.grupo_marcadores.sprites())
        #self.dibujar_rectangulos(self.limites.sprites())
        #pygame.draw.rect(self.visor, (255, 0, 0), self.granjero.rt_car, 1)
        #pygame.draw.rect(self.visor, (255, 0, 0), self.granjero.rect, 1)
        #pygame.draw.rect(self.visor, (255, 0, 0), self.meta, 1)
        self.grupo_popup.draw(self.visor)
    
    def start(self):
        pass
    
    def cleanUp(self):
        pass
