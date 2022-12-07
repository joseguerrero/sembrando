#!/usr/bin/env python


class configuracion:
    """
    Esta clase cumple la función de una base de datos o fichero de configuración, donde se almacenan de
    manera temporal las preferencias de uso del ReDA.
    """

    color = 0
    """Indica el color de la camisa del interprete, sus posibles valores son 0, 1 y 2. value: 0"""
    ubx = 499
    """Guarda la ubicación del selector de la velocidad del interprete del menú de configuración visual."""
    vel_anim = 4
    """Guarda la velocidad de la animación del interprete virtual del menú de configuración visual."""
    t_fuente = 18
    """Indica el tamaño actual de la fuente utilizada en todo el recurso."""
    velocidad = 0.5
    """Indica el valor de velocidad que se enviara al interprete virtual."""
    audio = False
    """Indica si el sonido esta activado/desactivado."""
    cache = False
    """Indica si existe una configuración guardada."""
    disc_vis = False
    """Indica si el lector de pantalla esta activado/desactivado."""
    disc_audi = False
    """Indica si el interprete virtual esta activado/desactivado."""
    texto_cambio = False
    """Indica si se ha cambiado el tamaño del texto recientemente."""
    magnificador = False
    """Indica si el magnificador esta activado/desactivado."""
    activar_lector = False
    """Indica lo mismo que disc_vis. Hay que revisar cual es el que se esta usando o cual es 
    la diferencia."""
    genero = ""
    """Indica el género del interprete virtual."""
    synvel = "baja"
    """Indica la velocidad del lector de pantalla, sus posibles valores son 'baja', 'media' y 'alta'."""
    definicion = ""
    """Guarda el valor de la palabra seleccionada para mostrar en el glosario."""

    visit = {"p0": False, "p2": False}
    """Diccionario que registra las visitas a las pantallas del recurso."""

    preferencias = {
        "color": 0,
        "ubx": 499,
        "vel_anim": 4,
        "t_fuente": 18,
        "velocidad": 0.5,
        "audio": False,
        "cache": False,
        "disc_audi": False,
        "disc_vis": False,
        "texto_cambio": False,
        "magnificador": False,
        "activar_lector": False,
        "genero": "",
        "synvel": "baja",
        "definicion": "",
    }
    """Diccionario que almacena las preferencias mientras el ReDA este cargado en memoria."""

    def consultar(self):
        """
        Carga la ultima configuración utilizada o la configuración por defecto.
        """
        self.ubx = self.preferencias["ubx"]
        self.t_fuente = self.preferencias["t_fuente"]
        self.vel_anim = self.preferencias["vel_anim"]
        self.velocidad = self.preferencias["velocidad"]
        self.color = self.preferencias["color"]
        self.cache = self.preferencias["cache"]
        self.disc_audi = self.preferencias["disc_audi"]
        self.disc_vis = self.preferencias["disc_audi"]
        self.texto_cambio = self.preferencias["texto_cambio"]
        self.audio = self.preferencias["audio"]
        self.genero = self.preferencias["genero"]
        self.definicion = self.preferencias["definicion"]
        self.synvel = self.preferencias["synvel"]
        self.magnificador = self.preferencias["magnificador"]
        self.activar_lector = self.preferencias["activar_lector"]

    def guardar_preferencias(self):
        """
        Guarda las preferencias actuales.
        """
        self.preferencias["ubx"] = self.ubx
        self.preferencias["t_fuente"] = self.t_fuente
        self.preferencias["vel_anim"] = self.vel_anim
        self.preferencias["velocidad"] = self.velocidad
        self.preferencias["color"] = self.color
        self.preferencias["cache"] = self.cache
        self.preferencias["disc_audi"] = self.disc_audi
        self.preferencias["disc_vis"] = self.disc_vis
        self.preferencias["texto_cambio"] = self.texto_cambio
        self.preferencias["audio"] = self.audio
        self.preferencias["genero"] = self.genero
        self.preferencias["definicion"] = self.definicion
        self.preferencias["synvel"] = self.synvel
        self.preferencias["magnificador"] = self.magnificador
        self.preferencias["activar_lector"] = self.activar_lector

    def cargar_default(self):
        """
        Carga valores por defecto para la animación del intérprete en el menú de configuración auditiva.
        """
        self.vel_anim = 4
        self.velocidad = 0.5
