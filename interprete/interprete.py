#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bge import logic
import mathutils
import sys
import configparser

class Vocabulario():
    dic = {}
    diccolor= {}

    def __init__(self):
        """
	    Define los diccionarios con las palabras del intérprete virtual, con sus respectivos nombres de clips de animación y duración. Tambien se definen los colores que utilizará el intérprete virtual.
	    """

        self.dic = {"absorber":("a_absorver", 385+20 ), "rsexual":("a_sexual", 370+20), "rasexual":("a_asexual", 323+20), "fotosintesis":("a_fotosintesis", 1150+20), "celula":("a_celula",1018+20), "componentes" :("a_componentes",350), "germinacion":("a_germinar",367+20), "minerales":("a_minerales",565+20), "nutrientes": ("a_nutrientes",1431+20), "organo":("a_organo",578+20) , "transformacion": ("a_transformacion",441+20),"transportar": ("a_transporte",443+20) }

        self.diccolor = {"0":((1, 0.604, 0, 1), (1, 0.604, 0, 1)), "1":((1.0, 0.09084, 0.319, 1),(0.212, 0.002428, 0.03434, 1)), "2":((0.242, 0.73, 0.242, 1),(0.03955, 0.631, 0.209, 1))}

    def Consultar(self, palabra):
        """
        Retorna el nombre del clip de animación y la duración de las palabras.
        
        @param palabra: Cadena de texto a identificar.
        @type palabra: str
        
        @return: Conjunto de valores con la siguiente estructura: (nombre_del_clip, duración). 
        @rtype: tuple
        """
        tupla = self.dic[palabra]
        return tupla

    def consultarcolor(self,color):
        """
    	Define el color a usar en el intérprete virtual.
    
    	@param color: Representado por los valores 1,2,3.
    	@type color: int
    
    	@return: Conjunto de valores con la siguiente estructura: (nombre_del_clip, duración). 
    	@rtype: tuple
    	"""
        tupla = self.diccolor[color]
        return tupla

class Interprete():
    genero = "Mujer"
    palabra = "celula"
    color = ""
    velocidad = 1
    voc = Vocabulario()

    def __init__(self): 
        """
    	Inicializa las variables y objetos.
    	"""
        config = configparser.RawConfigParser()
        config.read("gamemanager/interprete/config.ini")
        config.read("config.ini")      
        #cambiar a "interprete/config.ini" para que funcione con el ReDA
        
        self.palabra = sys.argv[-1]
        self.velocidad = float(sys.argv[-2])
        self.genero = sys.argv[-3]
        self.color = sys.argv[-4]        
        self.scena = logic.getCurrentScene()
        self.controlador = logic.getCurrentController()
        self.Cont = self.controlador.owner

    def play(self):
        """
    	Ejecuta el clip de animación. Es usado por la aplicación BlenderPlayer.
    	"""
        cotas = self.voc.Consultar(self.palabra)
        self.Cont.playAction(cotas[0], 0, cotas[1], layer=0, priority=0, blendin=0, play_mode=logic.KX_ACTION_MODE_PLAY, layer_weight=0.0, ipo_flags=0, speed=self.velocidad)
    
    def Interpretar(self):
        """
    	Define el color del intérprete con su respectivo genero. Ejecuta el método play()
    	"""
        colorX = self.voc.consultarcolor(self.color)
        self.scena.objects["camisaM"].color = colorX[0]
        self.scena.objects["camisaH"].color = colorX[1]
        actuador = self.controlador.actuators["Genero"]
        actuador.camera = self.genero
        self.play()

    def Repetir(self):
        """
    	Ejecuta el metodo play()	
    	"""
        self.play()

    def mover_palabra(self):
        """
    	Dependiendo del genero seleccionado ubica las imágenes de la palabra a reproducir en una posición especifica.
    	"""
        palabra = self.scena.objects[self.palabra] # define el objeto q se movera (palabra)
        if self.genero == "Mujer":
            palabra.worldPosition = (-0.68,0,3.4)
        else:
            palabra.worldPosition = (-0.68,0,0.4)

def main(): 
    """
    Inicializa el intérprete. Es necesario ejecutar los metodos interpretar() y mover_palabra().
    """
    interprete = Interprete()
    interprete.Interpretar()
    interprete.mover_palabra()

def repetir(self):

    """
    Repite la animacion del clip de animación.
    """
    interprete = Interprete()
    scena = logic.getCurrentScene()
    obj = scena.objects["repetir"]
    cont = logic.getCurrentController()
    owner = cont.owner
    click = cont.sensors["click"]
    over = cont.sensors["over"]

    if interprete.genero == "Hombre":
        obj.worldPosition = (0.29,-0.72,-0.3)
        #scena.objects["mostrar_palabra"].worldPosition = (0.19,0,-0.607)
        #palabra.worldPosition = (-0.68,0,0.4)

    if interprete.genero == "Mujer":
        obj.worldPosition = (0.29,-0.72,2.71)
        #scena.objects["mostrar_palabra"].worldPosition = (0.19,0,2.4)
        #palabra.worldPosition = (-0.68,0,3.4)

    if click.positive and over.positive:
        carried_object = over.hitObject
        print  (carried_object.name)
        if carried_object.name == "repetir":
            interprete.Repetir()     
    else:
        carried_object = "none"

def mover_palabra(self):
    """
    Dependiendo del genero seleccionado ubica las imagenes de la palabra a reproducir en una posición especifica.
    """
    interprete = Interprete()
    scena = logic.getCurrentScene()
    #scena.objects[interprete.palabra].worldPosition = (100,100,0)
    
main()
