import pyglet
from pyglet.window import key, mouse
import random

# Draws the window
window = pyglet.window.Window(resizable=True, caption="Pyglet window with A CAT")
window.set_minimum_size(320, 200)
window.set_maximum_size(1024, 768)

# Label for 'hello world' text
label = pyglet.text.Label(
    "Hello, world",
    font_name="Times New Roman",
    font_size=36,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x="center",
    anchor_y="center",
)

# Loads the image (from the working directory)
cat_texture = pyglet.resource.image("image.png")

# Creates a sprite from the image
cat_sprite = pyglet.sprite.Sprite(cat_texture)
# cat_sprite.x = 300
# cat_sprite.y = 200
# cat_sprite.scale = 0.5

# Circle color variables
c_R = 25
c_G = 45
c_B = 75
cir_x = window.width / 2
cir_y = window.height / 2
cir_radius = 25


# Function to randomly change circle color
def change_circle_color():
    global c_R, c_G, c_B
    c_R = max(5, min(c_R + random.randint(-25, 25), 255))
    c_G = max(5, min(c_G + random.randint(-25, 25), 255))
    c_B = max(5, min(c_B + random.randint(-25, 25), 255))
    return print("Circle color changed")


# On key press (down)
@window.event
def on_key_press(symbol, modifiers):
    global cir_x, cir_y
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print("The left arrow key was pressed.")
        if cir_x > cir_radius:
            cir_x -= 15
    elif symbol == key.RIGHT:
        if cir_x < window.width - cir_radius:
            cir_x += 15
    elif symbol == key.DOWN:
        if cir_y > cir_radius:
            cir_y -= 15
    elif symbol == key.UP:
        if cir_y < window.height - cir_radius:
            cir_y += 15
    elif symbol == key.C:
        cat_sprite.draw()  # This shit doesn't work. Figure it out later :(
    elif symbol == key.T:
        print(f"Window size: {window.width} x {window.height}")
    elif symbol == key.ENTER:
        print("The enter key was pressed.")
    elif symbol == key.Q and modifiers == key.MOD_CTRL:
        pyglet.app.exit()


# On mouse events
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("The left mouse button was pressed.")
    elif button == mouse.RIGHT:
        change_circle_color()


# On drawing the window....
@window.event
def on_draw():
    window.clear()
    # Draw the cat image
    cat_sprite.draw()  # this works
    # Draw 'hello world'
    label.draw()
    # Shapes
    circle = pyglet.shapes.Circle(
        x=cir_x, y=cir_y, radius=cir_radius, color=(c_R, c_G, c_B)
    )
    circle.draw()


# The following 2 lines log different event types you can handle on a window
# event_logger = pyglet.window.event.WindowEventLogger()
# window.push_handlers(event_logger)

pyglet.app.run()
