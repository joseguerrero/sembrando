#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pygame

class ManejadorEventos():
    def __init__(self):
        """
        Método inicializador de la clase.
        """
        self.keyspressed = []
        self.keys = []
        self.mods = []

    def update(self):
        """
        Obtiene la lista de los eventos actuales y determina que teclas estan siendo presionadas.
        """
        self.event = pygame.event.get()
        for event in self.event:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key not in self.keys:
                    self.keys.append(event.key)
            if event.type == pygame.KEYUP:
                if event.key in self.keys:
                    self.keys.remove(event.key)
        self.get_pressed()

    def get_pressed(self):
        """
        Obtiene la lista de teclas que se están presionando así como la lista de modificadores usados.
        """
        self.keyspressed = pygame.key.get_pressed()
        self.mods = pygame.key.get_mods()

    def pressed(self, key):
        """
        Verifica si una tecla especifica esta fue pulsada.
        
        @return: True si la tecla fue pulsada, de lo contrario False.
        @rtype: bool
        """
        if key in self.keys:
            return True
        else:
            return False
    
    def held(self, key):
        """
        Verifica si una tecla especifica se mantiene pulsada.
        
        @return: True si la tecla se mantiene pulsada, de lo contrario False.
        @rtype: bool
        """
        
        if self.keyspressed[key]:
            return True
        else:
            return False
    
    def modded(self, key):
        """
        Verifica si una tecla especifica fue pulsada conjuntamente con una tecla modificadora.
        
        @return: True si la tecla fue pulsada conjuntamente con un modificador, de lo contrario False.
        @rtype: bool
        """
        if self.mods&key:
            return True
        else:
            return False