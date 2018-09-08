import pyglet


class SoundService(object):
    def __init__(self):
        self.title = "pylet Sound System"
        self.sound_effects_path = "Resources/Sound/SoundEffects/"

    def play_sound(self, sound_name):
        pyglet.resource.media(self.sound_effects_path + sound_name, streaming=False).play()
