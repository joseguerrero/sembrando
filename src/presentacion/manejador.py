#!/usr/bin/env python

import os
import gc
import sys
import json
import pygame
import subprocess

from librerias.singleton import Singleton
from librerias.magnificador import Rendermag
from librerias.configuracion import configuracion

class Manejador(object):
    """
    Esta clase consiste en una implementación del patrón estrategia para python. 
    La instancia de esta clase funciona como un manejador de estados y permite hacer cambios entre pantallas
    que comparten la misma estructura, atributos y métodos.
    """
    __metaclass__ = Singleton
    habilitar = False
    VOLVER_PANTALLA_PREVIA = False
    config = configuracion()
    grupo_magnificador = Rendermag()
    rutas_int = ["/opt/blender/blenderplayer", "blenderplayer", "/usr/bin/blenderplayer"]
    
    def __init__(self, titulo, size = (1024, 572), fullscreen = False):
        """
        Método inicializador de la clase.
        
        @param titulo: Define el titulo que aparecera en la ventana de la aplicación.
        @type titulo: str
        @param size: Indica la resolución de la ventana de la aplicación. Por defecto es (1024x572).
        @type size: tuple
        @param fullscreen: Si es True la aplicación se mostrara en pantalla completa, si es False en una ventana.
        @type fullscreen: bool
        """
        pygame.init()
        self.primera_vez = True
        self.animacion = 0
        self.pantalla = 0
        self.states = []
        self.running = True
        self.screen = pygame.display.set_mode(size)
        self.load_text_content()
        pygame.display.set_caption(titulo)
    icon = pygame.image.load("../iconos/sembrando96x96.png")
    pygame.display.set_icon(icon)
 
    def cleanUp (self):
        """
        Limpia los elementos de las pantallas que esten cargadas, desconecta el servicio del sintetizador de voz
        verifica si blenderplayer esta activo, de ser asi lo cierra y finalmente cierra la aplicación.
        """
        self.states[-1].spserver.stopserver()
        self.states[-1].spserver.quitserver()
        while len(self.states) > 0:
            state = self.states.pop()
            state.cleanUp()
        if not subprocess.call(["pgrep", "blenderplayer"]):
            subprocess.call(["pkill", "-9", "blenderplayer"])
        print("Cerrando servidor de texto a voz") 
        sys.exit(0)
        print("Cerrando Sembrando para el futuro")
        
    def changeState (self, gameState):
        """
        Limpia los elementos de la pantalla actual y carga una nueva pantalla.
        @param gameState: Pantalla que se desea cargar.
        @type gameState: estado
        """
        if len(self.states) > 0:
            state = self.states.pop()
            state.cleanUp()
        self.states.append(gameState)
        self.states[-1].start()
        gc.collect()
 
    def pushState(self, gameState):
        """
        Carga los elementos de una nueva pantalla sin limpiar la pantalla actual.
        @param gameState: Pantalla que se desea cargar.
        @type gameState: estado
        """
        if len(self.states) > 0:
            self.states[-1].pause()
        self.states.append(gameState)
        self.states[-1].start()

    def popState(self):
        """
        Limpia los elementos de la pantalla actual.
        """
        if len(self.states) > 0:
            state = self.states.pop()
            state.cleanUp()
        if len(self.states) > 0:
            self.states[-1].resume()

    def handleEvents(self, events):
        """
        LLama al metodo handleEvents() de la pantalla actual y le envia los eventos que se estan generando.
        @param events: Lista de eventos que se generan cada vez que la pantalla se acutaliza.
        @type events: pygame.event.Event
        """
        self.states[-1].handleEvents(events)
 
    def update(self):
        """
        LLama al metodo update() de la pantalla actual.
        """
        self.states[-1].update()
 
    def draw(self):
        """
        LLama al metodo draw() de la pantalla actual y mantiene la aplicación actualizandose a 30 imágenes
        por segundo.
        """
        self.states[-1].draw()
        self.states[-1].reloj.tick(30)
        pygame.display.flip()
        
    def quit(self):
        """
        Indica que se debe cerrar la aplicación.
        """
        self.running = False
        
    def interpretar(self, codigo):
        """
        Si el intérprete virtual esta activado, abrira un subproceso que ejecuta la aplicación Blenderplayer.
        Al momento de llamar a blenderplayer, se le envia la configuración del intérprete virtual y la palabra
        que se desea intérpretar. Se hace un llamado a la aplicación Wmctrl para ubicar la ventana de blenderplayer
        por encima de la ventana del recurso.
        Si el intérprete esta desactivado se mostrara la pantalla del glósario de términos con la definición
        correspondiente.
        """
        if self.config.disc_audi == True:
            running = subprocess.call(["pgrep", "blenderplayer"])
            if running == 1:
                self.config.consultar()
                
                if os.path.isdir("../interprete/__pycache__"):
                    print("Borrando cache del interprete")
                    if os.path.isfile("../interprete/__pycache__/interprete.cpython-32.pyc"):
                        os.remove("../interprete/__pycache__/interprete.cpython-32.pyc")
                    os.removedirs("../interprete/__pycache__")
                
                #subprocess.call(["rm", "-r", "../interprete/__pycache__"])
                for ruta in self.rutas_int:
                    try:
                        subprocess.Popen([ruta, "-w", "512", "372", "512", "0", "../interprete/interprete.blend", "-", str(self.config.color), str(self.config.genero), str(self.config.velocidad), str(codigo)])
                        pygame.time.delay(2000)
                        subprocess.call(["wmctrl", "-a", "interprete", "-b", "add,above"])
                        break
                    except:
                        print("No se ha podido cargar el interprete virtual.")
            else:
                print("Blenderplayer ya se encuentra en ejecucion")
        else:
            self.config.definicion = codigo
            self.states[-1].portada_glosario = False
            self.states[-1].limpiar_grupos()
            self.states[-1].ir_glosario()

    def load_text_content(self):
        with open('paginas/text/content.json') as f:
            self.text_content  = json.load(f)
