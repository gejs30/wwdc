https://learn.adafruit.com/circuitpython-essentials/circuitpython-audio-out

"""CircuitPython Essentials Audio Out WAV example"""
import time
import board
import digitalio
from audiocore import WaveFile

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!

button = digitalio.DigitalInOut(board.A1)
button.switch_to_input(pull=digitalio.Pull.UP)

wave_file = open("softchime.wav", "rb")
wave = WaveFile(wave_file)
audio = AudioOut(board.A0)

while True:

    audio.play(wave)

    # This allows you to do other things while the audio plays!
    t = time.monotonic()
    while time.monotonic() - t < 60:
        pass

import time

from adafruit_circuitplayground.express import cpx

while True:
    cpx.pixels[0] = (abs(cpx.pixels[0][0] - 255), 0, 0)
    time.sleep(0.5)
    audio.pause()
    print("Waiting for button press to continue!")
    while button.value:
        pass
    audio.resume()
    while audio.playing:
        pass
    print("Done!")
