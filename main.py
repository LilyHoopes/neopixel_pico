import time
from neopixel import Neopixel
 
numpix = 30
pixels = Neopixel(numpix, 0, 28, "GRBW")
 
pink = (200, 21, 133)
red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
teal = (0, 255, 110)
blue = (0, 0, 255)
purple = (75, 0, 130)
white = (255, 255, 255)
color0 = red
 
pixels.brightness(50)
#pixels.set_pixel_line(0, 30, white)
pixels.fill(teal)
#pixels.set_pixel_line_gradient(0, 29, green, blue)
#pixels.set_pixel_line(14, 16, red)
#pixels.set_pixel(20, (255, 255, 255))
pixels.show()

"""
while True:
    if color0 == red:
       color0 = yellow
       color1 = red
    else:
        color0 = red
        color1 = yellow
    pixels.set_pixel(0, color0)
    pixels.set_pixel(1, color1)
    pixels.show()
    print('hey')
    time.sleep(1)
"""
