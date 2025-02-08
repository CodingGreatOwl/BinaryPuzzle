import numpy as np

class Board():
        
    def __init__(self, List_x, List_o):
        self.board = np.empty((10, 10), dtype=str)
        self.board[:] = ' '
        self.count_x_row = np.zeros(10)
        self.count_o_row = np.zeros(10)
        self.count_x_col = np.zeros(10)
        self.count_o_col = np.zeros(10)
        self.col_updated = set(range(10))
        self.row_updated = set(range(10))
        
        for i in List_o:
            self.board[i[0], i[1]] = 'O'

        for i in List_x:
            self.board[i[0], i[1]] = 'X'

    def init_count(self):
        """Count the o and x in the current board"""
        
        self.count_x_row = np.zeros(10)
        self.count_o_row = np.zeros(10)
        self.count_x_col = np.zeros(10)
        self.count_o_col = np.zeros(10)
        
        for i in range(10):
            for j in range(10):
                if self.board[i,j] == 'X':
                    self.count_x_row[i] += 1
                    self.count_x_col[j] += 1
                    
                elif self.board[i,j] == 'O':
                    self.count_o_row[i] += 1
                    self.count_o_col[j] += 1
    

    def pretty_print(self):
        """Print the board nicely"""
        interline = "╟─"+"──┼─"*9+"──╢"
        print("\n╔═"+"══╤═"*9+"══╗")
        for i in range(9):
            print("║",end='')
            line_str = ""
            for j in range(10):
                line_str += " "+self.board[i,j]+" │"
            print(line_str[:-1], end = '')
            print("║")
            print(interline)
        print("║",end='')
        line_str = ""
        for j in range(10):
            line_str += " "+self.board[9,j]+" │"
        print(line_str[:-1], end = '')
        print("║")
        print("╚═"+"══╧═"*9+"══╝")
        
    
    def check_double_row(self, x_to_check, y_to_check):
        """Return the character to respect the no more than tow next to each other"""
        
        
        if self.board[x_to_check, y_to_check] != ' ':
            return ' '
        
        if y_to_check >= 2 and self.board[x_to_check, y_to_check-2] == self.board[x_to_check, y_to_check-1] and self.board[x_to_check, y_to_check-1] != ' ':
            if self.board[x_to_check, y_to_check-2] == 'X':
                return 'O'
            else:
                return 'X'
            
        if y_to_check <= 7 and self.board[x_to_check, y_to_check+1] == self.board[x_to_check, y_to_check+2] and self.board[x_to_check, y_to_check+1] != ' ':
            if self.board[x_to_check, y_to_check+2] == 'X':
                return 'O'
            else:
                return 'X'
        
        return ' '
    
    def check_hole_between_similar(self, x_to_check, y_to_check):
        
        if y_to_check < 1 or y_to_check > 8:
            return ' '
        
        
        if self.board[x_to_check, y_to_check] != ' ':
            return ' '
        
        if self.board[x_to_check, y_to_check-1] == self.board[x_to_check, y_to_check+1] and self.board[x_to_check, y_to_check-1] != ' ':
            if self.board[x_to_check, y_to_check-1] == 'X':
                return 'O'
            else:
                return 'X'
        return ' '
    
    def check_hole_between_similar_col(self, x_to_check, y_to_check):
        
        if x_to_check < 1 or x_to_check > 8:
            return ' '
        
        if self.board[x_to_check, y_to_check] != ' ':
            return ' '
        
        if self.board[x_to_check-1, y_to_check] == self.board[x_to_check+1, y_to_check] and self.board[x_to_check-1, y_to_check] != ' ':
            if self.board[x_to_check-1, y_to_check] == 'X':
                return 'O'
            else:
                return 'X'
        return ' '
    
    def check_double_col(self, x_to_check, y_to_check):
        """Return the character to respect the no more than tow next to each other"""
        
        
        if self.board[x_to_check, y_to_check] != ' ':
            return ' '
        
        if x_to_check >= 2 and self.board[x_to_check-2, y_to_check] == self.board[x_to_check-1, y_to_check] and self.board[x_to_check-1, y_to_check] != ' ':
            if self.board[x_to_check-2, y_to_check] == 'X':
                return 'O'
            else:
                return 'X'
            
        if x_to_check <= 7 and self.board[x_to_check+1, y_to_check] == self.board[x_to_check+2, y_to_check] and self.board[x_to_check+1, y_to_check] != ' ':
            if self.board[x_to_check+2, y_to_check] == 'X':
                return 'O'
            else:
                return 'X'
        
        return ' '
    
    def update_count(self, sug, i, j):
        """Refresh the sybol counter"""
        
        if sug == 'X':
            self.count_x_row[i] += 1
            self.count_x_col[j] += 1
                    
        else:
            self.count_o_row[i] += 1
            self.count_o_col[j] += 1
        
    def start_solving(self):
        self.init_count()
        
        row_wise = True
        iter_ = 0
        
        while((self.col_updated != set() or self.row_updated != set()) and iter_ < 1000):
            iter_ += 1
            # Switch solving direction
            if row_wise and self.row_updated == set():
                row_wise = False
            elif not row_wise and self.col_updated == set():
                row_wise = True
            
            # select direction studied
            if row_wise and self.row_updated != set():
                row_ut = self.row_updated.pop()
            elif self.col_updated != set():
                col_ut = self.col_updated.pop()
                
            if row_wise:
                for i in range(10):
                    ## Test
                    if self.board[row_ut, i] != ' ':
                        continue
                        
                    ## Check if already 5 of one type
                    if self.count_o_col[i] == 5 or self.count_o_row[row_ut] == 5:
                        self.row_updated.add(row_ut)
                        self.col_updated.add(i)
                        self.update_count('X', row_ut, i)
                        self.board[row_ut, i] = 'X'
                        
                    elif self.count_x_col[i] == 5 or self.count_x_row[row_ut] == 5:
                        self.row_updated.add(row_ut)
                        self.col_updated.add(i)
                        self.update_count('O', row_ut, i)
                        self.board[row_ut, i] = 'O'
                    
                    elif (sug:= self.check_double_row(row_ut, i)) != ' ':
                        self.row_updated.add(row_ut)
                        self.col_updated.add(i)
                        self.update_count(sug, row_ut, i)
                        self.board[row_ut, i] = sug
                        
                    elif (sug:= self.check_hole_between_similar(row_ut, i)) != ' ':
                        self.row_updated.add(row_ut)
                        self.col_updated.add(i)
                        self.update_count(sug, row_ut, i)
                        self.board[row_ut, i] = sug
                            
            else:
                for i in range(10):
                    ## Test
                    if self.board[i, col_ut] != ' ':
                        continue
                        
                    ## Check if already 5 of one type
                    if self.count_o_col[col_ut] == 5 or self.count_o_row[i] == 5:
                        self.row_updated.add(i)
                        self.col_updated.add(col_ut)
                        self.update_count('X', i, col_ut)
                        self.board[i, col_ut] = 'X'
                        
                    elif self.count_x_col[col_ut] == 5 or self.count_x_row[i] == 5:
                        self.row_updated.add(i)
                        self.col_updated.add(col_ut)
                        self.update_count('O', i, col_ut)
                        self.board[i, col_ut] = 'O'
                        
                    
                    elif (sug:= self.check_double_col(i, col_ut)) != ' ':
                        self.row_updated.add(i)
                        self.col_updated.add(col_ut)
                        self.update_count(sug, i, col_ut)
                        self.board[i, col_ut] = sug
                        
                        
                    elif (sug:= self.check_hole_between_similar_col(i, col_ut)) != ' ':
                        self.row_updated.add(i)
                        self.col_updated.add(col_ut)
                        self.update_count(sug, i, col_ut)
                        self.board[i, col_ut] = sug
     
    def spit_values(self):
        List_o = []
        List_x = []
        for i in range(10):
            for j in range(10):
                if self.board[i,j] == 'X':
                    List_x.append((i,j))
                    
                elif self.board[i,j] == 'O':
                    List_o.append((i,j))
                    
        print("List_o = " + str(List_o))
        print("List_x = " + str(List_x))

    def is_complete(self):
        if any (self.count_o_col < 5):
            return False
        elif any(self.count_x_col < 5):
            return False
        else:
            return True


    def is_correct(self):
        """Check if the current board respects the rules"""

        # No more than 5 entity per row/col
        if any(self.count_o_col > 5) or any(self.count_x_col > 5):
            return False
        elif any(self.count_o_row > 5) or any(self.count_x_row > 5):
            return False

        # No more than 2 consecutive identical symbol
        for i in range(10):
            count_x = 0
            count_o = 0
            for j in range(10):
                if self.board[i,j] == 'X':
                    count_o = 0
                    count_x += 1
                elif self.board[i,j] == 'O':
                    count_x = 0
                    count_o += 1
                else:
                    count_x = 0
                    count_o = 0

                if count_x > 2 or count_o > 2:
                    return False

        for j in range(10):
            count_x = 0
            count_o = 0
            for i in range(10):
                if self.board[i,j] == 'X':
                    count_o = 0
                    count_x += 1
                elif self.board[i,j] == 'O':
                    count_x = 0
                    count_o += 1
                else:
                    count_x = 0
                    count_o = 0

                if count_x > 2 or count_o > 2:
                    return False
        

        # Check for identical row
        row_set = set()
        col_set = set()
        for i in range(10):
            row_string = ''.join(self.board[i,:]).replace(' ', '')
            col_string = ''.join(self.board[:,i]).replace(' ', '')
            if len(row_string) == 10:
                if row_string in row_set:
                    return False
                else:
                    row_set.add(row_string)

            if len(col_string) == 10:
                if col_string in col_set:
                    return False
                else:
                    col_set.add(col_string)

        return True

        