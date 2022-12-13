import keyboard
from modules.core.vars import char_man as cm
from pynput.keyboard import Key, Listener

def user_input(

):
    #key = keyboard.is_pressed()
    return #str(cm.lower_all_letter(key))

def left(
    inpt,
):
    while True:
        if keyboard.is_pressed(inpt):
            print(f"You pressed {inpt}.")
            break

    return

#def on_press(key):
#    print('{0} pressed'.format(
#        key))

#def on_release(key):
#    print('{0} release'.format(
#        key))
#    if key == Key.esc:
#        # Stop listener
#        return False

# Collect events until released
#with Listener(
#        on_press=on_press,
#        on_release=on_release) as listener:
#    listener.join()


