import sys
import pickle
import numpy as np
import pandas as pd

from modules.core.vars.bool_man import valid_bool
from modules.core.vars import string_man as sm, char_man as cm
from modules.core.loadsave import file_dir as fd, file_types as ft

slash = fd.slash()
valid_types = ft.types


def validate(
        filename,
        path=fd.dir_path(),
        warning=True,
):
    filename = sm.valid_string(filename)
    path = sm.slash_check(sm.valid_string(path))
    warning = valid_bool(warning)

    if fd.dir_exists(path):
        if fd.file_exists(path + filename):
            if warning:
                h = 0
                while h < 1:
                    usr_inp = input("Do you wish to override the current file? (y/n)")
                    if cm.lower_all_letter(sm.valid_string(usr_inp)) == 'y':
                        h = 1
                    elif cm.lower_all_letter(sm.valid_string(usr_inp)) == 'n':
                        sys.exit()
            return path + filename
        elif not fd.file_exists(filename):
            return path + filename
    else:
        raise ValueError(
            f"Error: Location {path} does not exist, please try again."
        )


def save_csv(
        data,
        filename,
        path=fd.dir_path(),
        warning=True,
):
    loc = validate(filename, path, warning)
    if not isinstance(data, pd.DataFrame):
        raise TypeError(
            "Error: Incorrect data type for save, dataframe is "
            f"instead got type of type{data}."
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
        return data.to_excel(sm.slash_check(path), sheet_name=filename, index=False)


save = {}
for ftype in valid_types.valid_file_types:
    save[ftype] = globals()[str('save_' + cm.remove_begin(ftype))]


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
