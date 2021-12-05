#!/usr/bin/env python

import pygame
from .texto import texto
from .textoci import texto2
from .imgfondo import fondo
TEXT_COLOR2 = (0,0,0)
COLOR_RED = (213, 0, 0)
BAR_COLOR = (151, 0, 172)
TEXT_COLOR = (255, 255, 255)

class Button(pygame.sprite.Sprite):
    def __init__(self, identificador, parent, text, fondo = 0, ancho = 500):
        """
        Método inicializador de la clase. 
        
        @param identificador: Variable usada para identificar al botón.
        @type identificador: str
        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        @param text: Variable que indica el texto que tendrá el botón.
        @type text: str
        @param fondo: Indica si el fondo del botón sera con imagen o sin imagen (en desarrollo).
        @type fondo: bool
        @param ancho: Indica el ancho del botón. Es usado para cuadrar el texto centrado.
        @type ancho: int
        """
        pygame.sprite.Sprite.__init__(self)
        self.ancho = ancho
        self.parent =parent 
        tipografia = pygame.font.match_font("FreeSans", False, False)        
        font = pygame.font.Font(tipografia, parent.config.t_fuente)
        self.identificador = identificador
        varios = "../imagenes/png/varios/"
        
        if fondo == 0:
            texto1 = font.render(text, 1, TEXT_COLOR)
            textorect = texto1.get_rect()
            texto2 = font.render(text, 1, COLOR_RED)
            self.img_fondo = pygame.image.load(varios + "img-boton.png")
            self.img_fondo2 = pygame.image.load(varios + "img-boton.png")
            imgrect = self.img_fondo.get_rect()
            textorect.center = imgrect.center[0],imgrect.center[1]+imgrect.center[1]/3
            self.img_fondo.blit (texto1, textorect)                            
            self.img_fondo2.blit (texto2,textorect)
            self.rect = self.img_fondo.get_rect()            
            self.image= self.img_fondo 
            
        if fondo == 1:                            
            txt = texto(0,0,text,parent.config.t_fuente,"texto_act",self.ancho)                                    
            self.rect = pygame.Rect(0,0,self.ancho,txt.ancho_final)
            image_texto = pygame.Surface((self.ancho,txt.ancho_final))
            image_texto.fill((255,255,255))
            image_texto.set_colorkey((255,255,255))
            for i in txt.img_palabras:
                image_texto.blit(i.image, i.rect)                
            self.image = image_texto
            self.img_fondo = image_texto
            self.img_fondo2 = image_texto 
        
    def cambiar_status(self, status):
        """
        Dibuja un efecto en los botones cambiando la imagen de fondo (descontinuado)
        """
        if status:
            self.image = self.img_fondo2
        else: 
            self.image = self.img_fondo    
            
    def mover_boton(self,x,y):
        """
        Cambia la posición del botón.
        """
        self.rect.center = (x,y)
                
