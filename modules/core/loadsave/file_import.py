import h5py
import pickle
import pandas as pd

from modules.core.loadsave import file_dir as fd, file_types as ft
from modules.core.vars import string_man as sm, char_man as cm

slash = fd.slash()
valid_types = ft.types


def validate(
        filename,
        path=fd.dir_path(),
):
    loc = sm.slash_check(sm.valid_string(path)) + sm.valid_string(filename)
    if fd.file_exists(loc):
        return loc
    else:
        raise ValueError(
            f"Error: Location {loc} does not exist, please try again."
        )


def load_csv(
        filename,
        path=fd.dir_path(),
):
    loc = validate(filename, path)
    if ft.type_check(loc, '.csv'):
        return pd.read_csv(loc)


def load_txt(
        filename,
        path=fd.dir_path(),
):
    loc = validate(filename, path)
    if ft.type_check(loc, '.txt'):
        return open(loc, 'r').read()


def load_pkl(
        filename,
        path=fd.dir_path(),
):
    loc = validate(filename, path)
    if ft.type_check(loc, '.pkl'):
        with open(loc, 'rb') as file:
            return pickle.load(file)


def load_xlsx(
        filename,
        path=fd.dir_path()
):
    loc = validate(filename, path)
    if ft.type_check(loc, '.xlsx'):
        return pd.ExcelFile(loc)


def load_hdf5(
        filename,
        path=fd.dir_path(),
):
    loc = validate(filename, path)
    if ft.type_check(loc, '.hdf5'):
        return h5py.File(loc, 'r')


load = {}
for ftype in valid_types.valid_file_types:
    load[ftype] = globals()[str('load_' + cm.remove_begin(ftype))]


def file_import(
        filename,
        path=fd.dir_path(),
):
    loc = validate(filename, path)

    if fd.file_ext(loc) in valid_types.valid_file_types:
        return load[fd.file_ext(loc)](filename, path)
    else:
        raise ValueError(
            f"Error: The following file type {fd.file_ext(loc)}, is "
            "not supported, please try the following extensions, "
            f"{valid_types.valid_file_types}"
        )


