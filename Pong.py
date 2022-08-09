import pygame
import os
import random
import sys
from pygame import color

#Inicializar modulo pygame y establecer variables
pygame.init()
pygame.font.init()
pygame.mixer.init()
reloj = pygame.time.Clock()
ANCHO, ALTO = 900, 500
VEN = pygame.display.set_mode((ANCHO, ALTO),0,32)
FPS = 60 
VEL = 6
Ai_velocidad = 7
ColisionCount = 0

#Sonidos
SONIDO_PALETA = pygame.mixer.Sound(os.path.join('Sonidos', 'Paleta.mp3'))
SONIDO_PARED = pygame.mixer.Sound(os.path.join('Sonidos', 'Pared.mp3'))
SONIDO_PUNTUACION = pygame.mixer.Sound(os.path.join('Sonidos', 'Puntuacion.mp3'))  

#Velocidad de la pelota en ambos ejes
VEL_PELOTA_X = 5
VEL_PELOTA_Y = 5

#Puntuacion
puntos_jugador1 = 0
puntos_jugador2 = 0
Fuente = pygame.font.Font('freesansbold.ttf', 24)
Fuente_ganador = pygame.font.SysFont('comicsans', 60)

#nombre de la ventana
pygame.display.set_caption("Pong")

#Colores
PREDETERMINADO = (64, 64, 64)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 176, 0)
AMARILLO = (255,192,0)
AQUA = (112,197,177)
MARRON = (132,60,12)
VERDE_LIMA = (0,176,80)
AZUL_CLARO = (112,213,208)
GRIS_OSCURO = (49,49,49)
AZUL_CIELO = (0,176,240)
ROSA = (255,121,156)
LAVANDA = (108,106,205)
MORADO = (112,48,160)
AZUL_LAVANDA = (121,147,196)
ROSA_CLARO = (250,199,195)

#Color de fondo
colordefondo = PREDETERMINADO

#Figuras del juego
pelota = pygame.Rect(ANCHO/2 - 7.5, ALTO/2 + 7.5, 15, 15)
jugador2 = pygame.Rect(ANCHO - 20, ALTO/2 - 20, 10, 80) 
jugador1 = pygame.Rect(10, ALTO/2 - 20 , 10, 80)
YBall = pelota.y

#Menu

