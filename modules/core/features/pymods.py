import inspect
from types import ModuleType


def valid_mod(
        module,
        var=False
):
    if not isinstance(module, ModuleType):
        raise TypeError(
            f"Argument {module} is of incorrect type, type of "
            f"{ModuleType} is required. Instead got type of {type(module)}."
        )

    if var:
        return module
    else:
        return True


def list_all(
        module,
):
    if valid_mod(module):
        return dir(module)


def list_dunder(
        module,
):
    module = list_all(module)
    res = []
    for value in module:
        if value[:2] == '__' and value[len(value) - 2:] == '__':
            res.append(value)
    return res


def list_funct(
        module,
):
    module = inspect.getmembers(valid_mod(module), inspect.isfunction)
    res = []

    for values in module:
        res.append(values[0])

    return res
