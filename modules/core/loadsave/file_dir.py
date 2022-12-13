import os
import pathlib
import warnings

from modules.core.vars.bool_man import valid_bool
from modules.core.vars import string_man as sm
from modules.core.system import config as sys_con


def slash(

):
    if sys_con.windows_os():
        return '\\'
    else:
        return '/'


sys_slash = slash()


def dir_parent(

):
    return str(pathlib.Path(os.getcwd()).parent)


def dir_path(

):
    return str(pathlib.Path(os.getcwd()))


path_dir = dir_path()


def dir_make(
        name,
        loc=path_dir,
        warning=True,
):
    name = sm.valid_string(name)
    loc = sm.valid_string(loc)
    warning = valid_bool(warning)

    if dir_exists(loc, warning=True):
        path = sm.slash_check(loc) + name
        if dir_exists(path, warning):
            return False
        else:
            os.mkdir(path)
            return True


def dir_exists(
        loc,
        warning=False,
):
    loc = sm.valid_string(loc)
    warning = valid_bool(warning)

    if os.path.exists(loc):
        return True
    else:
        if warning:
            warnings.warn(
                f"Warning: Directory {loc}, doesn't exist."
            )
        return False


def dir_name(
        loc=None,
        warning=True,
):
    warning = valid_bool(warning)

    if isinstance(loc, type(None)):
        return os.path.basename(os.getcwd())
    else:
        loc = sm.valid_string(loc)
        if dir_exists(loc, warning):
            return os.path.basename(loc)


def dir_drop(
        loc,
):
    loc = sm.valid_string(loc)
    return os.path.split(loc)[0]


def dir_list(
        loc=path_dir,
):
    return os.listdir(sm.slash_check(sm.valid_string(loc)))


def dir_num(
        loc=path_dir,
):
    return len(dir_list(sm.valid_string(loc)))


def file_exists(
        loc,
        warning=False,
):
    loc = sm.valid_string(loc)
    warning = valid_bool(warning)

    if os.path.isfile(loc):
        return True
    else:
        if warning:
            warnings.warn(
                f"Warning: The file {loc}, does not exits."
            )
        return False


def file_list(
        loc=path_dir,
):
    return next(os.walk(sm.slash_check(sm.valid_string(loc))))[2]


def file_num(
        loc=path_dir,
):
    return len(file_list(sm.valid_string(loc)))


def folder_list(
        loc=path_dir,
):
    return next(os.walk(sm.slash_check(sm.valid_string(loc))))[1]


def folder_num(
        loc=path_dir,
):
    return len(folder_list(sm.valid_string(loc)))


def file_ext(
        loc=path_dir,
):
    return os.path.splitext(sm.valid_string(loc))[-1].lower()


def all_file_type(
        file_type,
        loc=path_dir,
):
    file_type = sm.valid_string(file_type)
    loc = sm.valid_string(sm.slash_check(loc))
    res = []
    for root, dirs, files in os.walk(loc):
        for file in files:
            if file.endswith(file_type):
                res.append(os.path.join(root, file))
    return res


def load_bar(
        counter,
        end_point,
        width=50
):

    percent = (counter/end_point)*100
    end_num = ((end_point - 1)/end_point)*100

    left = width * percent // 100
    right = width - left

    tags = "#" * int(left)
    spaces = " " * int(right)
    percents = f"{percent:.2f}%"

    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)

    return

