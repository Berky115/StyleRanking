import pyglet
import os


class SoundService(object):
    def __init__(self):
        self.title = "pylet Sound System"
        self.sound_effects_path = "Resources/Sound/SoundEffects/"
        self.music_path = "Resources/Sound/Music/"
        self.current_background_song = "NONE"
        self.media_player = pyglet.media.Player()

    def play_sound_effect(self, sound_name):
        # Go up to root directory
        os.chdir("..")
        pyglet.resource.media( self.sound_effects_path + sound_name, streaming=False).play()

    def play_background_music(self, song_name):
        os.chdir("..")
        song = pyglet.resource.media(self.music_path + song_name, streaming=True)
        self.media_player.queue(song)
        self.media_player.play()
        self.current_background_song = song_name

    def stop_background_music(self):
        os.chdir("..")
        pyglet.resource.media(self.music_path + self.current_background_song, streaming=True)
        self.media_player.pause()
        self.current_background_song = "NONE"