#Code is written by ÖZER TANRISEVER
#Credit : https://www.linkedin.com/in/ozer-tanrisever/

import pygame
import time
import sudoku_solver as ss

def show_board():    
    '''This method draws the board layout.'''
    for i in range(0,10):
        
        if(i%3 ==0):
            punto = 4
        else:
            punto = 1

        pygame.draw.line(gameDisplay,(0,0,0),(0,i*((width)/9)),(height,i*((width)/9)),punto)
        pygame.draw.line(gameDisplay,(0,0,0),(i*((width)/9),0),(i*((width)/9),height),punto)
            
 
def print_original_board():
    '''This method prints the non played (original) board.'''
    board_numbers = []

    for i in ss.board:
        for j in i[:]:
            board_numbers.append(j)
    
    board_numbers.reverse()
    num_loc = []
    x=0
    for i in range(0,9):
        for i in range(0,9):
            num_loc.append([int(i*((width)/9)),x])
        x += 100



    for i in range(1,82):
        if(board_numbers[i-1] != 0 ):
            font = pygame.font.SysFont(None, 100)
            text = font.render(str(board_numbers[i-1]), True, (45,8,140,250))
            gameDisplay.blit(text,(num_loc[-i][0]+33,num_loc[-i][1]+20))
        
    
    pygame.display.update()
    clock.tick(12)

def sudoku_gui_number_update(squareX,squareY,new_number):
    '''This method puts a number to spesific location on the board and makes its background green.'''
    
    square_size = 100
    pygame.draw.rect(gameDisplay,(0,255,0),(squareX,squareY,square_size,square_size))
    
    font = pygame.font.SysFont(None, 100)
    text = font.render(str(new_number), False, (45,8,140,250))
    gameDisplay.blit(text,(squareX+33,squareY+20))
    show_board()
    
    pygame.display.update()
    clock.tick(12)


def sudoku_gui_number_delete(squareX,squareY):
    '''This method clears a square and makes red bordered! '''
    square_size = 100
    
    pygame.draw.rect(gameDisplay,(255,0,0),(squareX+1,squareY+1,square_size-1,square_size-1))
    pygame.draw.rect(gameDisplay,(255,255,255),(squareX+5,squareY+5,square_size-9,square_size-9))
    
    pygame.display.update()
    clock.tick(12)



pygame.init()

clock = pygame.time.Clock()
height = width = 900
gameDisplay = pygame.display.set_mode((height,width))
pygame.display.set_caption('Sudoku_Solver_made_by_Özer_TANRISEVER')

pygame.draw.rect(gameDisplay,(255,255,255),(0,0,height,width))


show_board()
print_original_board()


while(ss.find_empty_square_index() != None):

    r,c = ss.find_empty_square_index()   
    ss.assign_a_number(r,c)

    clock.tick(12)

time.sleep(3)
pygame.quit()





