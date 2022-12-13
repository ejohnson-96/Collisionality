import numpy as np
from modules.core.vars.bool_man import valid_bool


def valid_var(
        integer,
        floats,

):
    valid_bool(integer, floats)
    if integer and floats:
        return int, float
    elif integer and not floats:
        return int
    elif not integer and floats:
        return float
    else:
        raise ValueError(
            "Arguments integer and floats cannot both be False, "
            "please try again."
        )


def valid_num(
        *args,
        integer=True,
        floats=True,
        var=False,
):
    valid_bool(integer, floats, var)

    valid_vars = valid_var(integer, floats)

    for arg in args:
        if not isinstance(arg, valid_vars):
            raise TypeError(
                f"Argument {arg} is of incorrect type, {valid_vars} "
                f"type is required. Instead got type of {type(arg)}."
            )
    if var:
        return args
    else:
        return True


def positive(
        arg,
        zero=True,
):
    valid_num(arg)
    valid_bool(zero)

    if zero:
        if not arg >= 0:
            raise ValueError(
                f"Argument {arg} must be greater than or equal "
                "to zero. Please try again."
            )

    else:
        if not arg > 0:
            raise ValueError(
                f"Argument {arg} must be greater than zero. "
                "Please try again."
            )

    return True


def negative(
        arg,
        zero=True,
):
    valid_num(arg)
    valid_bool(zero)

    return


def add(
        *args,
):
    for arg in args:
        valid_num(arg)
    return sum(args)


def sub(
        *args,
):
    for arg in args:
        valid_num(arg)
    return 2 * args[0] - sum(args[:len(args)])


def multi(
        *args,
):
    res = 1
    for arg in args:
        valid_num(arg)
        res = res * arg
    return res


def div(
        num,
        dom,
):
    valid_num(num, dom)

    if dom == 0:
        raise ValueError(
            f"Argument {dom} cannot be zero, you cannot divide by "
            "zero dummy."
        )
    else:
        return num / dom


def dim(
        arg,
        lower=0,
        upper=1,
):
    valid_num(arg, upper, lower)

    if arg > upper:
        raise ValueError(
            f"Argument {arg} is larger than the upper limit of {upper}."
        )
    elif arg < lower:
        raise ValueError(
            f"Argument {arg} is smaller than the lower limit of {lower}."
        )
    else:
        return arg


def valid_vec(
        vec,
        dimension=False,
):
    if isinstance(vec, (int, float)):
        if dimension:
            return 1
        else:
            return vec
    elif isinstance(vec, (list, np.ndarray)):
        if len(vec) != (1, 2, 3):
            if dimension:
                return len(vec)
            else:
                return vec
        else:
            raise ValueError(
                f"Argument {vec} is of incorrect dimension, up to 3 "
                "dimensions only are permitted. Instead got dimension "
                f"of {len(vec)}."
            )

    else:
        raise TypeError(
            f"Argument {vec} is of incorrect type, type of int, float,"
            f" list or array is required. Instead got type of {type(vec)}."
        )


def valid_ent_num(
        inpt,
        integer=True,
        floats=True,
):
    valid_vars = valid_var(integer, floats)
    if not isinstance(inpt, (list, np.ndarray)):
        raise TypeError(
            f"Argument {inpt} is of incorrect type, type of list or "
            f"an array is required. Instead got type of {type(inpt)}."
        )
    else:
        for i in range(len(inpt)):
            if not isinstance(inpt[i], valid_vars):
                raise TypeError(
                    f"Argument {inpt[i]} is of incorrect type, type of"
                    f" {valid_vars} is required. Instead index {i} got"
                    f" a type of {type(inpt[i])}."
                )
        return inpt


def byte(
        bytes,
):
    if isinstance(bytes, (int, float)):
        print('dfs')
    elif isinstance(bytes, str):
        print(f'sdfdsf')
    else:
        raise ValueError(
            f""
        )
