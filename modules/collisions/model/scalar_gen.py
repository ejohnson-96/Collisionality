import numpy as np


def scalar_velocity(
        parker,
):
    for particle in parker.keys():
        parker[particle]['v_mag'] = []
        L = len(parker[particle]['time'])

        if particle == "proton":
            x, y, z = 'vp1_x', 'vp1_y', 'vp1_z'
        if particle == "alpha":
            x, y, z = 'va_x', 'va_y', 'va_z'

        for i in range(L):
            arg_ = parker[particle][x][i] ** 2 + parker[particle][y][i] ** 2 + parker[particle][z][i] ** 2

            if arg_ < 0:
                arg_ = 0

            parker[particle]["v_mag"].append(np.sqrt(arg_))

    return parker


def scalar_temps(
        parker,
        position,
):
    psp_res, wind_res = temp_generate(parker, position)

    return psp_res, wind_res


def temp_generate(
        parker,
        position,
):
    factor = 11604

    psp_result = {}
    psp_result_keys = ['time', 'proton_scalar_temp_1', 'proton_scalar_temp_2',
                       'alpha_scalar_temp', 'theta_ap', 'dens_ap']
    wind_result = {}
    wind_result_keys = ['wind_alpha_scalar_temp', 'wind_proton_scalar_temp', 'wind_theta']

    file_val = []
    for file in parker.keys():
        file_val.append(file)

    p = "proton"
    a = "alpha"

    L_p = len(parker[p]["time"])
    L_a = len(parker[a]["time"])

    wind = position['Wind_Temps.csv']

    for res_key in psp_result_keys:
        if "proton" in res_key:
            psp_result[res_key] = np.zeros(L_p)
        else:
            psp_result[res_key] = np.zeros(L_a)

    L_w = len(wind["time"])
    for res_key in wind_result_keys:
        wind_result[res_key] = np.zeros(L_w)

    for i in range(L_p):
        psp_result['proton_scalar_temp_1'][i] = (
                (2 * parker[p]['Tperp1'][i] + parker[p]['Trat1'][
                    i]) / 3)*factor
        psp_result['proton_scalar_temp_2'][i] = (
                (2 * parker[p]['Tperp2'][i] + parker[p]['Trat2'][
                    i]) / 3)*factor

    for i in range(L_a):
        psp_result['alpha_scalar_temp'][i] = (
                (2 * parker[a]['Ta_perp'][i] + parker[a]['Trat'][
                    i]) / 3)*factor

        psp_result['theta_ap'][i] = psp_result['alpha_scalar_temp'][i] / psp_result['proton_scalar_temp_1'][i]

        if parker[p]["np1"][i] == 0:
            psp_result['dens_ap'][i] = float('Nan')
        else:
            psp_result['dens_ap'][i] = parker[a]["na"][i] / parker[p]["np1"][i]

    for i in range(L_w):
        if position['Wind_Temps.csv']['TEMPALPHAeV'][i] == 0:
            wind_result['wind_alpha_scalar_temp'][i] = float('Nan')
        else:
            wind_result['wind_alpha_scalar_temp'][i] = position['Wind_Temps.csv']['TEMPALPHAeV'][i]

        if wind['TEMPPROTNeV'][i] == 0:
            wind_result['wind_proton_scalar_temp'][i] = float('Nan')
            wind_result['wind_theta'][i] = float('Nan')
        else:
            wind_result['wind_proton_scalar_temp'][i] = (wind['TEMPPROTNeV'][i])
            wind_result['wind_theta'][i] = (
                    wind['TEMPALPHAeV'][i] / wind['TEMPPROTNeV'][i])

    return psp_result, wind_result
