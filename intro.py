import neopixel #importing the library
import time
from machine import Pin # another way of importing a library
lights = neopixel.NeoPixel(Pin(15),2) # 0 is the Pin for neopixel and 4 is the number of lights
count = 0
while True:
    lights[0] = (0 + count, 85 + count, 170 + count) # set the color of 0th light to purple
    lights.write()
    count = count + 1
    if count == 255:
        count = 0
    time.sleep_ms(3)
