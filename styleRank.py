import threading
import time


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

        self.rank_list = {
            0 : self.NONE,
            1 : self.D,
            2 : self.C,
            3 : self.B,
            4 : self.A,
            5 : self.S,
            6 : self.SS,
            7 : self.SSS
        }

    def get_rank(self, priority):
        return self.rank_list[priority]


class RankService(object):
    def __init__(self, rank_list):
        self.rank_List = rank_list
        self.current_rank = self.rank_List.get_rank(0)
        self.max_progression = self.current_rank.progression_count
        self.current_progression = 10
        self.orb_multiplier = self.current_rank.orb_multiplier
        self.decreaseValue = 1;

    def polling_value(self):
        #Debug:
        print(self.current_progression , " / " , self.max_progression )
        print(self.current_rank.name)

        if self.current_rank.priority > 0:
            self.current_progression -= self.decreaseValue;

        if self.current_progression < 0 and self.current_rank.priority > 0:
            self.rank_down()

        if self.current_progression > self.max_progression and self.current_rank.priority <7:
            self.rank_up()

    def apply_points(self, new_points):
        self.current_progression += new_points * self.orb_multiplier
        if self.current_progression > self.max_progression:
            self.rank_up()
        elif self.current_progression < 0:
            self.rank_down()

    def rank_up(self):
        self.current_progression = self.current_progression - self.max_progression
        self.current_rank = self.rank_List.get_rank(self.current_rank.priority + 1)
        self.max_progression = self.current_rank.progression_count
        self.orb_multiplier = self.current_rank.orb_multiplier
        #Debug:
        print(self.current_rank.activation_sound)

    def rank_down(self):
        self.current_rank = self.rank_List.get_rank(self.current_rank.priority - 1)
        self.max_progression = self.current_rank.progression_count
        self.orb_multiplier = self.current_rank.orb_multiplier
        self.current_progression = self.max_progression // 2
        #Debug:
        print(self.current_rank.activation_sound)

    def set_rank(self, rank):
        self.current_rank = rank
        self.max_progression = rank.progression_count
        self.orb_multiplier = rank.orb_multiplier


class GameLoop(threading.Thread):
    def __init__(self,rank_service):
        self.rank_service = rank_service
        self.rank_service_running = True
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        while self.rank_service_running:
            time.sleep(1)
            self.rank_service.polling_value()


