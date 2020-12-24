# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from rpi_ws281x import Color, PixelStrip, ws




    #create a function that sets the right led to the right colour for the right amount of time
    # create a function that counts time and checks when notes should come it
    # split parts of the led strip into instruments

# LED strip configuration:
LED_COUNT = 115        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 50  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0
LED_STRIP = ws.SK6812_STRIP_RGBW
#LED_STRIP = ws.SK6812W_STRIP

big_list=[['instrument:', 81, [69, 16.0, 16.1875], [69, 16.25, 16.375], [76, 16.375, 16.5], [74, 16.5, 16.625], [72, 16.625, 16.75], [69, 16.75, 16.875], [69, 17.0, 17.1875], [69, 17.25, 
17.375], [76, 17.375, 17.5], [74, 17.5, 17.625], [72, 17.625, 17.75], [69, 17.75, 17.875], [72, 18.0, 18.125], [71, 18.125, 18.25], [67, 18.25, 18.375], [72, 18.375, 18.625], [71, 18.625, 18.75], [67, 18.75, 19.0], [72, 19.0, 19.125], [71, 19.125, 19.25], [67, 19.25, 19.375], [74, 19.375, 19.625], [71, 19.625, 19.75], [67, 19.75, 19.875], [69, 20.0, 20.1875], [69, 20.25, 20.375], [76, 20.375, 20.5], [74, 20.5, 20.625], [72, 20.625, 20.75], [69, 20.75, 20.875], [69, 21.0, 21.1875], [69, 21.25, 21.375], [76, 21.375, 21.5], [74, 21.5, 21.625], [72, 21.625, 21.75], [69, 21.75, 21.875], [69, 24.0, 24.1875], [69, 24.25, 24.375], [76, 24.375, 24.5], [74, 24.5, 24.625], [72, 24.625, 24.75], [69, 24.75, 24.875], [69, 25.0, 25.1875], [69, 25.25, 25.375], [76, 25.375, 25.5], [74, 25.5, 25.625], [72, 25.625, 25.75], [69, 25.75, 25.875], [72, 26.0, 26.125], [71, 26.125, 26.25], [67, 26.25, 
26.375], [72, 26.375, 26.625], [71, 26.625, 26.75], [67, 26.75, 27.0], [72, 27.0, 27.125], [71, 27.125, 27.25], [67, 27.25, 27.375], [74, 27.375, 27.625], [71, 27.625, 27.75], [67, 27.75, 27.875], [69, 28.0, 28.1875], [69, 28.25, 28.375], [76, 28.375, 28.5], [74, 28.5, 28.625], [72, 28.625, 28.75], [69, 28.75, 28.875], [69, 29.0, 29.1875], [69, 29.25, 29.375], [76, 29.375, 29.5], [74, 29.5, 29.625], [72, 29.625, 29.75], [69, 29.75, 29.875], [69, 32.0, 32.1875], [69, 32.25, 32.375], [76, 32.375, 32.5], [74, 32.5, 32.625], [72, 32.625, 32.75], [69, 32.75, 32.875], [69, 33.0, 33.1875], [69, 33.25, 33.375], [76, 33.375, 33.5], [74, 33.5, 33.625], [72, 33.625, 33.75], [69, 33.75, 33.875], [72, 34.0, 34.125], [71, 34.125, 34.25], [67, 34.25, 34.375], [72, 34.375, 34.625], [71, 34.625, 34.75], [67, 34.75, 35.0], [72, 35.0, 35.125], [71, 35.125, 35.25], [67, 35.25, 35.375], [74, 35.375, 35.625], [71, 35.625, 35.75], [67, 35.75, 35.875], [69, 36.0, 36.1875], [69, 36.25, 36.375], [76, 36.375, 36.5], [74, 36.5, 36.625], [72, 36.625, 36.75], [69, 36.75, 36.875], [69, 37.0, 37.1875], [69, 37.25, 37.375], [76, 37.375, 37.5], [74, 37.5, 37.625], [72, 37.625, 37.75], [69, 37.75, 37.875], [72, 38.0, 38.0625], [72, 38.125, 38.25], [72, 38.375, 
38.4375], [74, 38.5, 38.625], [74, 38.75, 38.875], [76, 39.0, 39.0625], [76, 39.125, 39.25], [76, 39.375, 39.4375], [74, 39.5, 39.625], [74, 39.75, 39.875], [69, 40.0, 40.1875], 
[69, 40.25, 40.375], [76, 40.375, 40.5], [74, 40.5, 40.625], [72, 40.625, 40.75], [69, 40.75, 40.875], [69, 41.0, 41.1875], [69, 41.25, 41.375], [76, 41.375, 41.5], [74, 41.5, 41.625], [72, 41.625, 41.75], [69, 41.75, 41.875], [72, 42.0, 42.125], [71, 42.125, 42.25], [67, 42.25, 42.375], [72, 42.375, 42.625], [71, 42.625, 42.75], [67, 42.75, 43.0], [72, 
43.0, 43.125], [71, 43.125, 43.25], [67, 43.25, 43.375], [74, 43.375, 43.625], [71, 43.625, 43.75], [67, 43.75, 43.875], [69, 44.0, 44.1875], [69, 44.25, 44.375], [76, 44.375, 44.5], [74, 44.5, 44.625], [72, 44.625, 44.75], [69, 44.75, 44.875], [69, 45.0, 45.1875], [69, 45.25, 45.375], [76, 45.375, 45.5], [74, 45.5, 45.625], [72, 45.625, 45.75], [69, 45.75, 45.875]], ['instrument:', 20, [72, 0.0, 0.25], [71, 0.25, 0.5], [72, 1.0, 1.25], [71, 1.25, 1.5], [72, 2.0, 2.25], [71, 2.25, 2.5], [70, 2.5, 2.75], [69, 2.75, 3.0], [68, 3.0, 3.25], [69, 3.25, 3.5], [70, 3.5, 3.75], [71, 3.75, 4.0], [72, 4.0, 4.25], [71, 4.25, 4.5], [72, 5.0, 5.25], [71, 5.25, 5.5], [72, 6.0, 6.25], [71, 6.25, 6.5], [70, 6.5, 6.75], [69, 6.75, 7.0], [68, 7.0, 7.25], [69, 7.25, 7.5], [70, 7.5, 7.75], [71, 7.75, 8.0], [72, 8.0, 8.25], [71, 8.25, 8.5], [72, 9.0, 9.25], [71, 9.25, 9.5], [72, 10.0, 10.25], [71, 
10.25, 10.5], [70, 10.5, 10.75], [69, 10.75, 11.0], [68, 11.0, 11.25], [69, 11.25, 11.5], [70, 11.5, 11.75], [71, 11.75, 12.0], [72, 12.0, 12.25], [71, 12.25, 12.5], [72, 13.0, 13.25], [71, 13.25, 13.5], [72, 14.0, 14.25], [71, 14.25, 14.5], [70, 14.5, 14.75], [69, 14.75, 15.0], [68, 15.0, 15.25], [69, 15.25, 15.5], [70, 15.5, 15.75], [71, 15.75, 16.0], 
[72, 30.0, 30.25], [71, 30.25, 30.5], [70, 30.5, 30.75], [69, 30.75, 31.0], [68, 31.0, 31.25], [69, 31.25, 31.5], [70, 31.5, 31.75], [71, 31.75, 32.0], [72, 46.0, 46.25], [71, 46.25, 46.5], [70, 46.5, 46.75], [69, 46.75, 47.0], [68, 47.0, 47.25], [69, 47.25, 47.5], [70, 47.5, 47.75], [71, 47.75, 48.0]], ['instrument:', 38, [41, 32.25, 32.5], [41, 32.75, 
33.0], [43, 33.25, 33.5], [43, 33.75, 34.0], [45, 34.25, 34.5], [45, 34.75, 35.0], [45, 35.25, 35.5], [45, 35.75, 36.0], [38, 36.25, 36.5], [38, 36.75, 37.0], [40, 37.25, 37.5], 
[40, 37.75, 38.0], [45, 38.25, 38.5], [45, 38.75, 39.0], [45, 39.25, 39.5], [45, 39.75, 40.0], [41, 40.25, 40.5], [41, 40.75, 41.0], [43, 41.25, 41.5], [43, 41.75, 42.0], [45, 42.25, 42.5], [45, 42.75, 43.0], [45, 43.25, 43.5], [45, 43.75, 44.0], [38, 44.25, 44.5], [38, 44.75, 45.0], [38, 45.25, 45.5], [38, 45.75, 46.0]], ['instrument:', 0, [42, 0.0, 0.125], [36, 0.0, 0.125], [42, 0.25, 0.375], [39, 0.5, 0.625], [42, 0.5, 0.625], [42, 1.0, 1.125], [36, 1.0, 1.125], [42, 1.25, 1.375], [36, 1.25, 1.375], [39, 1.5, 1.625], [42, 1.5, 1.625], [42, 2.0, 2.125], [36, 2.0, 2.125], [42, 2.25, 2.375], [42, 2.5, 2.625], [39, 2.5, 2.625], [42, 3.0, 3.125], [36, 3.0, 3.125], [42, 3.25, 3.375], [36, 3.25, 3.375], [42, 3.5, 3.625], [39, 3.5, 3.625], [42, 4.0, 4.125], [36, 4.0, 4.125], [42, 4.25, 4.375], [39, 4.5, 4.625], [42, 4.5, 4.625], [42, 5.0, 5.125], [36, 5.0, 5.125], [42, 5.25, 5.375], [36, 5.25, 5.375], [39, 5.5, 5.625], [42, 5.5, 5.625], [42, 6.0, 6.125], [36, 6.0, 6.125], [42, 6.25, 6.375], [42, 6.5, 6.625], [39, 6.5, 6.625], [42, 7.0, 7.125], [36, 7.0, 7.125], [42, 7.25, 7.375], [36, 7.25, 7.375], [42, 7.5, 7.625], [39, 7.5, 7.625], [42, 8.0, 8.125], [36, 8.0, 8.125], [42, 8.25, 8.375], [39, 8.5, 8.625], [42, 8.5, 8.625], [42, 9.0, 9.125], [36, 9.0, 9.125], [42, 9.25, 9.375], [36, 9.25, 9.375], [39, 9.5, 9.625], [42, 9.5, 9.625], [42, 10.0, 10.125], [36, 10.0, 10.125], [42, 10.25, 10.375], [42, 10.5, 10.625], [39, 10.5, 10.625], [42, 11.0, 11.125], [36, 11.0, 11.125], [42, 11.25, 11.375], [36, 11.25, 11.375], [42, 11.5, 11.625], [39, 11.5, 11.625], [42, 12.0, 12.125], [36, 12.0, 
12.125], [42, 12.25, 12.375], [39, 12.5, 12.625], [42, 12.5, 12.625], [42, 13.0, 13.125], [36, 13.0, 13.125], [42, 13.25, 13.375], [36, 13.25, 13.375], [39, 13.5, 13.625], [42, 13.5, 13.625], [42, 14.0, 14.125], [36, 14.0, 14.125], [42, 14.25, 14.375], [42, 14.5, 14.625], [39, 14.5, 14.625], [42, 15.0, 15.125], [36, 15.0, 15.125], [42, 15.25, 15.375], [36, 15.25, 15.375], [42, 15.5, 15.625], [39, 15.5, 15.625], [42, 16.0, 16.125], [36, 16.0, 16.125], [36, 24.0, 24.25], [36, 24.5, 24.75], [36, 25.0, 25.25], [36, 25.5, 25.75], [36, 26.0, 26.25], [36, 26.5, 26.75], [36, 27.0, 27.25], [36, 27.5, 27.75], [36, 28.0, 28.25], [36, 28.5, 28.75], [36, 29.0, 29.25], [36, 29.5, 29.75], [42, 30.0, 30.125], [36, 30.0, 30.125], [42, 30.25, 30.375], [42, 30.5, 30.625], [39, 30.5, 30.625], [42, 31.0, 31.125], [36, 31.0, 31.125], [42, 31.25, 31.375], [36, 31.25, 31.375], [42, 31.5, 31.625], [39, 31.5, 31.625], [36, 32.0, 32.25], [42, 32.25, 32.5], [36, 32.5, 32.75], [39, 32.5, 32.75], [42, 32.75, 33.0], [36, 33.0, 33.25], [42, 33.25, 33.5], [36, 33.5, 33.75], [39, 33.5, 33.75], [42, 33.75, 34.0], [36, 34.0, 34.25], [42, 34.25, 34.5], [36, 34.5, 34.75], [39, 34.5, 34.75], [42, 34.75, 35.0], [36, 35.0, 35.25], [42, 35.25, 35.5], [36, 35.5, 35.75], [39, 35.5, 35.75], [42, 35.75, 36.0], [36, 36.0, 36.25], [42, 36.25, 36.5], [36, 36.5, 36.75], [39, 36.5, 36.75], [42, 36.75, 37.0], [36, 37.0, 37.25], [42, 37.25, 37.5], [36, 
37.5, 37.75], [39, 37.5, 37.75], [42, 37.75, 38.0], [36, 38.0, 38.25], [42, 38.25, 38.5], [39, 38.5, 38.75], [36, 38.5, 38.75], [42, 38.75, 39.0], [36, 39.0, 39.25], [42, 39.25, 
39.5], [39, 39.5, 39.75], [36, 39.5, 39.75], [42, 39.75, 40.0], [36, 40.0, 40.25], [42, 40.25, 40.5], [36, 40.5, 40.75], [39, 40.5, 40.75], [42, 40.75, 41.0], [36, 41.0, 41.25], 
[42, 41.25, 41.5], [36, 41.5, 41.75], [39, 41.5, 41.75], [42, 41.75, 42.0], [36, 42.0, 42.25], [42, 42.25, 42.5], [36, 42.5, 42.75], [39, 42.5, 42.75], [42, 42.75, 43.0], [36, 43.0, 43.25], [42, 43.25, 43.5], [36, 43.5, 43.75], [39, 43.5, 43.75], [42, 43.75, 44.0], [36, 44.0, 44.25], [42, 44.25, 44.5], [36, 44.5, 44.75], [39, 44.5, 44.75], [42, 44.75, 45.0], [36, 45.0, 45.25], [42, 45.25, 45.5], [36, 45.5, 45.75], [39, 45.5, 45.75], [42, 45.75, 46.0], [36, 46.0, 46.125], [42, 46.0, 46.125], [42, 46.25, 46.375], [42, 46.5, 46.625], [39, 46.5, 46.625], [42, 47.0, 47.125], [36, 47.0, 47.125], [42, 47.25, 47.375], [36, 47.25, 47.375], [42, 47.5, 47.625], [39, 47.5, 47.625], [49, 48.0, 48.25], [36, 48.0, 48.25]]]

