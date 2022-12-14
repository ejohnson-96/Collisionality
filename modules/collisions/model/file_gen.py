import pickle

from modules.core.loadsave import file_dir as fd
from modules.core.vars import num_man as nm, str_man as sm

slash = fd.slash()


def load_path(
        root
):
    sm.valid_str(root)
    return sm.slash_dir(root) + "data" + slash + "load"


def save_path(
        encounter,
        root
):
    sm.valid_str(root)
    nm.valid_num(encounter)
    encounter = "E" + str(encounter)
    return sm.slash_dir(root) + "data" + slash + "save" + slash + encounter + slash


def error_files_loaded(
        encounter,
        load_dir,

):
    enc_dir = load_dir + slash + "E" + str(encounter)
    if fd.file_list(enc_dir) == 5:
        return True
    else:
        return False


def data_import(
        encounter,
        root
):
    nm.valid_num(encounter)
    load_dir = load_path(root)

    # mm_data = rw.encounter_import(enc)
    # sc_data = rw.sc_import(enc)

    if error_files_loaded(encounter, load_dir):
        error_data = 1
    else:
        error_data = None

    print('\nData import successful.\n')

    return


def position_import(
        encounter,
        root
):
    nm.valid_num(encounter)

    position_dir = sm.slash_dir(load_path(root)) + "E" + str(encounter) + slash + "Position" + slash
    position_files = []

    if position_dir:
        for file in fd.dir_list(position_dir):
            if file[0] != ".":
                position_files.append(file)

    for file in position_files:
        print(file)

    return position_dir, position_files


