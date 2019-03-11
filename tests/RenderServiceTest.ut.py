import unittest
import time

import sys
sys.path.append('../RankSystem')

from RenderingService import *

class TestRenderImage(unittest.TestCase):
    def test_can_render_image(self):
        rank = Rank("Damnation", "D", 1, "D-d-d-damn!.mp3" , 1000, .1)
        self.assertEqual(rank.name == "Damnation", True)

if __name__ == '__main__':
    unittest.main()