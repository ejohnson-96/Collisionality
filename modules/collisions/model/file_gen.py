import pickle
from modules.core.loadsave import file_dir as fd, file_import as fi
from modules.core.vars import num_man as nm, str_man as sm
from modules.collisions.model import scalar_gen as sc_gen
from modules.collisions.features import latlong as ll

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

    for file in load_files:
        data[file] = (fi.file_import(file, load_dir + slash + "E" + str(encounter)))

    if error_files_loaded(encounter, load_dir):
        error_data = True
    else:
        error_data = False

    print(f'\nE{encounter} data import successful.')

    return data, error_data


def position_import(
        encounter,
        root
):
    nm.valid_num(encounter)

    position_files = loaded_position(encounter, root)
    position_data = {}
    for file in position_files:
        position_data[file] = (fi.file_import(file, position_dir(encounter, root)))

    return position_data


def position_dir(
        encounter,
        root
):
    return sm.slash_dir(load_path(root)) + "E" + str(encounter) + slash + "Position" + slash


def loaded_position(
        encounter,
        root,
):
    sm.valid_str(root)
    position_files = []

    loc = position_dir(int(encounter), root)

    if fd.dir_exist(loc):
        for file in fd.dir_list(loc):
            if file[0] != ".":
                position_files.append(file)
    return position_files

def save_file(
        loc,
        file
):
    sm.valid_str(loc)
    loc = sm.slash_dir(loc)
    with open(loc + '.pkl', 'wb') as handle:
        pickle.dump(file, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return

def scalar_gen(
        parker,
        position,
):
    parker = speed_gen(parker)
    position = ll.lat_long(position)
    psp_temps, wind_temps = temp_gen(parker, position)
    print('Generating velocity magnitudes and temperature file... \n')
    return parker, psp_temps, wind_temps

def speed_gen(
        parker,
):
    return sc_gen.scalar_velocity(parker)

def temp_gen(
        parker,
        position,
):
    return sc_gen.scalar_temps(parker, position)

def save_file(
        file,
        name,
        save_loc
):
    loc = sm.slash_dir(save_loc) + str(name)

    with open(loc + '.pkl', 'wb') as handle:
        pickle.dump(file, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return

name = ['parker', 'position', 'errors', 'psp_data', 'wind_data']
def load_files(
        save_loc,
):
    solar = fi.file_import(name[0] + '.pkl', sm.slash_dir(save_loc))
    space = fi.file_import(name[1] + '.pkl', sm.slash_dir(save_loc))
    error = fi.file_import(name[2] + '.pkl', sm.slash_dir(save_loc))
    psp = fi.file_import(name[3] + '.pkl', sm.slash_dir(save_loc))
    wind = fi.file_import(name[4] + '.pkl', sm.slash_dir(save_loc))

    return solar, space, error, psp, wind
