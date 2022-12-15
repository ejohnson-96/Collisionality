import sys
import pickle
import numpy as np
import pandas as pd

from modules.core.vars.bool_man import valid_bool
from modules.core.vars.char_man import low_all_let, del_beg
from modules.core.vars.str_man import valid_str, slash_dir
from modules.core.loadsave import file_dir as fd, file_types as ft

slash = fd.slash()
valid_types = ft.types


def validate(
        filename,
        path=fd.dir_path(),
        warning=True,
):
    valid_str(filename, path)
    valid_bool(warning)

    if fd.dir_exists(path):
        if fd.file_exists(slash_dir(path) + filename):
            if warning:
                h = 0
                while h < 1:
                    usr_inp = input(
                        f"Location: {path}\n File: {filename}\n"
                        f"Do you wish to override the current file? (y/n)"
                    )
                    if low_all_let(valid_str(usr_inp)) == 'y':
                        h = 1
                    elif low_all_let(valid_str(usr_inp)) == 'n':
                        sys.exit()
            return slash_dir(path) + filename


def save_csv(
        data,
        filename,
        path=fd.dir_path(),
        warning=True,
):
    loc = validate(filename, path, warning)
    if not isinstance(data, pd.DataFrame):
        raise TypeError(
            f"Argument data is of incorrect type, type of {type(data)}"
            " was provided. Please try again."
        )
    else:
        return data.to_csv(loc)


def save_pkl(
        data,
        filename,
        path=fd.dir_path(),
        warning=True,
):
    loc = validate(filename, path, warning)
    if ft.type_check(loc, '.pkl'):
        with open(loc, 'wb') as handle:
            return pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def save_txt(
        data,
        filename,
        path=fd.dir_path(),
        warning=True,
):
    loc = validate(filename, path, warning)
    if ft.type_check(loc, '.txt'):
        return np.savetxt(loc, data)


def save_xlsx(
        data,
        filename,
        path=fd.dir_path(),
        warning=True,
):
    validate(filename, path, warning)
    if not isinstance(data, pd.DataFrame):
        raise TypeError(
            "Error: Incorrect data type for save, dataframe is "
            f"instead got type of type{data}."
        )
    else:
        return data.to_excel(slash_dir(path), sheet_name=filename, index=False)


save = {}
for ftype in valid_types.valid_file_types:
    save[ftype] = globals()[str('save_' + del_beg(ftype))]


def file_export(
        data,
        filename,
        path=fd.dir_path(),
        warning=True,
):
    warning = valid_bool(warning)
    loc = validate(filename, path, warning)

    if fd.file_ext(loc) in valid_types.valid_file_types:
        save[fd.file_ext(loc)](data, filename, path, False)
        return 'Save Successful.'
    else:
        raise ValueError(
            f"Error: The following file type {fd.file_ext(loc)}, is "
            "not supported, please try the following extensions, "
            f"{valid_types.valid_file_types}"
        )