class PopUp(pygame.sprite.Sprite):
    def __init__(self, parent , texto1, palabra_boton , imagenes , grupo, tipo = 0 ,px=512,py=281,tam =0):
        """
        Método inicializador de la clase. 
                
        @param parent: Instancia del gestor de pantallas.
        @type parent: Manejador
        @param texto1: Indica el texto que será mostrado en la ventana emergente.
        @type texto1: str 
        @param palabra_boton: Indica la palabra que tendrá el botón. Solo es usado en caso de ser tipo = 0,
        de ser distinto de 0 toma el valor de una cadena y no será asignado.
        @type palabra_boton: str
        @param imagenes: Indica la(s) imagen(es) que mostrará la ventana emergente. En caso de tipo = 2
        no es un campo necesario, en caso de tipo = 1 debe ser una superficie y en caso de tipo = 0
        el parámetro debe ser una tupla con dos imágenes, la  posición 0 sera la imagen
        que estará al lado del texto, mientras que la posición 1 sera la imagen que estará debajo del texto.
        @type imagenes: pygame.Surface, tuple
        @param grupo: Representa un grupo de Sprites donde será agregado el sprite con la imagen y su rectángulo.
        @type grupo: pygame.sprite.Group
        @param tipo: Determina el tipo de ventana emergente, si toma el valor de 2 la ventana emergente solo
        tomara el parámetro texto1 (los demás parámetros deben ser introducidos), en caso de tomar el valor 1
        la ventana emergente tomara los parámetros texto1, imagenes y palabra_boton, mostrando una ventana
        ordenada con texto justificado, un espacio a derecha donde sera ubicada la imagen (dicha imagen debe 
        tener máximo 1/3 del tamaño de la ventana emergente) y un botón centrado debajo del texto. En caso de
        tomar valor 0 la ventana emergente sera similar a la anterior, con la diferencia que tendrá una imagen
        más ubicada en la parte izquierda del botón y debajo del texto.
        @type tipo: int
        """
        pygame.sprite.Sprite.__init__(self)
        self.parent = parent
        self.sprite = pygame.sprite.Sprite()
        varios = "../imagenes/png/varios/"
        self.texto = pygame.Surface
        self.tipo = tipo
        self.arreglo_botones=[]
        self.grupo = grupo
        self.click = -1
        self.activo = 0
        self.tam = 0
        
        if tipo == 0: 
            self.img_fondo = pygame.image.load(varios + "cuadropop-up.png").convert_alpha()        
            self.sprite.image = pygame.image.load(varios + "cuadropop-up.png").convert_alpha()
            self.sprite.rect = self.sprite.image.get_rect()                   
            x=30
            y=30
            self.texto = texto(x, y,texto1[0], parent.config.t_fuente , "texto_act" ,(self.sprite.rect.width*2/3 ))                           
            self.area_texto = pygame.Rect(x,y,self.sprite.rect.w*2/3,self.texto.ancho_final)   
            self.area_imagenes = pygame.Rect((self.sprite.rect.w*2/3)+80, y, self.sprite.rect.w/3, self.texto.ancho_final)           
            self.parent = parent
            self.boton = Button(0,self.parent,palabra_boton)            
            self.boton.mover_boton( self.sprite.rect.width/2, self.area_texto.h + x*2 + self.boton.rect.h / 2 )            
            self.boton_rect = pygame.Rect(self.boton.rect.x  ,  self.boton.rect.y  , self.boton.rect.width  ,  self.boton.rect.height) 
            self.sprite.image = fondo(self.sprite.rect.w, self.boton.rect.y+self.boton.rect.h+x,5 ).return_imagen()  
            self.imagen = pygame.sprite.Sprite()  
            
            if type (imagenes)!= pygame.Surface :
                self.imagen2 = pygame.sprite.Sprite()  
                self.imagen.image = imagenes[0]
                self.imagen.rect =self.imagen.image.get_rect()                                
                self.imagen.rect.center =(self.sprite.rect.w*2/3 +(self.sprite.rect.w/3)/2 , self.area_imagenes.h/2 + self.boton_rect.h/2 )                
                self.imagen2.image = imagenes[1]
                self.imagen2.rect = self.imagen.image.get_rect() 
                self.imagen2.rect.left = x
                self.imagen2.rect.y = self.area_texto.h+40
                self.sprite.image.blit(self.imagen2.image , self.imagen2.rect)
                
            else:
                self.imagen.image = imagenes
                self.imagen.rect =self.imagen.image.get_rect()                                
                self.imagen.rect.center =(self.sprite.rect.w*2/3 +(self.sprite.rect.w/3)/2 , self.area_imagenes.h/2 + self.boton_rect.h/2 )
            if self.imagen.rect.y < 5:
                self.imagen.rect.y = 6
            for i in self.texto.img_palabras:
                self.sprite.image.blit(i.image, i.rect)
            self.sprite.image.blit(self.boton.image , self.boton.rect)
            self.sprite.image.blit(self.imagen.image , self.imagen.rect)
            self.sprite.rect.center = (px, py)
            self.boton_rect.center = (self.sprite.rect.x + self.sprite.rect.width/2, self.sprite.rect.y + self.area_texto.h + x*2 + self.boton.rect.h / 2)            

        if tipo == 1:
            self.img_fondo = pygame.image.load(varios + "cuadropop-up.png").convert_alpha()        
            self.sprite.image = pygame.image.load(varios + "cuadropop-up.png").convert_alpha()
            self.sprite.rect = self.sprite.image.get_rect()                  
            x = 15
            y = 15
            o = 0
            separacion = 30
            tabulacion = 30
            self.sprite.rect.w += tam
            for i in texto1:
                if o ==0:
                    self.texto = texto(x, y,i, parent.config.t_fuente , "texto_act" ,(self.sprite.rect.width )-x)
                if o>0:
                    self.arreglo_botones.append(Button(o-1,self.parent,i,1,self.sprite.rect.w - x*2 -tabulacion))
                o+=1        
            self.texto.rect = pygame.Rect(x,y,self.sprite.rect.w - 80, self.texto.ancho_final)                                
            y+=  self.texto.ancho_final + separacion
            for i in self.arreglo_botones:
                i.rect.x = x+tabulacion/2
                i.rect.y = y
                y+=i.rect.h + separacion/2        
            self.img_fondo = fondo(self.sprite.rect.w, y).return_imagen()           
            self.sprite.image = fondo(self.sprite.rect.w, y).return_imagen()
            
            
            for i in self.texto.img_palabras:
                self.sprite.image.blit(i.image,i.rect)
                self.img_fondo.blit(i.image,i.rect)                
            self.sprite.rect.center = (px, py)    
                          
            for i in self.arreglo_botones:
                self.sprite.image.blit(i.image,i.rect)
                self.img_fondo.blit(i.image,i.rect)                
                i.rect.x = self.sprite.rect.x + i.rect.x
                i.rect.y = self.sprite.rect.y + i.rect.y                   
        
        if tipo == 2:            
            
            self.sprite.image = pygame.image.load(varios + "cuadropop-up.png").convert_alpha()
            self.sprite.rect = self.sprite.image.get_rect()
            self.sprite.rect.w += tam
            self.texto = texto2(15,15, texto1,parent.config.t_fuente, "intercalado", self.sprite.rect.w -15, imagenes)
            self.sprite.image = fondo(self.sprite.rect.w, self.texto.ancho_final+30).return_imagen()
            self.sprite.rect.h = self.texto.ancho_final+30
            self.tam = self.texto.ancho_final+60
            for i in self.texto.img_palabras:
                self.sprite.image.blit(i.image, i.rect)                                             
            self.sprite.rect.center=(px,py)
                
    def popup_estatus(self):
        """
        Define cuando esta activa la ventana emergente.
    
        @return: En caso de ser True la ventana esta activa, en caso contrario no estará activa.
        @rtype: bool
        """
        if self.activo:
            return True
        else:
            return False
        
    def redibujar_boton(self):
        """
        Define el efecto de los botones en las ventanas emergentes (descontinuado)
        """
        if self.tipo ==0:
            self.sprite.image.blit(self.img_fondo,(self.boton.rect.x,self.boton.rect.y), self.boton.rect)
            self.sprite.image.blit(self.boton.img , self.boton.rect)
        if self.tipo == 1:
            self.sprite.image.blit(self.img_fondo,(0,0))            
        
    def agregar_grupo (self):
        """
        Agrega el sprite de la ventana emergente al grupo de sprite pasado por parámetros al crear el objeto.
        """
        self.activo=1
        self.grupo.add(self.sprite)
        
    def eliminar_grupo(self):
        """
        Elimina el sprite de la ventana emergente del grupo de sprite pasado por parámetros al crear el objeto.
        """
        self.activo = 0
        self.grupo.remove(self.sprite)
    
    def evaluar_click(self): 
        """
        Retorna el resultado del método manejador_eventos().
    
        @return: True si se hizo click, de lo contrario False.
        @rtype: bool
        """      
        return self.click
        
    def manejador_eventos(self, eventos):
        """
        Determina cuando se hace click al botón
        (solo en caso de ser una ventana emergente de tipo 0 o 1)
    
        @param eventos: Ultimo evento recibido.
        @rtype: pygame.event.Event
        """      
        teclasPulsadas = pygame.key.get_pressed()    
        if self.tipo == 0:  
            if self.boton_rect.collidepoint(pygame.mouse.get_pos()):
                if (eventos.type == pygame.MOUSEBUTTONDOWN and eventos.button == 1):                 
                    self.eliminar_grupo()                    
                    self.click = 0
                    return True
                else:
                    self.click= -1
                    
            if teclasPulsadas[pygame.K_RETURN]:
                self.eliminar_grupo()
                self.click = 0
            else:
                self.click= -1                   
                
        if self.tipo == 1:
            for i in self.arreglo_botones:
                if i.rect.collidepoint(pygame.mouse.get_pos()):  
                    if eventos.type == pygame.MOUSEBUTTONDOWN and eventos.button == 1:
                        self.click = i.identificador
                    else:
                        self.click = -1
