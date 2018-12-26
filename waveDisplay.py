# Add your Python code here. E.g.
from microbit import *

size = 5

# +1 because the program adds 1 before display
base_a = [[(i+j)+1 for j in range(size)] for i in range(size)]
base_b = [[9-(i+j)+1 for j in range(size)] for i in range(size)]

def deepcopy(src):
    return [[j for j in i] for i in src] 

leds = deepcopy(base_b)
img = Image(5,5)


while True:
    
    if button_a.is_pressed() and button_b.is_pressed():
        display.clear()
        break
    elif button_a.is_pressed():
        leds = deepcopy(base_a)
    elif button_b.is_pressed():
        leds = deepcopy(base_b)
    
    
    for y in range(size):
        for x in range(size):
            leds[y][x] = (leds[y][x] - 1) % 9
            img.set_pixel(x, y, leds[y][x])
            
    
    display.show(img)
    
    sleep(150)        
            
