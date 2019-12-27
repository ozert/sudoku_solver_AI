#Code is written by ÖZER TANRISEVER
#Credit : https://www.linkedin.com/in/ozer-tanrisever/
# The boards taken from https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html

#For GUI representation import sudoku_solver_gui and make adjustments accordingly.

import color_lib as cl
import time
#import sudoku_solver_gui as gui


#Easy
board = [[0,0,0,2,6,0,7,0,1],
[6,8,0,0,7,0,0,9,0],
[1,9,0,0,0,4,5,0,0],
[8,2,0,1,0,0,0,4,0],
[0,0,4,6,0,2,9,0,0],
[0,5,0,0,0,3,0,2,8],
[0,0,9,3,0,0,0,7,4],
[0,4,0,0,5,0,0,3,6],
[7,0,3,0,1,8,0,0,0]]

#Darn hard! Very very hard!
board2 = [[0,2,0,0,0,0,0,0,0],
[0,0,0,6,0,0,0,0,3],
[0,7,4,0,8,0,0,0,0],
[0,0,0,0,0,3,0,0,2],
[0,8,0,0,4,0,0,1,0],
[6,0,0,5,0,0,0,0,0],
[0,0,0,0,1,0,7,8,0],
[5,0,0,0,0,9,0,0,0],
[0,0,0,0,0,0,0,4,0]]




steps_taken = [] # This holds the taken steps in the game!


def print_board():

    global board
    print()

    for i in range(len(board)):
        
        if (i % 3 == 0):
            print('-------------------------')
        
        for j in range(len(board[0])):
            if(j % 3 == 0):
                print('| ' , end = '') 
            
            print(str(board[i][j]) + ' ' , end = '')
            
            if(j == len(board)-1):
                print('|')

        if(i == len(board)-1):
            print('-------------------------')
        
    print()       

def find_empty_square_index():

    '''This returns an empty item index on board (If it exists).'''

    global board
    for i in range(len(board)):
        for j in range (len(board[0])):
            if(board[i][j] == 0):
                return i,j #row,column
    return None

def find_threeXthreeSquareElements(row,column):
    
    ''''This returns a list of appropriate 3x3 square elements relative to it's row and columns (except itself)'''
    
    global board
    
    tts =[]
    
    if( (0 <= row <=2 ) and (0 <= column <= 2) ):
        low_border_row, high_border_row, low_border_column, high_border_column = 0,2,0,2  
    elif( (0 <= row <=2 ) and (3 <= column <= 5) ):
        low_border_row, high_border_row, low_border_column, high_border_column = 0,2,3,5  
    elif( (0 <= row <=2 ) and (6 <= column <= 8) ):
        low_border_row, high_border_row, low_border_column, high_border_column = 0,2,6,8      
    elif( (3 <= row <=5 ) and (0 <= column <= 2) ):
        low_border_row, high_border_row, low_border_column, high_border_column = 3,5,0,2  
    elif( (3 <= row <=5 ) and (3 <= column <= 5) ):
        low_border_row, high_border_row, low_border_column, high_border_column = 3,5,3,5      
    elif( (3 <= row <=5 ) and (6 <= column <= 8) ):
        low_border_row, high_border_row, low_border_column, high_border_column = 3,5,6,8      
    elif( (6 <= row <=8 ) and (0 <= column <= 2) ):
        low_border_row, high_border_row, low_border_column, high_border_column = 6,8,0,2      
    elif( (6 <= row <=8 ) and (3 <= column <= 5) ):
        low_border_row, high_border_row, low_border_column, high_border_column = 6,8,3,5  
    elif( (6 <= row <=8 ) and (6 <= column <= 8) ):
        low_border_row, high_border_row, low_border_column, high_border_column = 6,8,6,8  


    for i in range(low_border_row,high_border_row+1):
        for j in range(low_border_column,high_border_column+1):
            tts.append(board[i][j])
    
    return tts

def validation_check(test_num, row_vec, column_vec, square_vec):
    '''This method checks whether or not the number is suitable.'''

    if(test_num in row_vec or test_num in column_vec or test_num in square_vec or test_num >=10):
        return False
    else:
        return True

def find_column_vector(column):
    global board
    cv = []
    for i in range(len(board)):
        cv.append(board[i][column])
    return cv
    
def assign_a_number(row,column):

    global board, steps_taken
    
    test_number = board[row][column] # Current number in that position
    
    #This three lists will be used in validation!
    column_vec = find_column_vector(column)
    row_vec = board[row]
    square_vec = find_threeXthreeSquareElements(row, column)

    #cl.print_warning('Row vector   : ' + str(board[row]) + '\n' + 'Column vector: ' + str(column_vec) + '\n3x3 vector   : ' + str(square_vec) ) #For debugging
    

    while True:

        test_number +=1 # The new number may be the one (Algorithm can be slightly improved.)

        #cl.print_warning('The candidate number for this position is : ' + str(test_number)) # For debugging


        if (validation_check(test_number,row_vec, column_vec, square_vec)):
            #İf this happens, picked number is valid!
            board[row][column] = test_number
            
            if(len(steps_taken) >= 2 and [row,column] == steps_taken[-1]):
                return    

            else:
                steps_taken.append([row,column])
                return

        elif(test_number >=10):

            test_number = 0
            board[row][column] = 0
            back_track()

            return #For test purposes

    
def back_track():

    global steps_taken, board
    #print_board() #For debugging
    
    prev_step = []
    prev_step.append(steps_taken[-1])
    
    
    #cl.print_error('The given indexes are  : = > ' + str(prev_step[-1][0]) +'  '+ str(prev_step[-1][1])) # For debugging
    
    if(len(steps_taken) > 1 ):
        del steps_taken[-1]

    assign_a_number(prev_step[-1][0],prev_step[-1][1])
    
    return
    




#This part of the code is for backup.

start_solving = time.time()

while(find_empty_square_index() != None):

    r,c = find_empty_square_index()
    #cl.print_success('The found index of 0 is : (rov X column) ' + str(r) +' X '+ str(c)) #For debugging
    assign_a_number(r,c)
    #print_board() #For debugging # This line can be used for Graphical Representation!
    

end_solving = time.time()

cl.print_success('The time spent for solving is : ' + str(end_solving - start_solving))
print_board()