# Define functions which animate LEDs in various ways.


best_list=[['Piano', 42, 0.0, 0.125], ['Piano', 36, 0.0, 0.125], ['Piano', 42, 0.25, 0.375], ['Piano', 39, 0.5, 0.625], ['Piano', 42, 0.5, 0.625], 
['Piano', 42, 1.0, 1.125], ['Piano', 36, 1.0, 1.125], ['Piano', 42, 1.25, 1.375], ['Piano', 36, 1.25, 1.375], ['Piano', 39, 1.5, 1.625],
 ['Piano', 42, 1.5, 1.625], ['Piano', 42, 2.0, 2.125], ['Piano', 36, 2.0, 2.125], ['Piano', 42, 2.25, 2.375], ['Piano', 42, 2.5, 2.625], 
 ['Piano', 39, 2.5, 2.625], ['Piano', 42, 3.0, 3.125], ['Piano', 36, 3.0, 3.125], ['Piano', 42, 3.25, 3.375], ['Piano', 36, 3.25, 3.375],
  ['Piano', 42, 3.5, 3.625], ['Piano', 39, 3.5, 3.625], ['Piano', 42, 4.0, 4.125], ['Piano', 36, 4.0, 4.125], ['Piano', 42, 4.25, 4.375],
   ['Piano', 39, 4.5, 4.625], ['Piano', 42, 4.5, 4.625], ['Piano', 42, 5.0, 5.125], ['Piano',36, 5.0, 5.125], ['Piano', 42, 5.25, 5.375], 
   ['Piano', 36, 5.25, 5.375], ['Piano', 39, 5.5, 5.625], ['Piano', 42, 5.5, 5.625], ['Piano', 42, 6.0, 6.125], ['Piano', 36, 6.0, 6.125], 
   ['Piano', 42, 6.25, 6.375], ['Piano', 42, 6.5, 6.625], ['Piano', 39, 6.5, 6.625], ['Piano', 42, 7.0, 7.125], ['Piano', 36, 7.0, 7.125], 
   ['Piano', 42, 7.25, 7.375], ['Piano', 36, 7.25, 7.375], ['Piano', 42, 7.5, 7.625], ['Piano', 39, 7.5, 7.625], ['Piano', 42, 8.0, 8.125], 
   ['Piano', 36, 8.0, 8.125], ['Piano', 42, 8.25, 8.375], ['Piano', 39, 8.5, 8.625], ['Piano', 42, 8.5, 8.625], ['Piano', 42, 9.0, 9.125], 
   ['Piano', 36, 9.0, 9.125], ['Piano', 42, 9.25, 9.375], ['Piano', 36, 9.25, 9.375], ['Piano', 39, 9.5, 9.625], ['Piano', 42, 9.5, 9.625], 
   ['Piano', 42, 10.0, 10.125], ['Piano', 36, 10.0, 10.125], ['Piano', 42, 10.25, 10.375], ['Piano', 42, 10.5, 10.625], ['Piano', 39, 10.5, 10.625],
    ['Piano', 42, 11.0, 11.125], ['Piano', 36, 11.0, 11.125], ['Piano', 42, 11.25, 11.375], ['Piano', 36, 11.25, 11.375], ['Piano', 42, 11.5, 11.625],
     ['Piano', 39, 11.5, 11.625], ['Piano', 42, 12.0, 12.125], ['Piano', 36, 12.0, 12.125], ['Piano', 42, 12.25, 12.375], ['Piano', 39, 12.5, 12.625],
      ['Piano', 42, 12.5, 12.625], ['Piano', 42, 13.0, 13.125], ['Piano', 36, 13.0, 13.125], ['Piano', 42, 13.25, 13.375], ['Piano', 36, 13.25, 13.375],
       ['Piano', 39, 13.5, 13.625], ['Piano', 42, 13.5, 13.625], ['Piano', 42, 14.0, 14.125], ['Piano', 36, 14.0, 14.125], ['Piano', 42, 14.25, 14.375],
        ['Piano', 42, 14.5, 14.625], ['Piano', 39, 14.5, 14.625], ['Piano', 42, 15.0, 15.125], ['Piano', 36, 15.0, 15.125], ['Piano', 42, 15.25, 15.375],
         ['Piano', 36, 15.25, 15.375], ['Piano', 42, 15.5, 15.625], ['Piano', 39, 15.5, 15.625], ['Piano', 42, 16.0, 16.125], ['Piano', 36, 16.0, 16.125],
          ['Piano', 36, 24.0, 24.25], ['Piano', 36, 24.5, 24.75], ['Piano', 36, 25.0, 25.25], ['Piano', 36, 25.5, 25.75], ['Piano', 36, 26.0, 26.25],
           ['Piano', 36, 26.5, 26.75], ['Piano', 36, 27.0, 27.25], ['Piano', 36, 27.5, 27.75], ['Piano', 36, 28.0, 28.25], ['Piano', 36, 28.5, 28.75],
            ['Piano', 36, 29.0, 29.25], ['Piano', 36, 29.5, 29.75], ['Piano', 42, 30.0, 30.125], ['Piano', 36, 30.0, 
30.125], ['Piano', 42, 30.25, 30.375], ['Piano', 42, 30.5, 30.625], ['Piano', 39, 30.5, 30.625], ['Piano', 42, 31.0, 31.125], ['Piano', 36, 31.0, 31.125],
 ['Piano', 42, 31.25, 31.375], ['Piano', 36, 31.25, 31.375], ['Piano', 42, 31.5, 31.625], ['Piano', 39, 31.5, 31.625], ['Piano', 36, 32.0, 32.25], 
 ['Piano', 42, 32.25, 32.5], ['Piano', 36, 32.5, 32.75], ['Piano', 39, 32.5, 32.75], ['Piano', 42, 32.75, 33.0], ['Piano', 36, 33.0, 33.25],
  ['Piano', 42, 33.25, 33.5], ['Piano', 36, 33.5, 33.75], ['Piano', 39, 33.5, 33.75], ['Piano', 42, 33.75, 34.0], ['Piano', 36, 34.0, 34.25],
  ['Piano', 42, 34.25, 34.5], ['Piano', 36, 34.5, 34.75], ['Piano', 39, 34.5, 34.75], ['Piano', 42, 34.75, 35.0], ['Piano', 36, 35.0, 35.25], 
  ['Piano', 42, 35.25, 35.5], ['Piano', 36, 35.5, 35.75], ['Piano', 39, 35.5, 35.75], ['Piano', 42, 35.75, 36.0], ['Piano', 36, 36.0, 36.25], 
  ['Piano', 42, 36.25, 36.5], ['Piano', 36, 36.5, 36.75], ['Piano', 39, 36.5, 36.75], ['Piano', 42, 36.75, 37.0], ['Piano', 36, 37.0, 37.25], 
  ['Piano', 42, 37.25, 37.5], ['Piano', 36, 37.5, 37.75], ['Piano', 39, 37.5, 37.75], ['Piano', 42, 37.75, 38.0], ['Piano', 36, 38.0, 38.25], 
  ['Piano', 42, 38.25, 38.5], ['Piano', 39, 38.5, 38.75], ['Piano', 36, 38.5, 38.75], ['Piano', 42, 38.75, 39.0], ['Piano', 36, 39.0, 39.25], 
  ['Piano', 42, 39.25, 39.5], ['Piano', 39, 39.5, 39.75], ['Piano', 36, 39.5, 39.75], ['Piano', 42, 39.75, 40.0],
['Piano', 36, 40.0, 40.25], ['Piano', 42, 40.25, 40.5], ['Piano', 36, 40.5, 40.75], ['Piano', 39, 40.5, 40.75], ['Piano', 42, 40.75, 41.0], 
['Piano', 36, 41.0, 41.25], ['Piano', 42, 41.25, 41.5], ['Piano', 36, 41.5, 41.75], ['Piano', 39, 41.5, 41.75], ['Piano', 42, 41.75, 42.0], 
['Piano', 36, 42.0, 42.25], ['Piano', 42, 42.25, 42.5], ['Piano', 36, 42.5, 42.75], ['Piano', 39, 42.5, 42.75], ['Piano', 42, 42.75, 43.0], 
['Piano', 36, 43.0, 43.25], ['Piano', 42, 43.25, 43.5], ['Piano', 36, 43.5, 43.75], ['Piano', 39, 43.5, 43.75], ['Piano', 42, 43.75, 44.0], 
['Piano', 36, 44.0, 44.25], ['Piano', 42, 44.25, 44.5], ['Piano', 36, 44.5, 44.75], ['Piano', 39, 44.5, 44.75], ['Piano', 42, 44.75, 45.0],
 ['Piano', 36, 45.0, 45.25], ['Piano', 42, 45.25, 45.5], ['Piano', 36, 45.5, 45.75], ['Piano', 39, 45.5, 45.75], ['Piano', 42, 45.75, 46.0], 
 ['Piano', 36, 46.0, 46.125], ['Piano', 42, 46.0, 46.125], ['Piano', 42, 46.25, 46.375], ['Piano', 42, 46.5, 46.625], ['Piano', 39, 46.5, 46.625],
  ['Piano', 42, 47.0, 47.125], ['Piano', 36, 47.0, 47.125], ['Piano', 42, 47.25, 47.375], ['Piano', 36, 47.25, 47.375], ['Piano', 42, 47.5, 47.625],
   ['Piano', 39, 47.5, 47.625], ['Piano', 49, 48.0, 48.25], ['Piano', 36, 48.0, 48.25]]

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 29:
        return Color(pos * 3, 255 - pos * 3, 0,0)
    elif pos < 58:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3,0)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3,0)

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

