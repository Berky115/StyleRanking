import threading
import time
import pyglet

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
        self.D = Rank("Damnation", "D", 1, "D.wav" , 1000, 1.25)
        self.C = Rank("Crazy!", "C", 2, "C.wav", 1300, 1.5)
        self.B = Rank("Bravo!", "B", 3, "B.wav", 1500, 1.75)
        self.A = Rank("Anarchy!", "A", 4, "A.wav", 1700, 2)
        self.S = Rank("Sensational!", "S", 5, "S.wav", 2000, 2.25)
        self.SS = Rank("Sexy Style!", "SS", 6, "SS.wav", 3000, 2.5)
        self.SSS = Rank("Sweet Son of Sparda!", "SSS.wav", 7, "SSS.mp3" , 4000, 3)

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
    def __init__(self, rank_list, sound_service):
        self.rank_List = rank_list
        self.current_rank = self.rank_List.get_rank(0)
        self.max_progression = self.current_rank.progression_count
        self.current_progression = 10
        self.orb_multiplier = self.current_rank.orb_multiplier
        self.decreaseValue = 1
        self.sound_service = sound_service

    def polling_value(self):
        #Debug:
        print(self.current_progression , " / " , self.max_progression )
        print(self.current_rank.name)

        if self.current_rank.priority > 0:
            self.current_progression -= self.decreaseValue;

        if self.current_progression < 0 and self.current_rank.priority > 0:
            self.rank_down()
            self.sound_service.play_sound(self.current_rank.activation_sound)

        if self.current_progression > self.max_progression and self.current_rank.priority <7:
            self.rank_up()
            self.sound_service.play_sound(self.current_rank.activation_sound)

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

class SoundService(object):
    def __init__(self):
        self.title = "pylet Sound System"
        self.sound_effects_path = "Resources/Sound/SoundEffects/"

    def play_sound(self, sound_name):
        pyglet.resource.media(self.sound_effects_path + sound_name, streaming=False).play()


