

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
    while not at_goal():
        while front_is_clear():
            move()
        jump()
