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
    if not at_goal():
        if front_is_clear():
            move()
        jump()
