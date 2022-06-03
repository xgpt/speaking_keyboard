import winsound
from pynput import keyboard
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
        
        


# def on_press(key):
#     if key == keyboard.Key.esc:
#         return False  # stop listener
#     try:
#         k = key.char  # single-char keys
#     except:
#         k = key.name  # other keys
#     if k in ['1', '2', 'left', 'right']:  # keys of interest
#         # self.keys.append(k)  # store it in global-like variable
#         print('Key pressed: ' + k)
#         return False  # stop listener; remove this if want more keys
# 
# listener = keyboard.Listener(on_press=on_press)
# listener.start()  # start to listen on a separate thread# listener.join()  # remove if main thread is polling self.keys

def on_press(key):
#    if key == keyboard.Key.esc:
#        exit()
    try:
        k = key.char
    except:
        k = key.name
    print(str(k))
    if k in ['space']:
        winsound.PlaySound(resource_path('space.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['tab']:
        winsound.PlaySound(resource_path('tab.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['caps_lock']:
        winsound.PlaySound(resource_path('capslock.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['enter']:
        winsound.PlaySound(resource_path('enter.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['0']:
        winsound.PlaySound(resource_path('0.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['1']:
        winsound.PlaySound(resource_path('1.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['2']:
        winsound.PlaySound(resource_path('2.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['3']:
        winsound.PlaySound(resource_path('3.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['4']:
        winsound.PlaySound(resource_path('4.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['5']:
        winsound.PlaySound(resource_path('5.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['6']:
        winsound.PlaySound(resource_path('6.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['7']:
        winsound.PlaySound(resource_path('7.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['8']:
        winsound.PlaySound(resource_path('8.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['9']:
        winsound.PlaySound(resource_path('9.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['a']:
        winsound.PlaySound(resource_path('a.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['b']:          
        winsound.PlaySound(resource_path('b.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['c']:          
        winsound.PlaySound(resource_path('c.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['d']:          
        winsound.PlaySound(resource_path('d.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['e']:          
        winsound.PlaySound(resource_path('e.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['f']:          
        winsound.PlaySound(resource_path('f.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['g']:          
        winsound.PlaySound(resource_path('g.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['h']:          
        winsound.PlaySound(resource_path('h.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['i']:          
        winsound.PlaySound(resource_path('i.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['j']:          
        winsound.PlaySound(resource_path('j.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['k']:          
        winsound.PlaySound(resource_path('k.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['l']:          
        winsound.PlaySound(resource_path('l.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['m']:          
        winsound.PlaySound(resource_path('m.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['n']:          
        winsound.PlaySound(resource_path('n.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['o']:          
        winsound.PlaySound(resource_path('o.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['p']:          
        winsound.PlaySound(resource_path('p.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['q']:          
        winsound.PlaySound(resource_path('q.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['r']:          
        winsound.PlaySound(resource_path('r.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['s']:          
        winsound.PlaySound(resource_path('s.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['t']:          
        winsound.PlaySound(resource_path('t.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['u']:          
        winsound.PlaySound(resource_path('u.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['v']:          
        winsound.PlaySound(resource_path('v.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['w']:          
        winsound.PlaySound(resource_path('w.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['x']:          
        winsound.PlaySound(resource_path('x.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['y']:          
        winsound.PlaySound(resource_path('y.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)
    if k in ['z']:          
        winsound.PlaySound(resource_path('z.wav'), winsound.SND_ASYNC|winsound.SND_FILENAME)

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
