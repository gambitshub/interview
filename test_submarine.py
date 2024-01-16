import unittest

from submarine import Submarine, Pilot


class TestSubmarine(unittest.TestCase):

    def setUp(self):
        """set up the test"""
        self.my_sub = Submarine()

    def test_update_forward_position(self):
        """testing forward position updates correctly"""
        self.my_sub.update_position("forward", 5)
        self.assertEqual(self.my_sub.horizontal_pos, 5)

class TestPilot(unittest.TestCase):
    def setUp(self):
        self.submarine = Submarine()
        self.pilot = Pilot(self.submarine)

    def test_navigate(self):
        instructions = ['forward 5', 'down 3', 'up 2']
        self.pilot.navigate(instructions)
        self.assertEqual(self.submarine.horizontal_pos, 5)
        self.assertEqual(self.submarine.aim, 1)
        self.assertEqual(self.submarine.depth, 0)

class TestInput(unittest.TestCase):
    def setUp(self):
        self.instruction = "message 0"

    def test_input_format(self):
        command, value = self.instruction.split(" ")
        
if __name__ == "__main__":
    unittest.main()