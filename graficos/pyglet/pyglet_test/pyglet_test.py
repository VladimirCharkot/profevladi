import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image('tren.gif')

@window.event
def on_draw():
    window.clear()
    image.blit(70, 0)

pyglet.app.run()
