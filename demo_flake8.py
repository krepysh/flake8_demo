# flake8: noqa

def jump():
    pass
def move():
    pass


def at_goal():
    pass


def front_is_clear():
    pass

def get_config():
    pass

def hurdle():
    while (at_goal() == False):
        while (front_is_clear() ==  True):
            move()
        jump()
