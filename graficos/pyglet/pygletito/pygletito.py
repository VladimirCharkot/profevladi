import pyglet
from pyglet.window import key

window = pyglet.window.Window() # WINDOW_STYLE_BORDERLESS

imagenes = []
for i in range(4):
    imagen = pyglet.resource.image(f'sprite/{i+1}.png')
    imagenes.append(imagen)
    
anim = pyglet.image.Animation.from_image_sequence(imagenes, 0.1, True)
sprite = pyglet.sprite.Sprite(anim)

window.set_icon(imagenes[0])

keys = key.KeyStateHandler()
window.push_handlers(keys)

def leer_teclado():
    global x, y
    if keys[key.UP]:
        y += 10
    if keys[key.LEFT]:
        x -= 10
    if keys[key.DOWN]:
        y -= 10
    if keys[key.RIGHT]:
        x += 10

def movimiento():
    sprite.x = x
    sprite.y = y
    sprite.draw()
    limites()

def limites():
    global x, y
    if y > 500:
        y = -30
    if y < -40:
        y = 490
    if x > 650:
        x = -40
    if x < -50:
        x = 640

pyglet.clock.schedule_interval(lambda t: t, 1/60.0)


x, y = 10, 10

@window.event
def on_draw():
    leer_teclado()
    movimiento()
    window.clear()
    sprite.draw()

@window.event
def on_key_press(symbol, modifiers):
    global x, y, keys
    keys[symbol] = True

@window.event
def on_key_release(symbol, modifiers):
    global keys
    keys[symbol] = False
    
    
##event_logger = pyglet.window.event.WindowEventLogger()
##window.push_handlers(event_logger)

pyglet.app.run()
