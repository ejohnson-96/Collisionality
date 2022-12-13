import types
from modules.core.vars.num_man import valid_num
import numpy as np


def euler_method(
        funct,
        step_size,
        initial,
        return_arr=False,

):
    if not isinstance(funct, types.FunctionType):
        raise TypeError(
            f"Error: Argument {funct} is not a function type, "
            f"instead got type of {type(funct)}. Please try again,"
            " argument must start with lambda x, y: ."
        )

    step_size = valid_num(step_size)
    x = np.arange(0, 1 + step_size, step_size)
    initial = valid_num(initial)

    y = np.zeros(len(x))
    y[0] = initial

    for i in range(0, len(x) - 1):
        y[i + 1] = y[i] + step_size * funct(x[i], y[i])

    if return_arr:
        return y
    else:
        return y[len(x) - 1]