from modules.collisions.model import enc_gen as eg
from modules.collisions.model import file_gen as fg
from modules.core.vars import bool_man as bm, num_man as nm
from modules.core.loadsave import file_dir as fd

slash = fd.slash()
root = eg.root()
valid_encs = eg.enc_gen()
particles = eg.particle_gen()

encounter = eg.enc_selector()


def data_import(

):
    position_data = {}
    parker_data = {}

    if encounter == 0:
        for enc in valid_encs["X"]:
            parker_data["E" + str(enc)] = fg.data_import(int(enc), root)
            position_data["E" + str(enc)] = fg.position_import(int(enc), root)
    else:
        encount = "E" + str(encounter)
        parker_data[encount] = fg.data_import(encounter, root)
        position_data[encount] = fg.position_import(encounter, root)

    return parker_data, position_data


def data_validate(
        parker,
        position
):
    errors = {}
    for enc in parker.keys():
        errors[enc] = parker[enc][1]
        bm.valid_bool(errors[enc])
        for file in parker[enc][0].keys():
            for param in parker[enc][0][file].keys():
                for i in range(len(parker[enc][0][file][param])):
                    nm.valid_num(parker[enc][0][file][param][i])

    for enc in position.keys():
        for file in position[enc].keys():
            #print(file, position[enc][file])
            for param in position[enc][file].keys():
                if param == "datetime":
                    for i in range(len(position[enc][file][param])):
                        position[enc][file][param][i] = 1  # convertdate
                    # remane param
                    # delete previous datetime param
                for i in range(len(position[enc][file][param])):
                    nm.valid_num(position[enc][file][param][i])

    return parker, position, errors


x, y = data_import()
x, y, z = data_validate(x, y)

print(z, 'errors')

# x[valid_enc["EX"][enc]]   [ 0 (dict), 1 (error bool)] [file]

if encounter == 0:
    for i in range(len(valid_encs["EX"])):
        lf = fg.loaded_files(valid_encs["X"][i], fg.load_path(root))
        for file in lf:
            print(file, 'f')
            print(x[valid_encs["EX"][i]][0][file])
        lp = fg.loaded_position(valid_encs["X"][i], root)
        for file in lp:
            print(file, 'fs')
            print(y[valid_encs["EX"][i]][file])
else:
    lf = fg.loaded_files(encounter, fg.load_path(root))
    for file in lf:
        print(file, 'z')
        print(x["E" + str(encounter)][0][file])
    lp = fg.position_import(encounter, root)
    for file in lp:
        print(file, 's')
        print(y["E" + str(encounter)][file])





