import numpy as np


def valid_list(
        inpt,
):
    if not isinstance(inpt, list):
        raise TypeError(
            f"Error: Argument {inpt}, is not of type list, "
            f"instead got type of {type(inpt)}."
        )
    else:
        return inpt


def val_entry_num(
        inpt,
        integer=False,
):
    inpt = valid_list(inpt)

    if integer:
        var_type = int
    else:
        var_type = (int, float)

    for i in range(len(inpt)):
        if not isinstance(inpt[i], var_type):
            raise TypeError(
                f"Error: Argument {inpt[i]}, is not of type "
                f"{var_type}, instead got type {type(inpt[i])}."
            )
    return inpt


def val_entry_str(
        inpt,
):
    inpt = valid_list(inpt)

    for i in range(len(inpt)):
        if not isinstance(inpt[i], str):
            raise TypeError(
                f"Error: Argument {inpt[i]}, is not a str type, "
                f"instead got type of {type(inpt[i])}."
            )
    return inpt


def remove_all_occur(
        entry,
        item,
):
    entry = valid_list(entry)
    return [i for i in entry if i != item]


def convert_arr(
        entry,
):
    entry = valid_list(entry)
    return np.array(entry)


def sort_asc(
        entry,
):
    entry = valid_list(entry)
    return entry.sort()


def sort_dsc(
        entry,
):
    entry = valid_list(entry)
    return entry.sort(reverse=True)


def equal_len(
        entry_a,
        entry_b,
):
    entry_a = valid_list(entry_a)
    entry_b = valid_list(entry_b)

    if len(entry_a) != len(entry_b):
        return False
    else:
        return True
