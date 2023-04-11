import math
import numpy as np

from modules.core.vars import str_man as sm
from modules.core.loadsave import file_dir as fd


slash = fd.slash()

def theta_ap_0(r_0, r_1, n_p_1, eta_ap, v_p_1, t_p_1, theta_ap_1,
               n_step=1000, save_files=False):
    # Initialize the alpha-proton charge and mass ratios.
    z_a = 2.
    mu_a = 4.

    # Initialise.
    d_r = (r_0 - r_1) / (1. * n_step)

    theta_ap = theta_ap_1


    # Loop.
    save_theta = []
    save_radius = []
    for i in range(n_step):

        r = r_1 + ((i + 1) * d_r)

        n_p = n_p_1 * (r / r_1) ** -1.8
        v_p = v_p_1 * (r / r_1) ** -0.2
        t_p = t_p_1 * (r / r_1) ** -0.77

        alpha = (theta_ap + mu_a)
        beta = theta_ap

        if alpha == 0:
            alpha = float('Nan')
        if beta == 0:
            beta = float('Nan')

        charlie = 1 + (z_a ** 2 * eta_ap / beta)
        if charlie < 0:
            charlie = 0

        arg_ = ((n_p ** 0.5 / t_p ** 1.5) * (z_a * (mu_a + 1) / alpha) *
                (charlie) ** 0.5)

        if arg_ == 0:
            arg_ = math.exp(9)
        elif arg_ < 0:
            arg_ = math.exp(9)
        else:
            pass

        lambda_ap = 9 + np.log(arg_)

        x = (v_p * t_p ** 1.5)
        y = (eta_ap + 1) ** 2.5

        if theta_ap == float('Nan'):
            z = float('Nan')
        else:
            z = (theta_ap + mu_a) ** 1.5

        if x == 0:
            x = float('Nan')
        if y == 0:
            y = float('Nan')
        if z == 0:
            z = float('Nan')
        elif z < 0:
            z = float('Nan')



        d_theta_ap = ((-2.60e7) * ((n_p /x)) * (mu_a ** 0.5 * z_a ** 2 / y) * ((theta_ap - 1.) * (eta_ap * theta_ap + 1.) ** 2.5 / z) * (lambda_ap) * (d_r))

        theta_ap = theta_ap + d_theta_ap
        save_theta.append(theta_ap)
        save_radius.append(r)

    x = sm.slash_dir(fd.dir_drop(fd.dir_parent()))
    x = x + 'data' + slash + 'save' + slash + 'Fig5' + slash
    if save_files:
        fn1 = x + 'theta' + str(theta_ap_1) + '.txt'
        fn2 = x + 'radius' + str(theta_ap_1) + '.txt'
        np.savetxt(fn1, save_theta)
        np.savetxt(fn2, save_radius)

    return theta_ap



def theta_loop(
        time,
        wind_radius,
        psp_radius,
        density_p,
        density_ap,
        speed,
        temp,
        theta,
        save=False,
        n_=500,
):

    final_theta = np.zeros(len(time))
    L = int(len(theta))
    print(len(wind_radius), len(psp_radius), len(density_p),
                                    len(density_ap), len(speed), len(temp), len(theta))
    for i in range(L):
        final_theta[i] = theta_ap_0(wind_radius[i], psp_radius[i], density_p[i],
                                    density_ap[i], speed[i], temp[i], theta[i], n_, save)
        print('\r', f"{(i / len(time)) * 100:.2f} %", end="")

    return final_theta

def make_theta_vals(
        time,
        density_p,
        density_ap,
        temp,
        speed,
        theta,
        psp_radius,
        wind_radius_,
        save_theta_r=False,
):
    wind_radius = np.full(shape=len(time), fill_value=wind_radius_, dtype=float)
    final_theta = theta_loop(time, wind_radius, psp_radius, density_p, density_ap, speed, temp, theta, save_theta_r)
    return final_theta


def generate_theta(
        solar_data,
        spc_data,
        psp_scalar_temps,
        wind_scalar_temps,
        wind_radius,
        theta_ap_0,
        save_loc,
        save_theta_r=False,
):

    t = 'time'
    p = 'proton'
    psp = 'PSP.csv'

    time = solar_data[p][t]
    density_p = solar_data[p]['np1']
    density_ap = psp_scalar_temps['dens_ap']
    temp = psp_scalar_temps['proton_scalar_temp_1']
    speed = solar_data[p]['v_mag']

    psp_radius = spc_data[psp]['RADIAL_DISTANCE_AU']

    theta_ap_final = make_theta_vals(time, density_p, density_ap, temp, speed, theta_ap_0, psp_radius, wind_radius, save_theta_r)

    theta = {'0.1 - 0.2': theta_ap_0, str(wind_radius): theta_ap_final}

    file_names = ['theta_i.txt', 'theta_f.txt', 'wind_theta.txt']
    temp_files = [theta['0.1 - 0.2'], theta[str(wind_radius)], theta[str(wind_radius)]]
                  #wind_scalar_temps['wind_theta']]


    for i in range(len(file_names)):
        loc = sm.jwos(save_loc, file_names[i])
        np.savetxt(loc, temp_files[i])

    return theta_ap_final