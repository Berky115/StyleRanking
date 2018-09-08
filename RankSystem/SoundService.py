import pyglet
import os


class SoundService(object):
    def __init__(self):
        self.title = "pylet Sound System"
        self.sound_effects_path = "Resources/Sound/SoundEffects/"
        self.music_path = "Resources/Sound/Music/"
        self.current_background_song = "No song playing"

    def play_sound_effect(self, sound_name):
        # Go up to root directory
        os.chdir("..")
        pyglet.resource.media( self.sound_effects_path + sound_name, streaming=False).play()

    def play_background_music(self, song_name):
        os.chdir("..")
        pyglet.resource.media(self.music_path + song_name, streaming=True).play()
        self.current_background_song = song_name