def blank(strip, wait_ms=10):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i,(0,0,0,0))
        strip.show()
        time.sleep(wait_ms / 1000.0) 

# Main program logic follows:
if __name__ == '__main__':

    # Create PixelStrip object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    colorWipe(strip, Color(100, 0, 0), 0)  # Green wipe
    time.sleep(0.5)
    colorWipe(strip, Color(0, 0, 0), 0)
    time.sleep(0.5)
    colorWipe(strip, Color(100,0, 0), 0)  # Green wipe
    time.sleep(0.5)
    colorWipe(strip, Color(0, 0, 0), 0)
    time.sleep(0.5)
    colorWipe(strip, Color(100, 0, 0), 0)  # Green wipe
    time.sleep(0.5)
    colorWipe(strip, Color(0, 0, 0), 0)
    

    start=time.time()
    print('Press Ctrl-C to quit.')
    i=0
    #print(big_list)
    
    
    j=2
    previous_note=["s",0,0,0]
    while True:
        for note in best_list:

            instrument=note[0]
            pitch=note[1]
            n_start=note[2]
            n_end=note[3]
            #print("instrument",instrument)
            if (n_start-previous_note[3])>0.0:
                time.sleep(n_start-previous_note[3])
                print("resting")
            else:

                if instrument=="Piano":
                    for p in range(0,30):
                        strip.setPixelColor(p,Color(pitch,pitch,0,0))

                    strip.show()
                    print("playing note",pitch)
                    time.sleep(n_end-n_start)
                    for p in range(0,30):
                        strip.setPixelColor(p,Color(0,0,0,0))
                    strip.show()
                
            previous_note=note

        i=i+1
        # #for j in range(len(big_list)+1):
        # print("this is j ",j)
        # #print(big_list[j])
        # note_list=big_list[j][2:]
        # print("current time",round(time.time()-start,2))
        # nstart=float(note_list[i][1])
        # print("start of the note",nstart)
        # nstop=float(note_list[i][2])
        # npitch=int(note_list[i][0])
        # if ( round((time.time()-start),2) - nstart)<=0.005:
        #     print("NoteMatched!")
        #     print(npitch)
        #     print(wheel(npitch))
        #     p=j
        #     for p in range(30,30+30):

        #         strip.setPixelColor(p, wheel(npitch))
        #     strip.show()
        #     time.sleep(nstop-nstart)
        #     for p in range(30,30+30):
        #         strip.setPixelColor(p,Color(0,0,0,0))
        #     strip.show()
            
        
        
        
