import keyboard
def detect(ls):
    for x in ls:
        if keyboard.is_pressed(x):
            return True
    return False

def det(x):
    if keyboard.is_pressed(x):
        return True
    else:
        return False