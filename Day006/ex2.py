# Reeborg's Hurdle 1 challenge

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


for _ in range(6):
    jump()

# That code only works at:
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json#
