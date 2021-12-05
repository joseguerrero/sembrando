#!/usr/bin/env python

class Singleton(type):
    """
    Implementación del patrón singleton para python. 
    """
    def __init__(self, name, bases, dic):
        """
        Método inicializador de la clase.
        """
        super(Singleton, self).__init__(name, bases, dic)
        self.instance = None

    def __call__(self, *args, **kw):
        """
        Verifica si la clase no ha sido instanciada, se ser así, la instancia con los parámetros recibidos.
        Si la clase ya ha sido instanciada no tiene efecto.
        
        @return: La instancia de la clase.
        """
        if self.instance is None:
            self.instance = super(Singleton, self).__call__(*args, **kw)
        return self.instance