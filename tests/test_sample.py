"""
Sample App Tests
"""

from binnoxxo.board import Board
import unittest

class TestBoardMethods_IsComplete(unittest.TestCase):

    def test_is_complete(self):
        """Is indeed complete"""
        List_o = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9),]
        List_x = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)]
        

        b = Board(List_x, List_o)
        b.init_count()
        assert b.is_complete() == True

    def test_is_missing_x(self):
        """Board is missing one x at (6,1)"""
        List_o = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9),]
        List_x = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 0), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)]
        

        b = Board(List_x, List_o)
        b.init_count()
        assert b.is_complete() == False

    def test_is_missing_o(self):
        """Board is missing one O at (1,5)"""
        List_o = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9),]
        List_x = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)]
        

        b = Board(List_x, List_o)
        b.init_count()
        assert b.is_complete() == False

class TestBoardMethods_IsCorrect(unittest.TestCase):
    def test_has_too_many_x_row(self):
        """Board has too many x in a row"""
        List_o = []
        List_x = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
        

        b = Board(List_x, List_o)
        b.init_count()
        assert b.is_correct() == False

    def test_has_too_many_o_row(self):
        """Board has too many o in a row"""
        List_x = []
        List_o = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
        

        b = Board(List_x, List_o)
        b.init_count()
        assert b.is_correct() == False

    def test_has_too_many_x_col(self):
        """Board has too many x in a column"""
        List_o = []
        List_x = [(5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (0, 0)]
        

        b = Board(List_x, List_o)
        b.init_count()
        assert b.is_correct() == False

    def test_has_too_many_o_col(self):
        """Board has too many o in a column"""
        List_x = []
        List_o = [(5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (0, 0)]
        

        b = Board(List_x, List_o)
        b.init_count()
        assert b.is_correct() == False

    def test_has_3_consecutive_o_col(self):
        """Board has too many o in a column"""
        List_x = []
        List_o = [(5, 0), (6, 0), (7, 0)]
        

        b = Board(List_x, List_o)
        b.init_count()
        assert b.is_correct() == False

    def test_has_3_consecutive_x_col(self):
        """Board has too many o in a column"""
        List_o = []
        List_x = [(5, 0), (6, 0), (7, 0)]
        

        b = Board(List_x, List_o)
        b.init_count()
        assert b.is_correct() == False

    def test_has_3_consecutive_x_row(self):
        """Board has too many x in a row"""
        List_o = []
        List_x = [(1, 2), (1, 3), (1, 4)]
        

        b = Board(List_x, List_o)
        b.init_count()
        assert b.is_correct() == False

    def test_has_3_consecutive_o_row(self):
        """Board has too many o in a row"""
        List_x = []
        List_o = [(1, 2), (1, 3), (1, 4)]
        

        b = Board(List_x, List_o)
        b.init_count()
        assert b.is_correct() == False

    def test_has_similar_row(self):
        """Board two identical rows"""

        List_o = [(8, 1), (8, 2), (8, 4), (8, 7), (8, 8), (0, 1), (0, 5), (0, 6), (0, 8), (1, 2), (1, 6), (1, 7), (1, 9), (2, 0), (2, 1), (2, 5), (2, 8), (3, 1), (3, 2), (3, 4), (3, 7), (3, 8), (4, 0), (4, 3), (4, 5), (4, 6), (4, 9), (5, 0), (5, 3), (5, 4), (5, 7), (5, 9), (6, 1), (6, 2), (6, 4), (6, 5), (6, 8)]
        List_x = [(8, 0), (8, 3), (8, 5), (8, 6), (8, 9),(0, 0), (0, 4), (0, 7), (0, 9), (1, 0), (1, 1), (1, 5), (1, 8), (2, 2), (2, 6), (2, 7), (2, 9), (3, 0), (3, 3), (3, 5), (3, 6), (3, 9), (4, 1), (4, 2), (4, 4), (4, 7), (4, 8), (5, 1), (5, 2), (5, 5), (5, 6), (5, 8), (6, 0), (6, 3), (6, 6), (6, 7), (6, 9)]

        b = Board(List_x, List_o)
        b.init_count()
        assert b.is_correct() == False

    def test_has_similar_col(self):
        """Board two identical rows"""

        List_o = [(0, 2), (0, 4), (0, 5), (1, 0), (1, 2), (1, 3), (1, 6), (1, 8), (2, 1), (2, 3), (2, 6), (2, 8), (3, 4), (3, 5), (4, 3), (4, 5), (4, 6), (4, 8), (5, 0), (5, 2), (5, 4), (5, 6), (6, 0), (6, 1), (6, 4), (7, 1), (7, 3), (7, 5), (7, 8), (8, 0), (8, 2), (8, 3), (8, 6), (8, 8), (9, 1), (9, 4), (9, 5)]
        List_x = [(0, 0), (0, 1), (0, 3), (0, 6), (0, 8), (1, 1), (1, 4), (1, 5), (2, 2), (2, 4), (2, 5), (3, 3), (3, 6), (3, 8), (4, 0), (4, 4), (5, 1), (5, 3), (5, 5), (5, 8), (6, 2), (6, 3), (6, 5), (6, 6), (6, 8), (7, 0), (7, 2), (7, 4), (7, 6), (8, 1), (8, 4), (8, 5), (9, 0), (9, 2), (9, 3), (9, 6), (9, 8)]
        b = Board(List_x, List_o)
        b.init_count()
        assert b.is_correct() == False

if __name__ == '__main__':
    unittest.main()