import os, sys; sys.path.append(os.path.dirname(__file__))
import unittest
from grid_bfs import shortest_path_len

class TestGridBFS(unittest.TestCase):
    def test_basic(self):
        grid = [
            [0,0,0],
            [1,1,0],
            [0,0,0],
        ]
        self.assertEqual(shortest_path_len(grid), 4)

    def test_blocked(self):
        self.assertEqual(shortest_path_len([[1]]), -1)
        self.assertEqual(shortest_path_len([[0,1],[1,0]]), -1)

if __name__ == '__main__':
    unittest.main()
