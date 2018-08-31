class Rank(object):
    def __init__(self, name, glyph, priority, activation_sound, progression_count, orb_multiplier):
        self.name = name
        self.glyph = glyph
        self.priority = priority
        self.activation_sound = activation_sound
        self.progression_count = progression_count
        self.orb_multiplier = orb_multiplier

class Ranks(object):
    def __init__(self):
        self.NONE = Rank("","",0,"",1000,1)
        self.D = Rank("Damnation", "D", 1, "D-d-d-damn!.mp3" , 1000, 1.25)
        self.C = Rank("Crazy!", "C", 2, "CRAZY.mp3" , 1300, 1.5)
        self.B = Rank("Bravo!", "B", 3, "Bravo.mp3" , 1500, 1.75)
        self.A = Rank("Anarchy!", "A", 4, "Anarchy.mp3" , 1700, 2)
        self.S = Rank("Sensational!", "S", 5, "Sensational.mp3" , 2000, 2.25)
        self.SS = Rank("Sexy Style!", "SS", 6, "SSensational.mp3" , 3000, 2.5)
        self.SSS = Rank("Sweet Son of Sparda!", "SSS", 7, "SSSensational.mp3" , 4000, 3)


class RankService(object):
    def __init__(self):
        self.rank_List = [
            Rank("","",0,"",1000,1) ,
            Rank("Damnation", "D", 1, "D-d-d-damn!.mp3" , 1000, 1.25),
            Rank("Crazy!", "C", 2, "CRAZY.mp3" , 1300, 1.5),
            Rank("Bravo!", "B", 3, "Bravo.mp3" , 1500, 1.75),
            Rank("Anarchy!", "A", 4, "Anarchy.mp3" , 1700, 2),
            Rank("Sensational!", "S", 5, "Sensational.mp3" , 2000, 2.25),
            Rank("Sexy Style!", "SS", 6, "SSensational.mp3" , 3000, 2.5),
            Rank("Sweet Son of Sparda!", "SSS", 7, "SSSensational.mp3" , 4000, 3)
           ]
        self.current_rank = self.rank_List[0]
        self.max_progression = self.current_rank.progression_count
        self.current_progression = 0
        self.orb_multiplier = self.current_rank.orb_multiplier
    def applyPoints(self, new_points):
        self.current_progression += new_points * self.orb_multiplier
        if self.current_progression > self.max_progression:
            self.rankUp()
        elif self.current_progression < 0:
            self.rankDown()
    def rankUp(self):
        self.current_progression = self.current_progression - self.max_progression
        self.current_rank = self.rank_List[self.current_rank.priority + 1]
        self.max_progression = self.current_rank.progression_count
        self.orb_multiplier = self.current_rank.orb_multiplier
    def rankDown(self):
        self.current_rank = self.rank_List[self.current_rank.priority - 1]
        self.max_progression = self.current_rank.progression_count
        self.orb_multiplier = self.current_rank.orb_multiplier
        self.current_progression = self.max_progression // 2
    def setRank(self, rank):
        self.current_rank = rank
        self.max_progression = rank.progression_count
        self.orb_multiplier = rank.orb_multiplier
