#!/usr/bin/env python

from pygame import event
from manejador import Manejador
from paginas import menucfg

def main():
    game = Manejador('Sembrando para el  futuro', (1024, 572), False)
    game.changeState(menucfg.estado(game))
    while game.running:
        game.handleEvents(event.get())
        game.update()
        game.draw()
    game.cleanUp()

main()
