import unittest
from unittest.mock import Mock, patch
from maze import Maze

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.num_rows = 5
        self.num_cols = 5
        self.cell_size_x = 20
        self.cell_size_y = 20
        self.x1 = 0
        self.y1 = 0
        
        # Mock the window object
        self.win = Mock()
        
        # Create a Maze instance
        self.maze = Maze(self.x1, self.y1, self.num_rows, self.num_cols, self.cell_size_x, self.cell_size_y, self.win)

    @patch.object(Maze, '_draw_cell')
    def test_break_entrance_and_exit(self, mock_draw_cell):
        # Call the method to break entrance and exit
        self.maze._break_entrance_and_exit()

        # Check the top-left cell's top wall is removed
        top_left_cell = self.maze._cells[0][0]
        self.assertFalse(top_left_cell.has_wall('top'), msg="Top wall of the top-left cell should be removed")
        
        # Check the bottom-right cell's bottom wall is removed
        bottom_right_cell = self.maze._cells[self.num_rows - 1][self.num_cols - 1]
        self.assertFalse(bottom_right_cell.has_wall('bottom'), msg="Bottom wall of the bottom-right cell should be removed")

        # Verify that _draw_cell was called exactly twice (once for entrance, once for exit)
        self.assertEqual(mock_draw_cell.call_count, 2, msg="_draw_cell should have been called twice for entrance and exit walls")

        # Ensure calls to _draw_cell were made for the correct cell coordinates
        mock_draw_cell.assert_any_call(0, 0, wall_color="white")
        mock_draw_cell.assert_any_call(self.num_rows - 1, self.num_cols - 1, wall_color="white")

if __name__ == '__main__':
    unittest.main()