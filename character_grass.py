from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
circle = 360

while( x < 750 ):
   clear_canvas_now()
   grass.draw_now(400, 30)
   character.draw_now(x, y)
   x = x + 2
   delay(0.01)

while( y < 550 ):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    y = y + 2
    delay(0.01)

while( x > 0 ):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    x = x - 2
    delay(0.01)

while ( y > 80 ):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    y = y - 2
    delay(0.01)
    
while 1:
    clear_canvas_now()
    grass.draw_now(400, 30)
    x = 400 + 200 * math.sin(math.radians(circle))
    y = 400 - 200 * math.cos(math.radians(circle))
    character.draw_now(x, y)
    circle = circle + 1
    if(circle < 360):
        circle = 0
    delay(0.01)

close_canvas()