font = pygame.font.SysFont(None, 45)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
from pygame.locals import *
def main_menu():
    while True:
        bg = pygame.image.load("Fondo_Menu.png")
        VEN.blit(bg, (0, 0))
        draw_text('Pong',  pygame.font.SysFont(None, 100) , (NEGRO), VEN, 365, 100)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(150, 250, 200, 50)
        button_2 = pygame.Rect(550, 250, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                controls()
                fondos()
                singleplayer()
                
        if button_2.collidepoint((mx, my)):
            if click:
                controls()
                fondos()
                principal()
        pygame.draw.rect(VEN, (NEGRO), button_1,1)
        pygame.draw.rect(VEN, (NEGRO), button_2,1)
        draw_text('Singleplayer', font, (NEGRO), VEN, 155, 260)
        draw_text('Multiplayer', font, (NEGRO), VEN, 565, 260)

 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        reloj.tick(60)
def controls():
    AceptandoControles = True
    while AceptandoControles:
        mx, my = pygame.mouse.get_pos()
        bg = pygame.image.load("Fondo_Menu.png")
        VEN.blit(bg, (0, 0))
        draw_text('Player 2', font, (NEGRO), VEN, 600, 100)
        draw_text('Player 1', font, (NEGRO), VEN, 200, 100)
        draw_text('Mover Arriba = W', font, (NEGRO), VEN, 100, 200)
        draw_text('Mover Abajo = S', font, (NEGRO), VEN, 100, 250)
        draw_text('Boost = Spacebar', font, (NEGRO), VEN, 100, 300)
        draw_text('Mover Arriba = Flecha Arriba', font, (NEGRO), VEN, 450, 200)
        draw_text('Mover Abajo = Flecha Abajo', font, (NEGRO), VEN, 450, 250)
        draw_text('Boost = CTRL', font, (NEGRO), VEN, 450, 300)
        botonPlay = pygame.Rect(350, 400, 200, 50)
        if botonPlay.collidepoint((mx, my)):
            if click:
                break
        pygame.draw.rect(VEN, (NEGRO), botonPlay,1)
        draw_text('Play', font, (NEGRO), VEN, 425, 410)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        reloj.tick(60)
def fondos():
    click = False
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        bg = pygame.image.load("Fondo_Menu.png")
        VEN.blit(bg, (0, 0))

        Amarillo = pygame.Rect(600, 120, 200, 50)
        Aqua = pygame.Rect(100, 120, 200, 50)
        Marron = pygame.Rect(100, 180, 200, 50)
        VerdeLima = pygame.Rect(600, 180, 200, 50)
        AzulCLaro = pygame.Rect(100, 240, 200, 50)
        GrisOscuro = pygame.Rect(600, 240, 200, 50)
        AzulCielo = pygame.Rect(100, 300, 200, 50)
        Rosa = pygame.Rect(600, 300, 200, 50)
        Lavanda = pygame.Rect(100, 360, 200, 50)
        Morado = pygame.Rect(600, 360, 200, 50)
        AzulLavanda = pygame.Rect(100, 420, 200, 50)
        RosaClaro = pygame.Rect(600, 420, 200, 50)
        draw_text('Selecciona un fondo',  pygame.font.SysFont(None, 100) , (NEGRO), VEN, 100, 50)
        pygame.draw.rect(VEN, (AMARILLO), Amarillo)
        pygame.draw.rect(VEN, (AQUA), Aqua)
        pygame.draw.rect(VEN, (MARRON), Marron)
        pygame.draw.rect(VEN, (VERDE_LIMA), VerdeLima)
        pygame.draw.rect(VEN, (AZUL_CLARO), AzulCLaro)
        pygame.draw.rect(VEN, (GRIS_OSCURO), GrisOscuro)
        pygame.draw.rect(VEN, (AZUL_CIELO), AzulCielo)
        pygame.draw.rect(VEN, (ROSA), Rosa)
        pygame.draw.rect(VEN, (LAVANDA), Lavanda)
        pygame.draw.rect(VEN, (MORADO), Morado)
        pygame.draw.rect(VEN, (AZUL_LAVANDA), AzulLavanda)
        pygame.draw.rect(VEN, (ROSA_CLARO), RosaClaro)
        PlayingButton = pygame.Rect(350, 400, 200, 50)
        global colordefondo
        if Amarillo.collidepoint((mx, my)):
            if click:
                colordefondo = AMARILLO
                running = False
        if Aqua.collidepoint((mx, my)):
            if click:
                colordefondo = AQUA
                running = False
        if Marron.collidepoint((mx, my)):
            if click:
                colordefondo = MARRON
                running = False
        if VerdeLima.collidepoint((mx, my)):
            if click:
                colordefondo = VERDE_LIMA
                running = False
        if AzulCLaro.collidepoint((mx, my)):
            if click:
                colordefondo = AZUL_CLARO
                running = False
        if GrisOscuro.collidepoint((mx, my)):
            if click:
                colordefondo = GRIS_OSCURO
                running = False
        if AzulCielo.collidepoint((mx, my)):
            if click:
                colordefondo = AZUL_CIELO
                running = False
        if Rosa.collidepoint((mx, my)):
            if click:
                colordefondo = ROSA
                running = False
        if Lavanda.collidepoint((mx, my)):
            if click:
                colordefondo = LAVANDA
                running = False
        if Morado.collidepoint((mx, my)):
            if click:
                colordefondo = MORADO
                running = False
        if AzulLavanda.collidepoint((mx, my)):
            if click:
                colordefondo = AZUL_LAVANDA
                running = False
        if RosaClaro.collidepoint((mx, my)):
            if click:
                colordefondo = ROSA_CLARO
                running = False
        if PlayingButton.collidepoint((mx, my)):
            if click:
                running = False
        click = False
        pygame.draw.rect(VEN, (NEGRO), PlayingButton,1)
        draw_text('Play', font, (NEGRO), VEN, 425, 410)    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        reloj.tick(60)
#funcion que determina la logica de la pelota y la colision
def fisica():
    global VEL_PELOTA_Y, VEL_PELOTA_X

    #Indica cuanto se tiene que mover la pelo ta en el eje X y Y
    pelota.x += VEL_PELOTA_X
    pelota.y += VEL_PELOTA_Y
    if pelota.colliderect(jugador2) and VEL_PELOTA_X != 15:
        VEL_PELOTA_X = VEL_PELOTA_X + 1
        

    #Establece la colision de la pelota con otras superficies
    if pelota.top <= 50 or pelota.bottom >= ALTO:
        VEL_PELOTA_Y *= -1
        SONIDO_PARED.play()

    if pelota.left <= 0:
        reinicio1()
    if pelota.right >= ANCHO:
        reinicio2()

    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        VEL_PELOTA_X *= -1
        SONIDO_PALETA.play()

#Funcion que determina el movimiento del primer jugador
def Mjugador1(teclas, jugador1):
    if teclas[pygame.K_SPACE]:
        VEL = 12
    else:
        VEL = 6
    
    if teclas[pygame.K_w] and jugador1.y - VEL > 45:
        jugador1.y -= VEL
    if teclas[pygame.K_s] and jugador1.y + VEL + 75 < ALTO:
        jugador1.y += VEL

#Funcion que determina el movimiento del segundo jugador
def Mjugador2(teclas, jugador2):
    if teclas[pygame.K_RCTRL]:
        VEL = 12
    else:
        VEL = 6
    
    if teclas[pygame.K_UP] and jugador2.y - VEL > 45:
        jugador2.y -= VEL
    if teclas[pygame.K_DOWN]and jugador2.y + VEL + 75 < ALTO:
        jugador2.y += VEL

def reinicio1():
    global VEL_PELOTA_Y, VEL_PELOTA_X, puntos_jugador2,ColisionCount
    pelota.center = (ANCHO/2 - 7.5, ALTO/2 + 7.5)
    VEL_PELOTA_Y *= random.choice((1, -1))
    VEL_PELOTA_X = 5
    VEL_PELOTA_X *= -1
    puntos_jugador2 += 1
    SONIDO_PUNTUACION.play()
    ColisionCount = 0
def reinicio2():
    global VEL_PELOTA_Y, VEL_PELOTA_X, puntos_jugador1, ColisionCount
    pelota.center = (ANCHO/2 - 7.5, ALTO/2 + 7.5)
    VEL_PELOTA_Y *= random.choice((1, -1))
    VEL_PELOTA_X = 5
    VEL_PELOTA_X *= 1
    puntos_jugador1 += 1
    SONIDO_PUNTUACION.play()
    ColisionCount = 0
def puntuacion_jugadores():
    Puntuacion = Fuente.render("Jugador 1: " + str(puntos_jugador1), True, BLANCO)
    VEN.blit(Puntuacion, (10,15))
    Puntuacion = Fuente.render("Jugador 2: " + str(puntos_jugador2), True, BLANCO)
    VEN.blit(Puntuacion, (ANCHO - 155 , 15))

def decidir_ganador(ganador):
    texto_ganador = Fuente_ganador.render(ganador, True, VERDE)
    VEN.blit(texto_ganador, (ANCHO/2 - texto_ganador.get_width()/2, ALTO/2 - texto_ganador.get_height()/2))
    pygame.display.update()
    SONIDO_PUNTUACION.play()
    pygame.time.delay(3000)

def Ai():
    global ColisionCount
    if pelota.colliderect(jugador2):
        ColisionCount = ColisionCount + 1 
    if ColisionCount > 10:
        jugador2.top += Ai_velocidad +2
        jugador2.bottom -= Ai_velocidad -2
    if jugador2.top < pelota.y - 7:
        jugador2.top += Ai_velocidad
    if jugador2.bottom > pelota.y + 7: 
        jugador2.bottom -= Ai_velocidad 
    if jugador2.top <= 50:
        jugador2.top = 50
    if jugador2.bottom >= ALTO:
        jugador2.bottom = ALTO
#Funciones principales que seran llamadas
def principal():
    correr = True
    while correr:
        global puntos_jugador1, puntos_jugador2
        reloj.tick(FPS)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                correr = False
                pygame.quit()
        
        teclas = pygame.key.get_pressed()        
        Mjugador1(teclas, jugador1)
        Mjugador2(teclas, jugador2)
        
        fisica()

        VEN.fill(colordefondo)
        pygame.draw.aaline(VEN, BLANCO, (ANCHO/2, 50), (ANCHO/2, ALTO))
        pygame.draw.aaline(VEN, BLANCO, (0, 50), (ANCHO, 50))
        pygame.draw.rect(VEN, BLANCO, jugador1)
        pygame.draw.rect(VEN, BLANCO, jugador2)
        pygame.draw.ellipse(VEN, BLANCO, pelota)
        puntuacion_jugadores()
        pygame.display.update()

        ganador = ""
        if puntos_jugador1 == 7:
            ganador = "¡Jugador 1 ha Ganado!"
        if puntos_jugador2 == 7:
            ganador = "¡Jugador 2 ha Ganado!"
        
        if ganador != "":
            decidir_ganador(ganador)
            break

    puntos_jugador1 = 0
    puntos_jugador2 = 0
    principal()
def singleplayer():
    correr = True
    while correr:
        global puntos_jugador1, puntos_jugador2
        reloj.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                correr = False
                pygame.quit()
        teclas = pygame.key.get_pressed()        
        Mjugador1(teclas, jugador1)
        fisica()
        Ai()
        VEN.fill(colordefondo)
        pygame.draw.aaline(VEN, BLANCO, (ANCHO/2, 50), (ANCHO/2, ALTO))
        pygame.draw.aaline(VEN, BLANCO, (0, 50), (ANCHO, 50))
        pygame.draw.rect(VEN, BLANCO, jugador1)
        pygame.draw.rect(VEN, BLANCO, jugador2)
        pygame.draw.ellipse(VEN, BLANCO, pelota)
        puntuacion_jugadores()
        pygame.display.update()

        ganador = ""
        if puntos_jugador1 == 7:
            ganador = "¡Jugador 1 ha Ganado!"
        if puntos_jugador2 == 7:
            ganador = "¡Jugador 2 ha Ganado!"
        
        if ganador != "":
            decidir_ganador(ganador)
            break

    puntos_jugador1 = 0
    puntos_jugador2 = 0
    singleplayer()

main_menu()