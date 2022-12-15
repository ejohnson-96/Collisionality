import h5py
import pickle
import pandas as pd

from modules.core.loadsave import file_dir as fd, file_types as ft
from modules.core.vars.char_man import del_beg
from modules.core.vars.str_man import valid_str, slash_dir


def load_csv(
        filename,
        path=fd.dir_path(),
):
    valid_str(filename, path)
    loc = fd.file_exists(slash_dir(path) + filename, var=True)
    if ft.valid_type(loc, '.csv'):
        return pd.read_csv(loc)


def load_txt(
        filename,
        path=fd.dir_path(),
):
    valid_str(filename, path)
    loc = fd.file_exists(slash_dir(path) + filename, var=True)
    if ft.valid_type(loc, '.txt'):
        return open(loc, 'r').read()


def load_pkl(
        filename,
        path=fd.dir_path(),
):
    valid_str(filename, path)
    loc = fd.file_exists(slash_dir(path) + filename, var=True)
    if ft.valid_type(loc, '.pkl'):
        with open(loc, 'rb') as file:
            return pickle.load(file)


def load_xlsx(
        filename,
        path=fd.dir_path()
):
    valid_str(filename, path)
    loc = fd.file_exists(slash_dir(path) + filename, var=True)
    if ft.valid_type(loc, '.xlsx'):
        return pd.ExcelFile(loc)


def load_hdf5(
        filename,
        path=fd.dir_path(),
):
    valid_str(filename, path)
    loc = fd.file_exists(slash_dir(path) + filename, var=True)
    if ft.valid_type(loc, '.hdf5'):
        return h5py.File(loc, 'r')


def file_import(
        filename,
        path=fd.dir_path(),
):
    load = {}

    for ftype in ft.types.valid_file_types:
        load[ftype] = globals()[str('load_' + del_beg(ftype))]

    valid_str(filename, path)
    loc = fd.file_exists(slash_dir(path) + filename, var=True)

    if fd.file_exists(loc):
            if fd.file_ext(loc) in ft.types.valid_file_types:
                return load[fd.file_ext(loc)](filename, path)
            else:
                raise ValueError(
                    f"Argument {filename} does not have a supported extension,"
                    f" valid extensions are {ft.types}. Extension provided "
                    f"was {fd.file_ext(loc)}, at location {path}. Please try "
                    "again."
                )
