import numpy as np


def valid_arr(
        inpt,
):
    if not isinstance(inpt, np.ndarray):
        raise TypeError(
            f"Error: Argument {inpt}, is not an array, "
            f"instead got type of {type(inpt)}"
        )
    else:
        return inpt


def single_arr(
        arr,
):
    arr = valid_arr(arr)
    if not arr.ndim == 1:
        raise ValueError(
            "Error: Argument is not a single length, "
            f" instead got dimension {arr.ndim}."
        )
    else:
        return arr


def arr_dim(
        arr,
):
    arr = valid_arr(arr)
    return arr.ndim


def valid_ent_num(
        arr,
):
    arr = single_arr(arr)

    for i in range(len(arr)):
        if not isinstance(arr[i], (float, int, np.integer, np.float_)):
            raise TypeError(
                f"Error: Entry index {i}; {arr[i]}, is not of type "
                f"int or float, instead got type of {type(arr[i])}."
            )
    else:
        return arr


def valid_ent_str(
        arr,
):
    arr = single_arr(arr)

    for i in range(len(arr)):
        if not isinstance(arr[i], str):
            raise TypeError(
                f"Error: Entry index {i}; {arr[i]}, is not of type "
                f"string, instead got type of {type(arr[i])}."
            )
        else:
            return arr


def valid_ent_bool(
        arr,
):
    arr = single_arr(arr)

    for i in range(len(arr)):
        if not isinstance(arr[i], (bool, np.bool_)):
            raise TypeError(
                f"Error: Entry index {i}; {arr[i]}, is not a boolean "
                f"type, instead got type of {type(arr[i])}."
            )
        else:
            return arr


def equal_len(
        arr_a,
        arr_b,
        show_lengths=False,
):
    arr_a = single_arr(arr_a)
    arr_b = single_arr(arr_b)

    if len(arr_a) != len(arr_b):
        if show_lengths:
            print(f'Length - array A: {len(arr_a)}, '
                  f'array B: {len(arr_b)}.')
        return False
    else:
        if show_lengths:
            print(f'Length - {len(arr_a)}')
        return True


def print_out(
        arr,
        index=False,
):
    arr = single_arr(arr)

    for i in range(len(arr)):
        if index:
            arg_ = ', ' + str(i) + '.'
        else:
            arg_ = ''
        print(arr[i], arg_)
    return


def sort_asc(
        arr,
):
    arr = single_arr(arr)
    return np.sort(arr)


def sort_dsc(
        arr,
):
    arr = single_arr(arr)
    return np.sort(arr)[::-1]


def first_entry(
        arr,
):
    arr = single_arr(arr)
    return arr[0]


def last_entry(
        arr,
):
    arr = single_arr(arr)
    return arr[-1]


def arr_len(
        arr,
):
    arr = single_arr(arr)
    return len(arr)


def remove_index(
        arr,
        index=0,
):
    arr = single_arr(arr)
    return np.delete(arr, index)


def remove_last_entry(
        arr,
):
    return remove_index(arr, -1)


def remove_first_entry(
        arr,
):
    return remove_index(arr, 0)


def is_nan(
        arr,
):
    arr = single_arr(arr)
    return arr[np.logical_not(np.isnan(arr))]
