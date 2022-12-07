import pygame


class contador:
    inicio = False
    final = False
    tiempo = 0

    def __init__(self, tiempo_inicial, tiempo_final, fps):
        self.ti = tiempo_inicial
        self.tf = tiempo_final
        self.fps = fps

    def iniciar(self):
        self.inicio = True
        self.contador = pygame.time.Clock()
        self.contador.tick(self.fps)
        self.tiempo = self.ti

    def contar(self):
        if self.inicio and not self.final:
            if self.tiempo > self.tf:
                self.tiempo = 0
                self.final = True
            else:
                self.tiempo += self.contador.get_time()
            print(self.tiempo)


# def main():
#    salir = False
#    p = pygame.display.set_mode((400, 400))
#    cron = contador(5000, 10000, 1)
#
#    while salir != True:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                salir = True
#
#            if event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_F1:
#                    cron.iniciar()
#
#        cron.contar()
#        pygame.display.update()
#        pygame.time.Clock().tick(1)
# main()
