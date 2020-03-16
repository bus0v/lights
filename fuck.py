import time
from random import randint
import board
import neopixel


# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
#pixel_pin = board.NeoPixel

# On a Raspberry pi, use this instead, not all pins are supported
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 10

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRBW


pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
  while(True):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def twinkle(wait):
  while(True):
    
    
    pixel_index=randint(0,9)
    for i in range(1000,0,-1):
      bright=i/10
      pixels[pixel_index]=(0,0,bright,0)
      pixels.show()
      time.sleep(wait)
   # time.sleep(wait)
    pixels[pixel_index] = (0,0,0,0)
    time.sleep(wait*10)

def pong(wait):
    n=0
    while(n<10):
        for i in range(10):
            pixel_index =int(i/10*255)
            pixels[i] = wheel(pixel_index)
            pixels.show()
            time.sleep(wait)
            pixels[i] = (0,0,0,0)
        for j in range(9,0,-1):
            #print("j",j)
            pixel_index=int(j/10*255)        
            pixels[j] = wheel(pixel_index)
            pixels.show()
            time.sleep(wait)
            pixels[j] = (0,0,0,0)
        n=n+1

def main():
    # Comment this line out if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    #pixels.fill((255, 0, 0, 0)
    
    #pixels.show()
    #time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    #pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    #pixels.fill((0, 255, 0, 0))
    #pixels.show()
    #time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    #pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    #pixels.fill((0, 0, 255, 0))
    #pixels.show()
    #time.sleep(1)
    #pong(0.05)
    twinkle(0.01)
    #rainbow_cycle(0.001)    # rainbow cycle with 1ms delay per step

if __name__=="__main__":
    main()
    
