import unittest
import threading
import time

from styleRank import Rank, Ranks, RankService, GameLoop

class TestRankFunctionality(unittest.TestCase):
    def test_can_make_rank(self):
        rank = Rank("Damnation", "D", 1, "D-d-d-damn!.mp3" , 1000, .1)
        self.assertEquals(rank.name == "Damnation", True)
        self.assertEquals(rank.glyph == "D", True)
        self.assertEquals(rank.priority == 1, True)
        self.assertEquals(rank.activation_sound == "D-d-d-damn!.mp3", True)
        self.assertEquals(rank.progression_count == 1000, True)
        self.assertEquals(rank.orb_multiplier == .1, True)

class TestRankService(unittest.TestCase):
    def test_rank_up(self):
        test_rank = Rank("Damnation", "D", 1, "D-d-d-damn!.mp3" , 1000, .1)
        rank_service = RankService(Ranks())
        rank_service.current_progression = 999
        rank_service.applyPoints(100)
        self.assertEquals(rank_service.current_rank.name == test_rank.name,True)

    def test_rank_down(self):
        rank_service = RankService(Ranks())
        ranks = Ranks()
        rank_service.setRank(ranks.C)
        rank_service.current_progression = 1
        rank_service.applyPoints(-100)
        self.assertEquals(rank_service.current_rank.name == ranks.D.name,True)


class TestThreadBehavior(unittest.TestCase):
    def test_threading_behavior(self):
        gameLoop = GameLoop(RankService(Ranks()))
        gameLoop.rank_service.decreaseValue = 50
        ranks = Ranks()
        gameLoop.rank_service.setRank(ranks.S)
        time.sleep(5)
        self.assertEquals(gameLoop.rank_service.current_rank.name != ranks.S.name,True)
        gameLoop.rank_service_running = False

if __name__ == '__main__':
    unittest.main()
