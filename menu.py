import pygame, sys


v_width = 600
v_height = 600
pygame.init()
window = pygame.display.set_mode((v_width, v_height))
dificultades = ["Facil", "Intermedio", "Dificil"]


class Menu :
    def __init__(self,window) :
        self.window = window
        self.fond = pygame.font.Font(None, 30)

    def mostrar(self,texto, x, y):
       texto_ = self.fond.render(texto, True, (0, 0, 0))
       self.window.blit(texto_, (x, y))

    def draw(self):
        pygame.draw.rect(self.window,(255,255,255),(v_height//4,v_width//2.5,300,100))
    
    def flip(self):
        pygame.display.flip()
    



def main() : 
    menu = Menu(window)
    while True:

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        window.fill((45,0,0))
        menu.draw()
        menu.mostrar("Dificultad ",v_height//4,v_width//2.5)
        for i ,dificultad in enumerate(dificultades):
           menu.mostrar(f"{dificultad}",v_height//4,v_width//(2.5))
        
        menu.flip()
        

main()
    
