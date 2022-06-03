import winsound
import keyboard
import pynput

while True:
    keyboard.add_hotkey("a", lambda: winsound.PlaySound('B.wav', winsound.SND_ASYNC))