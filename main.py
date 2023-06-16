import pygame
import sys
from juego import Juego
from ia import minimax
grid = []

pygame.init()
v_width = 600
v_height = 600

col = 8
filas = 8

box_width = v_width // col
box_height = v_height// filas
window = pygame.display.set_mode((v_width, v_height))


def main():
    
    juego = Juego(window)
    dificultad = 0
    play = True
    
    while play:

        if juego.turn == 1:
            value, tablero = minimax(juego.getTablero(),dificultad, True, juego)
            juego.ai_move(tablero)



        if juego.ganar()!= None:
            print("Ganador Fichas Color :" + juego.ganar())
            
            
      
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
              
                    
                i = y // box_width
                j = x // box_height

                if dificultad !=0:   
                 juego.select(i,j)
                    
                    
            elif event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                 dificultad =1
                if event.key == pygame.K_2:
                 dificultad =2
                if event.key == pygame.K_3:
                 dificultad =3
                   


        window.fill((0,0,0))
          
        juego.flip()

  
       
main()