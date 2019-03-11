import pyglet
import os


class RenderObject(object):
    def __init__(self, x_pos, y_pos, image):
        self.xPos = x_pos
        self.yPos = y_pos
        self.image = image


class RenderService(object):
    def __init__(self):
        self.name = "Style Rank Rendering Service"
        self.image_resource_path = "Resources/Images/"

    def display_object(self,render_object):
        # Go up to root directory
        os.chdir("..")
        window = pyglet.window.Window()
        image = pyglet.resource.image(self.image_resource_path + render_object.image)

        @window.event
        def on_draw():
            window.clear()
            image.blit(render_object.xPos, render_object.yPos)
        pyglet.app.event_loop.run()


    def close_window(self):
        pyglet.app.EventLoop().exit()