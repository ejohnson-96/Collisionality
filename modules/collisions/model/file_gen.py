
from modules.core.loadsave import file_dir as fd, file_import as fi
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

def loaded_files(
        encounter,
        load_dir
):
    enc_dir = load_dir + slash + "E" + str(encounter)
    files = []
    for file in fd.file_list(enc_dir):
        if file[0] != ".":
            files.append(file)
    return files

def error_files_loaded(
        encounter,
        load_dir,

):
    enc_dir = load_dir + slash + "E" + str(encounter)
    if len(fd.file_list(enc_dir)) == 5:
        return True
    else:
        return False


def data_import(
        encounter,
        root
):
    nm.valid_num(encounter)
    load_dir = load_path(root)
    load_files = loaded_files(encounter, load_dir)

    data = {}
    print(load_files)
    for file in load_files:
        data[file] = (fi.file_import(file, load_dir + slash + "E" + str(encounter)))

    if error_files_loaded(encounter, load_dir):
        error_data = True
    else:
        error_data = False

    print('\nData import successful.\n')

    return data, error_data


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
    position_data = []
    for file in position_files:
        position_data.append(fi.file_import(file, position_dir))

    return position_data  #position_dir, position_files


