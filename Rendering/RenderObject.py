import pyglet

class Render_object(object):
    def __init__(self, image):
        self.xPos = 0
        self.yPos = 0
        self.image = image

    @window.event
    def input_handler(self,symbol,modifiers):
        if symbol == 97:
            self.xPos +=1
        elif symbol.xPos == 100:
            self.xPos -=1



# window = pyglet.window.Window()
# image = pyglet.resource.image('logo.jpg')
# xPos = 0
#
# @window.event
# def on_key_press(symbol, modifiers):
#     print('A key was pressed', symbol, modifiers)
#     if symbol == 97:
#         xPos -= 1
#     elif symbol == 100:
#         xPos += 1
#
# @window.event
# def on_draw():
#     window.clear()
#
# @window.event
# def on_draw():
#     window.clear()
#     image.blit(xPos, 0)
#
# pyglet.app.run()