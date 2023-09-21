from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def render_frame(x, y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)

def run_circle():
    print('circle')

    # 일단 그림을 그리자
    cx, cy, r = 400, 300, 200

    for deg in range(270, 630,1):
        x = r * math.cos(math.radians(deg)) + cx
        y = r * math.sin(math.radians(deg)) + cy
        render_frame(x, y)

def run_rectangle():
    print('rectangle')
    
    for x in range(50,750+1,10): 
        render_frame(x,90)

    for y in range(90, 510+1, 10): 
        render_frame(750,y)
        
    for x in range(750,50-1,-10): 
        render_frame(x,510)
        
    for y in range(510, 90-1, -10):
        render_frame(50,y)

while True:
    run_circle()
    run_rectangle()
    break

close_canvas()
