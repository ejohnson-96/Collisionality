import random

from modules.core.vars.string_man import valid_string
from modules.core.vars.num_man import valid_num


def hex_to_rgb(
        hex,
):
    hex = valid_string(hex)

    if '#' not in hex:
        raise ValueError(
            'Error: String must begin with #.'
        )
    else:
        h = hex.lstrip('#')

    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(
        r,
        g,
        b,
):
    for arg_ in (r,g,b):
        valid_num(arg_)
    rgb = (r,g,b)

    return '#%02x%02x%02x' % rgb


def rand_rgb(

):
    r = random.random()
    g = random.random()
    b = random.random()

    return r, g, b