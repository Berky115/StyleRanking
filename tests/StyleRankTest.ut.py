import unittest
import time

import sys
sys.path.append('../RankSystem')

from StyleRank import *
from SoundService import *
from GameLoop import *

class TestRankFunctionality(unittest.TestCase):
    def test_can_make_rank(self):
        rank = Rank("Damnation", "D", 1, "D-d-d-damn!.mp3" , 1000, .1)
        self.assertEqual(rank.name == "Damnation", True)
        self.assertEqual(rank.glyph == "D", True)
        self.assertEqual(rank.priority == 1, True)
        self.assertEqual(rank.activation_sound == "D-d-d-damn!.mp3", True)
        self.assertEqual(rank.progression_count == 1000, True)
        self.assertEqual(rank.risk_reward_multiplier == .1, True)


class TestRankService(unittest.TestCase):
    def test_rank_up(self):
        test_rank = Rank("Damnation", "D", 1, "D-d-d-damn!.mp3" , 1000, .1)
        rank_service = RankService(Ranks(),SoundService(), style_config())
        rank_service.current_progression = 999
        rank_service.apply_points(100)
        self.assertEqual(rank_service.current_rank.name == test_rank.name,True)

    def test_rank_down(self):
        rank_service = RankService(Ranks(),SoundService(), style_config())
        ranks = Ranks()
        rank_service.set_rank(ranks.C)
        rank_service.current_progression = 1
        rank_service.apply_points(-100)
        self.assertEqual(rank_service.current_rank.name == ranks.D.name,True)
    def test_continued_rank_up(self):
        rank_service = RankService(Ranks(), SoundService(), style_config())
        ranks = Ranks()
        rank_service.current_progression = 100
        rank_service.apply_points(rank_service.current_rank.progression_count)
        self.assertEqual(rank_service.current_rank.name == ranks.D.name, True)
        rank_service.current_progression = 100
        rank_service.apply_points(rank_service.current_rank.progression_count)
        self.assertEqual(rank_service.current_rank.name == ranks.C.name, True)
        rank_service.current_progression = 100
        rank_service.apply_points(rank_service.current_rank.progression_count)
        self.assertEqual(rank_service.current_rank.name == ranks.B.name, True)
        rank_service.current_progression = 100
        rank_service.apply_points(rank_service.current_rank.progression_count)
        self.assertEqual(rank_service.current_rank.name == ranks.A.name, True)
        rank_service.current_progression = 100
        rank_service.apply_points(rank_service.current_rank.progression_count)
        self.assertEqual(rank_service.current_rank.name == ranks.S.name, True)
        rank_service.current_progression = 100
        rank_service.apply_points(rank_service.current_rank.progression_count)
        self.assertEqual(rank_service.current_rank.name == ranks.SS.name, True)
        rank_service.current_progression = 100
        rank_service.apply_points(rank_service.current_rank.progression_count)
        self.assertEqual(rank_service.current_rank.name == ranks.SSS.name, True)
        rank_service.current_progression = 100
        rank_service.apply_points(rank_service.current_rank.progression_count)
        self.assertEqual(rank_service.current_rank.name == ranks.SSS.name, True)


class TestConfiguration(unittest.TestCase):
    def test_config_author(self):
        test = style_config()
        self.assertEqual(test.author == "Berky", True, "should show default author")
        test.author = "Dante"
        self.assertEqual(test.author == "Dante", True , "should change author")




class TestSoundBehavior(unittest.TestCase):
    def test_sound_behavior(self):
        rank_service = RankService(Ranks(), SoundService(), style_config())
        ranks = Ranks()
        rank_service.set_rank(ranks.S)
        rank_service.current_progression = 1
        rank_service.apply_points(-100)
        self.assertEquals(rank_service.current_rank.activation_sound == "A.wav", True)


class TestThreadBehavior(unittest.TestCase):
    def test_threading_behavior(self):
        game_loop = GameLoop(RankService(Ranks(),SoundService(), style_config()))
        game_loop.rank_service.decreaseValue = 50
        ranks = Ranks()
        game_loop.rank_service.set_rank(ranks.S)
        time.sleep(5)
        self.assertEquals(game_loop.rank_service.current_rank.name != ranks.S.name,True)
        game_loop.rank_service_running = False


if __name__ == '__main__':
    unittest.main()
