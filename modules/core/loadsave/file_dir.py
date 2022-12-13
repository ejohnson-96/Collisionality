import os, pathlib
import sys

from modules.core.sys.config import windows_os
from modules.core.vars.bool_man import valid_bool
from modules.core.vars.char_man import low_all_let
from modules.core.vars.str_man import valid_str, slash_dir


def slash(

):
    if windows_os():
        return '\\'
    else:
        return '/'


def dir_parent(

):
    return str(pathlib.Path(os.getcwd()).parent)


def dir_path(

):
    return str(pathlib.Path(os.getcwd()))


def dir_exist(
        loc,
        error=True,
):
    valid_str(loc)
    valid_bool(error)
    if os.path.exists(loc):
        return True
    else:
        if error:
            raise ValueError(
                f"Directory location provided {loc}, does not exist."
            )
        else:
            return False


def dir_make(
        name,
        loc=dir_path(),
        error=True,
):
    valid_str(name, loc)

    if dir_exist(loc):
        path = slash_dir(loc) + name
        if dir_exist(path, error):
            raise ValueError(
                "The name argument provided for the new directory, "
                f"{name}, already exists. Please try again."
            )
        else:
            os.mkdir(path)
            return True


def dir_drop(
        loc,
        name=False,
):
    if valid_str(loc):
        if name:
            return os.path.split(loc)[1]
        else:
            return os.path.split(loc)[0]


def dir_list(
        loc=dir_path(),
):
    if dir_exist(loc):
        return os.listdir(slash_dir(loc))


def dir_num(
        loc=dir_path(),
):
    if dir_exist(loc):
        return len(dir_list(slash_dir(loc)))


def file_exists(
        loc,
        error=True,
        var=False,

):
    valid_str(loc)
    if os.path.isfile(loc):
        if var:
            return loc
        else:
            return True
    else:
        if error:
            raise ValueError(
                f"File location provided {loc}, does not exist."
            )
        else:
            return False


def file_list(
        loc=dir_path(),
):
    if dir_exist(loc):
        return next(os.walk(slash_dir(loc)))[2]


def file_num(
        loc=dir_path(),
):
    if dir_exist(loc):
        return len(file_list(slash_dir(loc)))


def file_ext(
        loc=dir_path(),
):
    valid_str(loc)
    if file_exists(loc):
        return os.path.splitext(loc)[-1].lower()


def load_bar(
        counter,
        end_point,
        width=50
):
    percent = (counter / end_point) * 100

    left = width * percent // 100
    right = width - left

    tags = "#" * int(left)
    spaces = " " * int(right)
    percents = f"{percent:.2f}%"

    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)

    return


def warn(
        loc,
):
    valid_str(loc)
    h = 0
    while h < 1:
        usr_inp = input(f"Location: {loc} \nDo you wish to delete the current "
                        f"item? (y/n) \n")
        if valid_str(usr_inp):
            if low_all_let(usr_inp) == 'y':
                return
            elif low_all_let(usr_inp) == 'n':
                sys.exit()
    return


