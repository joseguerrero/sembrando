#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import cProfile

import pygame
from manejador import Manejador
from paginas import menucfg

def main():
    game = Manejador('Sembrando para el  futuro', (1024, 572), False)
    game.changeState(menucfg.estado(game))
    while game.running:
        game.handleEvents(pygame.event.get())
        game.update()
        game.draw()
    game.cleanUp()

#cProfile.run('main()')
main()
