#!/usr/bin/env python
# -*- coding: utf-8 -*-
def _pixelPerfectCollisionDetection(sp1, sp2):
    """
    Método interno utilizado para la detección de colisiones perfect pixel.
    @param sp1: Sprite numero 1.
    @type sp1: pygame.sprite.Sprite
    @param sp2: Sprite numero 2.
    @type sp2: pygame.sprite.Sprite
    @return: 1 si se encuentra alguna colisión, 0 si no se detectan colisiones.
    @rtype: bool
    """
    rect1 = sp1.rect;     
    rect2 = sp2.rect;                            
    rect  = rect1.clip(rect2) 
    hm1 = sp1.hitmask
    hm2 = sp2.hitmask
    x1 = rect.x-rect1.x
    y1 = rect.y-rect1.y
    x2 = rect.x-rect2.x
    y2 = rect.y-rect2.y
    for r in range(0,rect.height):      
        for c in range(0,rect.width):
            if hm1[c+x1][r+y1] & hm2[c+x2][r+y2]:
                return True
    return False

def spritecollide_pp(sprite, group):
    """
    Detecta colisiones por pixel entre un sprite y un grupo de sprites dados, lo cual retorna una lista
    de todos los sprites que chocan con el sprite.
    Todos los sprites deben tener un valor "hitmap", que es un arreglo bidimensional que contiene valores 
    mayores a cero para todos los pixeles que pueden chocar. El arreglo bidimensional "hitmap" puede ser
    definido usando pygame.surfarray.array_colorkey() o pygame.surfarray.array_alpha().
    Todos los sprites deben tener un rectángulo del área del sprite. Si el argumento 'dokill' es True, los 
    sprites que choquen serán automáticamente eliminados del grupo.
    
    @param sprite: Sprite con el que se quiere determinar la colisión.
    @type sprite: pygame.sprite.Sprite
    @param group: Grupo de sprites que posiblemente chocan con sprite.
    @type group: pygame.sprite.Group
    @return: Lista de los sprites que chocan con sprite.
    @rtype: list
    """
    crashed = []
    spritecollide = sprite.rect.colliderect
    ppcollide = _pixelPerfectCollisionDetection
    for s in group.sprites():
        if spritecollide(s.rect):
            if ppcollide(sprite, s):
                crashed.append(s)
    return crashed