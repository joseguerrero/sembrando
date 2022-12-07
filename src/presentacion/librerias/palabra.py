#!/usr/bin/env python

import pygame


class palabra(pygame.sprite.Sprite):
    """
    Esta clase implementa palabras, que pueden ser utilizadas para construir textos u otras estructuras
    con las que se desee mostrar información escrita.
    """

    codigo = ""
    """Identificador único de una palabra. """
    palabra = ""
    """Texto que se muestra en pantalla. """
    comparador = ""
    """Variable usada para determinar el tipo de texto que se debe dibujar en pantalla. """
    tipo_objeto = "palabra"
    """Identificador general de esta clase. """
    selec = False
    """Indica que la palabra ha sido seleccionada. """
    definible = False
    """Indica que al hacer click en un 'indice' se mostraran palabras definibles. """
    definicion = False
    """Indica que al hacer click en una 'definición' se mostrara su concepto. """
    interpretable = False
    """Indica que al hacer click sobre una palabra subrayada en los contenidos, se mostrara 
    el interprete virtual o el glosario de terminos. """
    instrucciones = ["Instrucciones:", "Por acodo:", "Por injerto:"]

    entradas = {
        "absorbe": "absorber",
        "absorber": "absorber",
        "célula": "celula",
        "componentes": "componentes",
        "fotosíntesis": "fotosintesis",
        "germinación": "germinacion",
        "minerales": "minerales",
        "nutrientes": "nutrientes",
        "órgano": "organo",
        "órganos": "organo",
        "reproducción asexual": "rasexual",
        "reproducción sexual": "rsexual",
        "transformación": "transformacion",
        "transporta": "transportar",
    }
    """Diccionario que contiene las posibles entradas del glosario de términos, presentes en el contenido 
    del recurso. """
    definiciones = {
        "Absorber": "absorber",
        "Célula": "celula",
        "Componentes": "componentes",
        "Fotosíntesis": "fotosintesis",
        "Germinar": "germinar",
        "Germinación": "germinacion",
        "Mineral": "minerales",
        "Nutriente": "nutrientes",
        "Órgano": "organo",
        "Reproducción asexual": "rasexual",
        "Reproducción sexual": "rsexual",
        "Transformación": "transformacion",
        "Transportar": "transportar",
    }
    """Diccionario que contiene los textos de las definiciones como se deben mostrar en el glosario de términos. """
    indices = ["A", "C", "F", "G", "M", "N", "O", "R", "T"]
    """Lista que contiene los indices del glosario de términos. """
    intercalado = ["RATON", "DIR", "ENTER"]
    """Lista que palabras clave que se sustituirán por imágenes. """
    tipografia = pygame.font.match_font("FreeSans", False, False)
    """Tipografía seleccionada para renderizar el texto. """

    def __init__(self, palabra, size, tipo_texto):
        """
        Método inicializador de la clase.

        @param palabra: Texto que se dibujara en la pantalla.
        @type palabra: str
        @param size: Tamaño de la fuente. Su valor debe estar entre 18 y 22.
        @type size: int
        @param tipo_texto: Tipo de texto que se muestra en pantalla. Puede ser: 'definicion', 'normal',
        'texto_act', 'intercalado', 'instrucción', 'indice', 'definición', 'concepto', 'caja_texto'.
        @type tipo_texto: str
        """
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.size = size
        self.tipo_palabra = tipo_texto
        try:
            self.letras = pygame.font.Font(self.tipografia, size)
        except IOError:
            print("Error al cargar la fuente!")
        self.palabra = palabra
        self.limpiar_comparador(palabra)

        if self.comparador in self.instrucciones:
            self.letras.set_bold(True)

        if self.comparador in self.entradas.keys():
            self.codigo = self.entradas[self.limpiar_palabra(self.palabra)]

        elif self.tipo_palabra == "definicion":
            self.codigo = self.definiciones[self.palabra]

        if self.tipo_palabra == "texto_act":
            self.letras.set_underline(False)
            self.interpretable = False
            self.image = self.letras.render(self.palabra, True, (0, 0, 0))

        elif self.tipo_palabra == "normal":
            if self.comparador in self.entradas.keys():
                self.letras.set_underline(True)
                self.interpretable = True
            else:
                self.letras.set_underline(False)
                self.interpretable = False
            self.image = self.letras.render(self.palabra, True, (0, 0, 0))

        elif self.tipo_palabra == "intercalado":
            if self.comparador in self.intercalado:
                self.letras = pygame.font.Font(self.tipografia, 36)
            self.image = self.letras.render(self.palabra, True, (0, 0, 0))

        elif self.tipo_palabra == "instruccion":
            self.letras.set_underline(False)
            self.interpretable = False
            self.image = self.letras.render(self.palabra, True, (0, 0, 0))

        elif self.tipo_palabra == "indice":
            self.selec = False
            self.letras.set_bold(True)
            if self.comparador in self.indices:
                self.definible = True
                self.image = self.letras.render(self.palabra, True, (122, 140, 31))
            else:
                self.definible = False
                self.image = self.letras.render(self.palabra, True, (60, 36, 21))

        elif self.tipo_palabra == "definicion":
            if self.comparador in self.definiciones.keys():
                if self.selec:
                    self.letras.set_bold(True)
                self.definicion = True
            else:
                self.definicion = False
            self.image = self.letras.render(self.palabra, True, (60, 36, 21))

        elif self.tipo_palabra == "concepto":
            self.image = self.letras.render(self.palabra, True, (60, 36, 21))

        elif self.tipo_palabra == "caja_texto":
            self.image = self.letras.render(self.palabra, True, (60, 36, 21))

        self.image.convert()
        self.rect = self.image.get_rect()

    def get_palabra(self):
        """
        @return: Superficie de la palabra.
        @rtype: pygame.Surface
        """
        return self.image

    def get_rect(self):
        """
        @return: Rectángulo de la superficie.
        @rtype: pygame.Rect
        """
        return self.image.get_rect()

    def negrita(self):
        """
        Redibuja la palabra en negrita.
        """
        if self.selec:
            self.letras.set_bold(True)
            self.image = self.letras.render(self.palabra, True, (60, 36, 21))

    def destacar(self):
        """
        Al hacer click sobre un indice en el glosario de términos redibuja el indice correspondiente,
        destacándolo con otro color y en negrita.
        """
        palabra_limpia = self.palabra.strip(".")
        palabra_limpia = palabra_limpia.strip(",")
        palabra_limpia = palabra_limpia.strip("?")
        if self.tipo_palabra == "indice" and self.selec:
            self.letras = pygame.font.Font(self.tipografia, self.size + 6)
            self.letras.set_bold(True)
            if palabra_limpia in self.indices:
                self.definible = True
                self.image = self.letras.render(self.palabra, True, (122, 140, 31))
            else:
                self.definible = False
                self.image = self.letras.render(self.palabra, True, (60, 36, 21))

    def restaurar(self):
        """
        Redibuja los indices del glosario de términos.
        """
        palabra_limpia = self.palabra.strip(".")
        palabra_limpia = palabra_limpia.strip(",")
        palabra_limpia = palabra_limpia.strip("?")
        if self.tipo_palabra == "indice":
            self.letras = pygame.font.Font(self.tipografia, self.size)
            self.letras.set_bold(True)
            if palabra_limpia in self.indices:
                self.definible = True
                self.image = self.letras.render(self.palabra, True, (122, 140, 31))
            else:
                self.definible = False
                self.image = self.letras.render(self.palabra, True, (60, 36, 21))

    def update(self, tipo_update):
        """
        Restaura los textos de las definiciones a su estado original.
        @param tipo_update: Determina las palabras que serán restauradas. Si su valor es 1 se restauran
        definiciones e indices, si su valor es 2 se restauran solo las definiciones.
        @type tipo_update: int
        """
        palabra_limpia = self.palabra.strip(".")
        palabra_limpia = palabra_limpia.strip(",")
        palabra_limpia = palabra_limpia.strip("?")
        if tipo_update == 1:
            if self.tipo_palabra == "definicion":
                self.selec = False
                self.letras.set_bold(False)
                self.image = self.letras.render(self.palabra, True, (60, 36, 21))
            if self.tipo_palabra == "indice":
                self.letras = pygame.font.Font(self.tipografia, self.size)
                self.letras.set_bold(True)
                if palabra_limpia in self.indices:
                    self.selec = False
                    self.definible = True
                    self.image = self.letras.render(self.palabra, True, (122, 140, 31))
                else:
                    self.definible = False
                    self.image = self.letras.render(self.palabra, True, (60, 36, 21))
        elif tipo_update == 2:
            if self.tipo_palabra == "definicion":
                self.selec = False
                self.letras.set_bold(False)
                self.image = self.letras.render(self.palabra, True, (60, 36, 21))

    def limpiar_comparador(self, comparador):
        """
        Se utiliza para eliminar caracteres no permitidos del comparador.
        """
        self.comparador = comparador.strip(",")
        self.comparador = self.comparador.strip("(")
        self.comparador = self.comparador.strip(")")
        self.comparador = self.comparador.strip("?")
        self.comparador = self.comparador.strip("¿")
        self.comparador = self.comparador.strip("!")
        self.comparador = self.comparador.strip("¡")
        self.comparador = self.comparador.strip(".")

    def limpiar_palabra(self, palabra):
        """
        Se utiliza para eliminar caracteres que no forman parte de la palabra.
        @return: La palabra original sin signos de puntuación adyacentes.
        @rtype: str
        """
        palabra_limpia = palabra.strip(",")
        palabra_limpia = palabra_limpia.strip(")")
        palabra_limpia = palabra_limpia.strip("(")
        palabra_limpia = palabra_limpia.strip("?")
        palabra_limpia = palabra_limpia.strip("¿")
        palabra_limpia = palabra_limpia.strip("!")
        palabra_limpia = palabra_limpia.strip("¡")
        palabra_limpia = palabra_limpia.strip(".")
        return palabra_limpia
