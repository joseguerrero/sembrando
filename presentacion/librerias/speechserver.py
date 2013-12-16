#!/usr/bin/env python
# -*- coding: utf-8 -*-
import speechd, subprocess
from manejador import Manejador as parent

class Speechserver():
    """
    Esta clase implementa una sencilla interfaz para acceder al sintetizador de voz "Espeak".
    """
    def __init__(self):
        """
        Método inicializador de la clase.
        """
        self.parent = parent
        self.dic_vel = {"baja": 0, "media": 25, "rapida": 50}
        self.speaker = speechd.Speaker('SERVERSPEECH')
        self.speaker.set_punctuation(speechd.PunctuationMode.NONE)
        self.speaker.set_language("es")
        self.actualizar_servidor()
        self.hablando = False
        self.ultima_lectura = ""
            
    def actualizar_servidor(self):
        """
        Consulta el valor de la velocidad del sintetizador.
        """
        self.speaker.set_rate(self.dic_vel[self.parent.config.synvel])
             
    def processtext2(self, texto, lector_activo):
        """
        Enviá información al sintetizador de voz para que este la procese y permite encolar las peticiones.
        
        @param texto: El texto que se desea enviar al sintetizador.
        @type texto: str
        @param lector_activo: Indica si el sintetizador de voz esta activado.
        @type lector_activo: bool
        """        
        if lector_activo:
            self.data = texto.encode("utf-8")          
            self.speaker.speak(self.data)
    
    def processtext(self, texto, lector_activo, continuar = True):
        """
        Enviá información al sintetizador de voz para que este la procese. No permite encolar peticiones.
        
        @param texto: El texto que se desea enviar al sintetizador.
        @type texto: str
        @param lector_activo: Indica si el sintetizador de voz esta activado.
        @type lector_activo: bool
        @param continuar: Se supone que debe permitir encolar peticiones.
        @type continuar: bool
        @bug: Aún no se ha logrado implementar un método único que permita activar y desactivar
        las peticiones en cola.
        """
        self.ultima_lectura = texto
        if lector_activo:
            if self.hablando and continuar:
                self.stopserver()
            self.data = texto.encode("utf-8")          
            self.speaker.speak(self.data)
            self.hablando = True
            
    def stopserver(self):
        """
        Detiene el sintetizador de voz.
        """
        self.speaker.stop()
        self.hablando = False
    
    def repetir(self):
        self.stopserver()
        self.speaker.speak(self.data)
        
    def quitserver(self):
        """
        Cierra la conexión con el sintetizador de voz.
        """
        self.speaker.close()
        subprocess.call(['pkill', '-9', 'speech-dispatcher'])
