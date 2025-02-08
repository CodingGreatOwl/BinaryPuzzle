import numpy as np
from board import Board

def solv_recursive(b: Board):
    skip_recursive = False

    if b.is_correct() and b.is_complete():
        print("Found a solution : ")
        b.pretty_print()
        return True
    else:
        # Find an empty cell (in the most filled line that is not complete -> %10)
        count_incomplete = (b.count_o_row+b.count_x_row)%10
        idx_row_empty = np.argmax(count_incomplete)
        if count_incomplete[idx_row_empty] == 0:
            print("Wow it's a rare case not handled now")
            raise("Not implemented")
        
        for i in range(10):
            if(b.board[idx_row_empty, i]==' '):
                break

        b.board[idx_row_empty, i] = 'O'
        b.start_solving()
        if not b.is_correct():
            skip_recursive = True    
        if not skip_recursive and solv_recursive(b):
            return True
        
        skip_recursive = False

        b.board[idx_row_empty, i] = 'X'
        b.start_solving()
        if not b.is_correct():
            skip_recursive = True    
        if not skip_recursive and solv_recursive(b):
            return True

        # Reinitialize and admit wrong solution
        b.board[idx_row_empty, i] = ' '
        return False


def input():
    #List_o = [(0,1), (0,6), (1,6), (2,0), (4,0), (4,3), (5,3), (5,9), (9,0), (9,6), (9,7)]
    #List_x = [(1,1), (2,7), (3,5), (4,8), (5,5), (6,0), (7,0), (7,4), (7,5), (8,1), (8,3), (8,8)]

    List_o = [(0,7), (1,9), (2,9), (2,2), (3,6), (7,2), (7,5), (8,2), (8,8), (9,4)]
    List_x = [(0,1), (1,3), (3,3), (4,8), (4,5), (6,0), (6,4), (6,6), (6,8), (7,0), (9,1)]

    b = Board(List_x, List_o)
        
    b.pretty_print()
    b.start_solving()
    if solv_recursive(b):
        print("Thanks for playing")
