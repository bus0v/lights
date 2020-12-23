# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import pretty_midi
from rpi_ws281x import Color, PixelStrip, ws


midi_data = pretty_midi.PrettyMIDI('C:\\Users\\PC\\Documents\\Compsci pursuits!\\music_midi\\90s.mid')
print("duration:",midi_data.get_end_time())
print(f'{"note":>10} {"start":>10} {"end":>10}')
big_list=[]
n=0
for instrument in midi_data.instruments:
    print("instrument:", instrument.program)

    big_list.append(["instrument:", instrument.program])
    for note in instrument.notes:
        big_list[n].append([note.pitch,note.start,note.end])
        print(f'{note.pitch:10} {note.start:10} {note.end:10}')

    n=n+1
    print(big_list)

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


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


# Main program logic follows:
if __name__ == '__main__':
    # Create PixelStrip object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print('Press Ctrl-C to quit.')
    while True:
        # Color wipe animations.
        strip.setPixelColor(0, Color(255, 255, 255,0))
