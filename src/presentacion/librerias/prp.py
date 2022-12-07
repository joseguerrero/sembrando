#!/usr/bin/env python


class prp:
    """
    Esta clase es una pequeña base de datos de los textos que se manejan en la actividad 1.
    """

    dic_pr = {
        0: (
            "    Órgano que fija la planta al suelo y a través de los pelos radicales absorbe los minerales, agua y nutrientes necesarios para la alimentación de la planta y sus frutos. ",
            "1. Tallo ",
            "2. Flor ",
            "3. Raíz ",
        ),
        1: (
            "    Órgano que transpira, sostiene las hojas y transporta el agua y los minerales desde la raíz mediante un complejo sistema de conductos. ",
            "1. Hoja ",
            "2. Raíz ",
            "3. Tallo ",
        ),
        2: (
            "    Órganos que realizan la transformación de los componentes básicos (agua y minerales) en los nutrientes. ",
            "1. Hojas ",
            "2. Raíz ",
            "3. Flor ",
        ),
        3: (
            "    Órgano reproductor de las plantas. ",
            "1. Flor ",
            "2. Tallo ",
            "3. Hoja ",
        ),
        4: (
            "    Proceso que permite a los seres vivos crear otros seres vivos semejantes o iguales a ellos mismos. ",
            "1. Acodo ",
            "2. Reproducción ",
            "3. Injerto ",
        ),
        5: (
            "    Reproducción en la cual un sólo organismo da origen a un nuevo ser. ",
            "1. Reproducción sexual ",
            "2. Reproducción asexual ",
        ),
        6: (
            "    Reproducción en la cual un nuevo ser se forma por la unión de una célula femenina y una célula masculina. ",
            "1. Reproducción sexual ",
            "2. Reproducción asexual ",
        ),
        7: (
            "    Conjunto de técnicas y conocimientos para cultivar la tierra. ",
            "1. Agricultura ",
            "2. Siembra ",
            "3. Injerto ",
        ),
        8: (
            "    Proceso mediante el cual se dobla una rama de una planta, se entierra y cuando tenga raíces, se separa de la planta madre. ",
            "1. Tipo de reproducción asexual por acodo ",
            "2. Unión de células masculinas y células femeninas ",
            "3. Tipo de reproducción asexual por injerto ",
        ),
        9: (
            "    Consiste en introducir un fragmento de tallo de una planta a otra planta, ambas de la misma especie, formando una nueva planta. ",
            "1. Tipo de reproducción asexual por acodo ",
            "2. Unión de células masculinas y células femeninas ",
            "3. Tipo de reproducción asexual por injerto ",
        ),
    }
    """Diccionario que contiene las preguntas y posibles respuestas. """

    dic_pre = {
        0: "    Órgano que fija la planta al suelo y a través de los pelos radicales absorbe los minerales, agua y nutrientes necesarios para la alimentación de la planta y sus frutos. ",
        1: "    Órgano que transpira, sostiene las hojas y transporta el agua y los minerales desde la raíz mediante un complejo sistema de conductos. ",
        2: "    Órganos que realizan la transformación de los componentes básicos (agua y minerales) en los nutrientes. ",
        3: "    Órgano reproductor de las plantas. ",
        4: "    Proceso que permite a los seres vivos crear otros seres vivos semejantes o iguales a ellos mismos. ",
        5: "    Reproducción en la cual un sólo organismo da origen a un nuevo ser. ",
        6: "    Reproducción en la cual un nuevo ser se forma por la unión de una célula femenina y una célula masculina. ",
        7: "    Conjunto de técnicas y conocimientos para cultivar la tierra. ",
        8: "    Proceso mediante el cual se dobla una rama de una planta, se entierra y cuando tenga raíces, se separa de la planta madre. ",
        9: "    Consiste en introducir un fragmento de tallo de una planta a otra planta, ambas de la misma especie, formando una nueva planta. ",
    }
    """Diccionario que contiene solo las preguntas. """

    dic_res = {
        0: ("1. Tallo ", "2. Flor. ", "3. Raíz "),
        1: ("1. Hoja ", "2. Raíz ", "3. Tallo "),
        2: ("1. Hojas ", "2. Raíz ", "3. Flor "),
        3: ("1. Flor ", "2. Tallo. ", "3. Hoja "),
        4: ("1. Acodo ", "2. Reproducción ", "3. Injerto "),
        5: ("1. Reproducción sexual ", "2. Reproducción asexual "),
        6: ("1. Reproducción sexual ", "2. Reproducción asexual "),
        7: ("1. Agricultura ", "2. Siembra ", "3. Injerto "),
        8: (
            "1. Tipo de reproducción asexual por acodo ",
            "2. Unión de células masculinas y células femeninas ",
            "3. Tipo de reproducción asexual por injerto ",
        ),
        9: (
            "1. Tipo de reproducción asexual por acodo ",
            "2. Unión de células masculinas y células femeninas ",
            "3. Tipo de reproducción asexual por injerto ",
        ),
    }

    dic_res_lector = {
        0: ("1. Tallo. ", "2. Flor. ", "3. Raíz. "),
        1: ("1. Hoja. ", "2. Raíz. ", "3. Tallo. "),
        2: ("1. Hojas. ", "2. Raíz. ", "3. Flor. "),
        3: ("1. Flor. ", "2. Tallo. ", "3. Hoja. "),
        4: ("1. Acodo. ", "2. Reproducción. ", "3. Injerto. "),
        5: ("1. Reproducción sexual. ", "2. Reproducción asexual. "),
        6: ("1. Reproducción sexual. ", "2. Reproducción asexual. "),
        7: ("1. Agricultura. ", "2. Siembra. ", "3. Injerto. "),
        8: (
            "1. Tipo de reproducción asexual por acodo. ",
            "2. Unión de células masculinas y células femeninas. ",
            "3. Tipo de reproducción asexual por injerto. ",
        ),
        9: (
            "1. Tipo de reproducción asexual por acodo. ",
            "2. Unión de células masculinas y células femeninas. ",
            "3. Tipo de reproducción asexual por injerto. ",
        ),
    }

    """Diccionario que contiene solo las posibles respuestas. """

    dic_pistas = {
        0: (
            "    Recuerda: es un órgano que carece de hojas. ",
            "    Recuerda: crece dentro de la tierra. ",
            "    ¡Muy bien! Sabías que... el 29 de mayo de 1948 se declara el Araguaney árbol nacional de Venezuela. ",
        ),
        1: (
            "    Recuerda: crece en sentido contrario a la raíz. ",
            "    Recuerda: de él salen las ramas, las flores y los frutos. ",
            "    ¡Excelente! Sabías que... el árbol de Apamate es primo hermano del Araguaney. El color de sus flores varía entre lila y rosado. ",
        ),
        2: (
            "    ¡Muy bien! El color verde que tienen las hojas es debido a una sustancia llamada clorofila. ",
            "    Recuerda: son verdes y salen del tallo. ",
            "    Recuerda: son delgadas y su forma es semejante a la de una gota. ",
        ),
        3: (
            "    ¡Excelente! La Orquídea venezolana es originaria de la Cordillera de la Costa. El 23 de mayo de 1951, por decreto oficial fue declarada como la flor nacional. ",
            "    Recuerda: tiene una célula sexual femenina y una célula sexual masculina. ",
            "    Recuerda: tienen diferentes colores y formas. ",
        ),
        4: (
            "    Recuerda: existen 2 tipos y ellas son sexual y asexual. ",
            "    ¡Excelente! La reproducción es una de las funciones más importantes de los seres vivos, porque permite la continuidad de las especies. ",
            "    Recuerda: la germinación es el proceso por el cual una semilla da origen a un nuevo ser. ",
        ),
        5: (
            "    Recuerda: este tipo de reproducción puede darse por medio de gajos, estacas o esquejes. ",
            "    ¡Muy bien! La yuca se reproduce asexualmente. La yuca es un tubérculo que en nuestro país se da frecuentemente. ",
        ),
        6: (
            "    ¡Muy bien! El mango es un fruto típico de Venezuela y se reproduce de forma sexual. ",
            "    Recuerda: las personas y los animales también se reproducen con la unión de las células masculinas y femeninas. ",
        ),
        7: (
            "    ¡Excelente! Sabías que... en Venezuela el principal estado productor de maíz es: Portuguesa. ",
            "    Recuerda: es necesario el tratamiento de los suelos. ",
            "    Recuerda: se desarrolla el cultivo de vegetales. ",
        ),
        8: (
            "    ¡Muy bien! Se dice que la mejor época del año para que la reproducción asexual por acodo se produzca es en primavera. ",
            "    Recuerda: la madera de la rama debe ser tierna. ",
            "    Recuerda: la mora se reproduce poniendo en práctica este método. ",
        ),
        9: (
            "    Recuerda: este tipo de reproducción permite la creación de una nueva planta con las características de otras 2 plantas. ",
            "    Recuerda: esta técnica también sirve para conservar las características de una planta. ",
            "    ¡Excelente! Hay dos tipos de injerto ellos son llamados de Púa y de Yema. ",
        ),
    }
    """Diccionario que contiene las pistas de cada pregunta. """

    r_correcta = {
        0: "3. Raíz ",
        1: "3. Tallo ",
        2: "1. Hojas ",
        3: "1. Flor ",
        4: "2. Reproducción ",
        5: "2. Reproducción asexual ",
        6: "1. Reproducción sexual ",
        7: "1. Agricultura ",
        8: "1. Tipo de reproducción asexual por acodo ",
        9: "3. Tipo de reproducción asexual por injerto ",
    }
    """Diccionario con las respuestas correctas a cada pregunta. """

    instruc = {
        0: "    Instrucciones: recolecta todos los elementos necesarios para sembrar plantas. Utiliza "
        "TECLADO para desplazarte, por cada elemento selecciona la opción que corresponda a cada "
        "enunciado utilizando el ratón RATON o pulsando la tecla 1, 2 ó 3 según se te indique. "
        "Utiliza la tecla ESC para salir. ",
        1: "Instrucciones: recolecta todos los elementos necesarios para sembrar plantas. Utiliza "
        "las teclas de dirección para desplazarte, por cada elemento selecciona la opción que corresponda a cada "
        "enunciado utilizando el ratón o pulsando la tecla 1, 2 ó 3 según se te indique. "
        "Utiliza la tecla escape para salir. Pulsa F1 para iniciar la actividad. ",
    }
    """Diccionario con las instrucciones en texto y audio para el primer nivel. """

    marcas_n1 = {
        "semilla": (
            "Hacia arriba se encuentra el saco de semillas. ",
            "Muévete a la derecha hasta encontrar la regadera. ",
            "Hacia la derecha encontrarás el ultimo elemento. ",
        ),
        "semilla1": ("Ya tienes las semillas, baja para continuar",),
        "pala": ("Hacia abajo encontrarás la pala. ", ""),
        "regadera": (
            "Muévete a la derecha hasta encontrar la regadera. ",
            "Hacia la izquierda encontrarás las semillas. ",
            "Hacia la izquierda encontrarás el ultimo elemento. ",
        ),
        "regadera1": ("Ya tienes la regadera, ve a la izquierda para continuar. ",),
    }
    """Diccionario de los marcadores de posición del primer nivel. """

    marcas_n2 = {
        "sem_car": (
            "Hacia abajo encontrarás el saco de semillas. ",
            "Hacia la derecha encontrarás mas elementos. ",
            "Primero debes subir para buscar la carretilla. ",
        ),
        "semillas1": ("Ya tienes las semillas, sube para continuar",),
        "carretilla1": ("Ya tienes la carretilla, baja para continuar",),
        "regadera1": ("Ya tienes la regadera, baja para continuar",),
        "insect1": ("Ya tienes el controlador biológico, baja para continuar",),
        "abono1": ("Ya tienes el abono, sube para continuar",),
        "regadera": (
            "Hacia arriba se encuentra la regadera",
            "Hacia la derecha encontrarás otros elementos. ",
            "Hacia la izquierda encontrarás las semillas y hacia la derecha otros elementos. ",
        ),
        "pala": (
            "Hacia abajo encontrarás la pala. ",
            "Es recomendable que busques los otros elementos primero. ",
        ),
        "insec": (
            "Hacia arriba encontrarás el controlador biológico.  ",
            "Hacia la izquierda quedan elementos por recolectar. ",
            "Hacia la derecha encontrarás el abono",
            "Hacia la izquierda encontrarás el ultimo elemento. ",
        ),
        "abono": (
            "Hacia abajo encontrarás el abono.  ",
            "Hacia la izquierda quedan elementos sin recolectar. ",
            "Hacia la izquierda encontrarás el ultimo elementos. ",
        ),
    }
    """Diccionario de los marcadores de posición del segundo nivel. """

    valor = 0
    """Indice de la opción seleccionada. """

    def __init__(self):
        """Método inicializador de la clase."""
        self.nros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def quitar_pregunta(self, indice):
        """Elimina una pregunta de la lista, para que no vuelva a salir.

        @param indice: Indice de la pregunta que se desea eliminar.
        @type indice: int
        """
        self.nros.remove(indice)
