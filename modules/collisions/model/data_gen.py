import numpy as np

from modules.core.vars import bool_man as bm, num_man as nm
from modules.collisions.model import enc_gen as eg, file_gen as fg


def gen_const(

):
    root = eg.root()
    valid_encs = eg.enc_gen()
    particles = eg.particle_gen()
    return root, valid_encs, particles


def data_import(
        encounter
):
    position_data = {}
    parker_data = {}

    root, valid_encs, _ = gen_const()

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
            # print(file, position[enc][file])
            for param in position[enc][file].keys():
                if param == "datetime":
                    for i in range(len(position[enc][file][param])):
                        position[enc][file][param][i] = 1  # convertdate
                    # remane param
                    # delete previous datetime param
                for i in range(len(position[enc][file][param])):
                    nm.valid_num(position[enc][file][param][i])

    return parker, position, errors


def ave_cad(
        time,
):
    delta = []
    sum = 0
    for i in range(len(time) - 1):
        delta.append(time[i + 1] - time[i])
    for i in range(len(delta)):
        sum = sum + delta[i]
    return sum/len(delta)



def factor_gen(
        parker,
        position,
        cad=False
):
    bm.valid_bool(cad)

    parker_cadance = {}
    for enc in parker.keys():
        parker_cadance[enc] = {}
        for file in parker[enc][0].keys():
            parker_cadance[enc][file] = ave_cad(parker[enc][0][file]['time']), len(parker[enc][0][file]['time'])

    max_cad = 0
    for enc in parker_cadance.keys():
        for file in parker_cadance[enc].keys():
            if parker_cadance[enc][file][0] > max_cad:
                max_cad = parker_cadance[enc][file][0]

    parker_factors = {}
    for enc in parker_cadance.keys():
        parker_factors[enc] = {}
        for file in parker_cadance[enc].keys():
            parker_factors[enc][file] = int(max_cad/parker_cadance[enc][file][0])

    position_cadence = {}
    for enc in position.keys():
        position_cadence[enc] = {}
        for file in position[enc].keys():
            position_cadence[enc][file] = ave_cad(position[enc][file]['time']), len(position[enc][file]['time'])

    max_cad = 0
    for enc in position_cadence.keys():
        for file in position_cadence[enc].keys():
            if position_cadence[enc][file][0] > max_cad:
                max_cad = position_cadence[enc][file][0]

    position_factors = {}
    for enc in position_cadence.keys():
        position_factors[enc] = {}
        for file in position_cadence[enc].keys():
            position_factors[enc][file] = int(max_cad/position_cadence[enc][file][0])

    if cad:
        return parker_cadance, position_cadence
    else:
        return parker_factors, position_factors


def data_combine(
        parker,
        position,
        particles
):
    print("dsfsdfasd")
    park_out = {}
    pos_out = {}

    for particle in particles:
        park_out[particle] = {}
        for type in ["data", "errors"]:
            park_out[particle][type] = {}

    enc = parker.keys()

    test = []
    for enc in parker.keys():
        test.append(parker[enc][1])



    print(x)
    print()

    print(park_out)

    return park_out, pos_out



def data_resize(
        parker,
        position,
):
    t = 'time'
    factors = factor_gen(parker, position)
    cad = factor_gen(parker, position, True)

    for enc in parker.keys():
        for file in parker[enc][0].keys():
            parker[enc][0][file] = data_cadence(parker[enc][0][file], factors[0][enc][file])

    for enc in position.keys():
        for file in position[enc].keys():
            position[enc][file] = data_cadence(position[enc][file], factors[1][enc][file])

    #print(cad)
    #t_ = parker['E6'][0]['E6_alphas.csv'][t]
    #t_ = int(10000)

    #for enc in parker.keys():
    #    for file in parker[enc][0].keys():
    #        for param in parker[enc][0][file].keys():


    #for enc in position.keys():
    #    for file in position[enc].keys():
    #        xp = position[enc][file][t]
    #        for param in position[enc][file].keys():
    #            fp = position[enc][file][param]
    #            position[enc][file][param] = np.interp(t_, xp, fp)

    return parker, position


def data_cadence(
        data,
        factor,
):
    res = {}
    if factor == 1:
        return data
    else:
        for y in data.keys():
            res[y] = []
            L = int(len(data[y]))
            for i in range(int(L/factor)):
                arg_ = 0
                for j in range(factor):
                    arg_ = arg_ + data[y][i + j]
                arg_ = arg_/factor
                res[y].append(arg_)
    return res

