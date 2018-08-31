import unittest

from styleRank import Rank, Ranks, RankService

class TestRankFunctionality(unittest.TestCase):
    def test_can_make_rank(self):
        #name, glyph, priority, activation_sound, progression_count, orb_multiplier
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
        rank_service = RankService()
        rank_service.current_progression = 999
        rank_service.applyPoints(100)
        self.assertEquals(rank_service.current_rank.name == test_rank.name,True)
    def test_rank_down(self):
        rank_service = RankService()
        ranks = Ranks()
        rank_service.setRank(ranks.C)
        rank_service.current_progression = 1
        rank_service.applyPoints(-100)
        self.assertEquals(rank_service.current_rank.name == ranks.D.name,True)


if __name__ == '__main__':
    unittest.main()
