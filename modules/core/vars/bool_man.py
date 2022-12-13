def valid_bool(
        *args,
        var=False,
):
    for arg in args:
        if not isinstance(arg, bool):
            raise TypeError(
                f"Argument {arg} is of incorrect type, bool type is "
                f"required. Instead got type of {type(arg)}."
            )
    if var:
        return args
    else:
        return True


def and_(
        a,
        b,
):
    valid_bool(a, b)
    if a == 1 and b == 1:
        return True
    else:
        return False


def nand_(
        a,
        b,
):
    valid_bool(a, b)
    if a == 1 and b == 1:
        return False
    else:
        return True


def or_(
        a,
        b,
):
    valid_bool(a, b)
    if a == 1 or b == 1:
        return True
    else:
        return False


def xor_(
        a,
        b,
):
    valid_bool(a, b)
    if a != b:
        return True
    else:
        return False


def not_(
        a,
):
    valid_bool(a)
    return not a


def nor_(
        a,
        b,
):
    valid_bool(a, b)

    if (a == 0) and (b == 0):
        return True
    elif (a == 0) and (b == 1):
        return False
    elif (a == 1) and (b == 0):
        return False
    elif (a == 1) and (b == 1):
        return True
    else:
        raise ValueError(
            f"Logic cannot be determined for arguments passed: "
            f"{a} and {b}, of types {type(a)} and {type(b)} "
            "respectively."
        )


def xnor_(
        a,
        b,
):
    valid_bool(a, b)
    if a == b:
        return True
    else:
        return False
