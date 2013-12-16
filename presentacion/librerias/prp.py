#!/usr/bin/env python
# -*- coding: utf-8 -*-

class prp():
    """
    Esta clase es una pequeña base de datos de los textos que se manejan en la actividad 1.
    """

    dic_pr = {
    0:(u"    Órgano que fija la planta al suelo y a través de los pelos radicales absorbe los minerales, agua y nutrientes necesarios para la alimentación de la planta y sus frutos. ", u"1. Tallo ", u"2. Flor ", u"3. Raíz "),
    1:(u"    Órgano que transpira, sostiene las hojas y transporta el agua y los minerales desde la raíz mediante un complejo sistema de conductos. ", u"1. Hoja ", u"2. Raíz ", u"3. Tallo "), 
    2:(u"    Órganos que realizan la transformación de los componentes básicos (agua y minerales) en los nutrientes. ", u"1. Hojas ", u"2. Raíz ", u"3. Flor "),
    3:(u"    Órgano reproductor de las plantas. ", u"1. Flor ", u"2. Tallo ", u"3. Hoja "), 
    4:(u"    Proceso que permite a los seres vivos crear otros seres vivos semejantes o iguales a ellos mismos. ", u"1. Acodo ", u"2. Reproducción ", u"3. Injerto "), 
    5:(u"    Reproducción en la cual un sólo organismo da origen a un nuevo ser. ", u"1. Reproducción sexual ", u"2. Reproducción asexual "),
    6:(u"    Reproducción en la cual un nuevo ser se forma por la unión de una célula femenina y una célula masculina. ", u"1. Reproducción sexual ", u"2. Reproducción asexual "), 
    7:(u"    Conjunto de técnicas y conocimientos para cultivar la tierra. ", u"1. Agricultura ", u"2. Siembra ", u"3. Injerto "),
    8:(u"    Proceso mediante el cual se dobla una rama de una planta, se entierra y cuando tenga raíces, se separa de la planta madre. ", u"1. Tipo de reproducción asexual por acodo ", u"2. Unión de células masculinas y células femeninas ", u"3. Tipo de reproducción asexual por injerto "),
    9:(u"    Consiste en introducir un fragmento de tallo de una planta a otra planta, ambas de la misma especie, formando una nueva planta. ",  u"1. Tipo de reproducción asexual por acodo ", u"2. Unión de células masculinas y células femeninas ", u"3. Tipo de reproducción asexual por injerto ")
    }
    """Diccionario que contiene las preguntas y posibles respuestas. """
    
    dic_pre = {
    0:u"    Órgano que fija la planta al suelo y a través de los pelos radicales absorbe los minerales, agua y nutrientes necesarios para la alimentación de la planta y sus frutos. ",
    1:u"    Órgano que transpira, sostiene las hojas y transporta el agua y los minerales desde la raíz mediante un complejo sistema de conductos. ", 
    2:u"    Órganos que realizan la transformación de los componentes básicos (agua y minerales) en los nutrientes. ",
    3:u"    Órgano reproductor de las plantas. ",
    4:u"    Proceso que permite a los seres vivos crear otros seres vivos semejantes o iguales a ellos mismos. ",
    5:u"    Reproducción en la cual un sólo organismo da origen a un nuevo ser. ", 
    6:u"    Reproducción en la cual un nuevo ser se forma por la unión de una célula femenina y una célula masculina. ",
    7:u"    Conjunto de técnicas y conocimientos para cultivar la tierra. ",
    8:u"    Proceso mediante el cual se dobla una rama de una planta, se entierra y cuando tenga raíces, se separa de la planta madre. ",
    9:u"    Consiste en introducir un fragmento de tallo de una planta a otra planta, ambas de la misma especie, formando una nueva planta. "
    }
    """Diccionario que contiene solo las preguntas. """
    
    dic_res = {
    0:(u"1. Tallo ", u"2. Flor. ", u"3. Raíz "), 1:(u"1. Hoja ", u"2. Raíz ", u"3. Tallo "), 2:(u"1. Hojas ", u"2. Raíz ", u"3. Flor "),
    3:(u"1. Flor ", u"2. Tallo. ", u"3. Hoja "), 4:(u"1. Acodo ", u"2. Reproducción ", u"3. Injerto "), 5:(u"1. Reproducción sexual ", u"2. Reproducción asexual "),
    6:(u"1. Reproducción sexual ", u"2. Reproducción asexual "), 7:(u"1. Agricultura ", u"2. Siembra ", u"3. Injerto "),
    8:(u"1. Tipo de reproducción asexual por acodo ", u"2. Unión de células masculinas y células femeninas ", u"3. Tipo de reproducción asexual por injerto "),
    9:(u"1. Tipo de reproducción asexual por acodo ", u"2. Unión de células masculinas y células femeninas ", u"3. Tipo de reproducción asexual por injerto ")
    }
    
    dic_res_lector = {
    0:(u"1. Tallo. ", u"2. Flor. ", u"3. Raíz. "), 1:(u"1. Hoja. ", u"2. Raíz. ", u"3. Tallo. "), 2:(u"1. Hojas. ", u"2. Raíz. ", u"3. Flor. "),
    3:(u"1. Flor. ", u"2. Tallo. ", u"3. Hoja. "), 4:(u"1. Acodo. ", u"2. Reproducción. ", u"3. Injerto. "), 5:(u"1. Reproducción sexual. ", u"2. Reproducción asexual. "),
    6:(u"1. Reproducción sexual. ", u"2. Reproducción asexual. "), 7:(u"1. Agricultura. ", u"2. Siembra. ", u"3. Injerto. "),
    8:(u"1. Tipo de reproducción asexual por acodo. ", u"2. Unión de células masculinas y células femeninas. ", u"3. Tipo de reproducción asexual por injerto. "),
    9:(u"1. Tipo de reproducción asexual por acodo. ", u"2. Unión de células masculinas y células femeninas. ", u"3. Tipo de reproducción asexual por injerto. ")
    }
    
    
    """Diccionario que contiene solo las posibles respuestas. """

    dic_pistas = {
    0:(u"    Recuerda: es un órgano que carece de hojas. ", u"    Recuerda: crece dentro de la tierra. ", u"    ¡Muy bien! Sabías que... el 29 de mayo de 1948 se declara el Araguaney árbol nacional de Venezuela. " ),
    1:(u"    Recuerda: crece en sentido contrario a la raíz. ", u"    Recuerda: de él salen las ramas, las flores y los frutos. ", u"    ¡Excelente! Sabías que... el árbol de Apamate es primo hermano del Araguaney. El color de sus flores varía entre lila y rosado. "),
    2:(u"    ¡Muy bien! El color verde que tienen las hojas es debido a una sustancia llamada clorofila. ", u"    Recuerda: son verdes y salen del tallo. ", u"    Recuerda: son delgadas y su forma es semejante a la de una gota. "),
    3:(u"    ¡Excelente! La Orquídea venezolana es originaria de la Cordillera de la Costa. El 23 de mayo de 1951, por decreto oficial fue declarada como la flor nacional. ", u"    Recuerda: tiene una célula sexual femenina y una célula sexual masculina. ", u"    Recuerda: tienen diferentes colores y formas. "),
    4:(u"    Recuerda: existen 2 tipos y ellas son sexual y asexual. ", u"    ¡Excelente! La reproducción es una de las funciones más importantes de los seres vivos, porque permite la continuidad de las especies. ", u"    Recuerda: la germinación es el proceso por el cual una semilla da origen a un nuevo ser. "),
    5:(u"    Recuerda: este tipo de reproducción puede darse por medio de gajos, estacas o esquejes. ", u"    ¡Muy bien! La yuca se reproduce asexualmente. La yuca es un tubérculo que en nuestro país se da frecuentemente. "),
    6:(u"    ¡Muy bien! El mango es un fruto típico de Venezuela y se reproduce de forma sexual. ", u"    Recuerda: las personas y los animales también se reproducen con la unión de las células masculinas y femeninas. "),
    7:(u"    ¡Excelente! Sabías que... en Venezuela el principal estado productor de maíz es: Portuguesa. ", u"    Recuerda: es necesario el tratamiento de los suelos. ", u"    Recuerda: se desarrolla el cultivo de vegetales. "),    
    8:(u"    ¡Muy bien! Se dice que la mejor época del año para que la reproducción asexual por acodo se produzca es en primavera. ", u"    Recuerda: la madera de la rama debe ser tierna. ", u"    Recuerda: la mora se reproduce poniendo en práctica este método. "),
    9:(u"    Recuerda: este tipo de reproducción permite la creación de una nueva planta con las características de otras 2 plantas. ", u"    Recuerda: esta técnica también sirve para conservar las características de una planta. ", u"    ¡Excelente! Hay dos tipos de injerto ellos son llamados de Púa y de Yema. ")              
    }
    """Diccionario que contiene las pistas de cada pregunta. """ 
    
    r_correcta = { 
    0:u"3. Raíz ", 1:u"3. Tallo ", 2:u"1. Hojas ", 3:u"1. Flor ", 4:u"2. Reproducción ", 5:u"2. Reproducción asexual ", 6:u"1. Reproducción sexual ",
    7:u"1. Agricultura ", 8:u"1. Tipo de reproducción asexual por acodo ", 9:u"3. Tipo de reproducción asexual por injerto "             
    }
    """Diccionario con las respuestas correctas a cada pregunta. """
    
    instruc = {
    0:
    u"    Instrucciones: recolecta todos los elementos necesarios para sembrar plantas. Utiliza " 
    u"TECLADO para desplazarte, por cada elemento selecciona la opción que corresponda a cada "
    u"enunciado utilizando el ratón RATON o pulsando la tecla 1, 2 ó 3 según se te indique. "
    u"Utiliza la tecla ESC para salir. ",
    
    1:
    u"Instrucciones: recolecta todos los elementos necesarios para sembrar plantas. Utiliza " 
    u"las teclas de dirección para desplazarte, por cada elemento selecciona la opción que corresponda a cada "
    u"enunciado utilizando el ratón o pulsando la tecla 1, 2 ó 3 según se te indique. "
    u"Utiliza la tecla escape para salir. Pulsa F1 para iniciar la actividad. ",
    }
    """Diccionario con las instrucciones en texto y audio para el primer nivel. """
    
    marcas_n1 = {
    "semilla":(u"Hacia arriba se encuentra el saco de semillas. ", u"Muévete a la derecha hasta encontrar la regadera. ", u"Hacia la derecha encontrarás el ultimo elemento. "),
    "semilla1": (u"Ya tienes las semillas, baja para continuar",),
    "pala":(u"Hacia abajo encontrarás la pala. ", u""),
    "regadera":(u"Muévete a la derecha hasta encontrar la regadera. ", u"Hacia la izquierda encontrarás las semillas. ", u"Hacia la izquierda encontrarás el ultimo elemento. "),
    "regadera1": (u"Ya tienes la regadera, ve a la izquierda para continuar. ",),
    }
    """Diccionario de los marcadores de posición del primer nivel. """
    
    marcas_n2 = {
    "sem_car":(u"Hacia abajo encontrarás el saco de semillas. ", u"Hacia la derecha encontrarás mas elementos. ", u"Primero debes subir para buscar la carretilla. "),
    "semillas1": (u"Ya tienes las semillas, sube para continuar",),
    "carretilla1":(u"Ya tienes la carretilla, baja para continuar",),
    "regadera1": (u"Ya tienes la regadera, baja para continuar",),
    "insect1": (u"Ya tienes el controlador biológico, baja para continuar",),
    "abono1": (u"Ya tienes el abono, sube para continuar",),
    "regadera":(u"Hacia arriba se encuentra la regadera", u"Hacia la derecha encontrarás otros elementos. ", u"Hacia la izquierda encontrarás las semillas y hacia la derecha otros elementos. "),
    "pala":(u"Hacia abajo encontrarás la pala. ", u"Es recomendable que busques los otros elementos primero. "),   
    "insec":(u"Hacia arriba encontrarás el controlador biológico.  ", u"Hacia la izquierda quedan elementos por recolectar. ", u"Hacia la derecha encontrarás el abono", u"Hacia la izquierda encontrarás el ultimo elemento. " ),
    "abono":(u"Hacia abajo encontrarás el abono.  ", u"Hacia la izquierda quedan elementos sin recolectar. ", u"Hacia la izquierda encontrarás el ultimo elementos. ")
    }
    """Diccionario de los marcadores de posición del segundo nivel. """
    
    valor = 0
    """Indice de la opción seleccionada. """
    
    def __init__(self):
        """Método inicializador de la clase. """
        self.nros = [0,1,2,3,4,5,6,7,8,9]
        
    def quitar_pregunta(self, indice):
        """Elimina una pregunta de la lista, para que no vuelva a salir.
         
        @param indice: Indice de la pregunta que se desea eliminar.
        @type indice: int
        """
        self.nros.remove(indice)
