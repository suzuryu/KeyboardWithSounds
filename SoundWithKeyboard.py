import sys
import winsound

from pyhooked import Hook, KeyboardEvent, MouseEvent
from synthesizer import Player, Synthesizer, Waveform

from scalesFreq import scales_freq

# a 65
# z 90
# space 32
# enter 13
# back 8

def play_synthe(code):
    synth = Synthesizer(
        osc1_waveform = Waveform.square,
        osc1_volume   = 0.2,
    )
    
    freq = scales_freq[code - 65]
    player.play_wave(synth.generate_constant_wave(frequency=freq, length=0.1))

def handle_events(args):
    if isinstance(args, KeyboardEvent):
        code = args.key_code

        if args.event_type == 'key down':
            print(code, end='\n')

            if  65 <= code <= 90:
                play_synthe(code)

player = Player()
player.open_stream()

hk = Hook()  # make a new instance of PyHooked
hk.handler = handle_events  # add a new shortcut ctrl+a, or triggered on mouseover of (300,400)
hk.hook()  # hook into the events, and listen to the presses
