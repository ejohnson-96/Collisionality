import matplotlib.pyplot as plt
import numpy as np

from modules.collisions.model import file_gen as fg, data_gen as dg, enc_gen as eg, theta_gen as tg
from modules.core.loadsave import file_dir as fd
from modules.collisions.graph import figures as fig

slash = fd.slash()
root, valid_encs, particles = dg.gen_const()

save_dir = "/Users/elliotjohnson/Storage"

def generate_files(

):
    encounter = eg.enc_selector()
    parker, position = dg.data_import(encounter)
    parker, position, errors = dg.data_validate(parker, position)
    parker, position = dg.data_combine(parker, position, particles)
    parker, psp_data, wind_data = fg.scalar_gen(parker, position)

    for file in (parker, position, errors, psp_data, wind_data):
        name = [i for i, j in locals().items() if j == file][0]
        fg.save_file(file, name, save_dir)

    return

def generate_theta(
    wind_radius=[1.0],
    save_theta_r=False,
):
    path = "/Users/elliotjohnson/GitHub/Collisions/data/save/"

    solar, space, error, psp, wind = fg.load_files(save_dir)

    theta_ap_0 = psp['theta_ap']

    for radius in wind_radius:
        save_loc = path + str(radius) + slash
        tg.generate_theta(solar, space, psp, wind, radius, theta_ap_0, save_loc, save_theta_r)

    return


#generate_files()
theta_ap_f = generate_theta()


solar, space, error, psp, wind = fg.load_files(save_dir)
print(space.keys())
print(theta_ap_f)

x = theta_ap_f #psp['theta_ap']
weg = np.ones_like(x) / float(len(x))

plt.figure(figsize=(10, 10))
results, edges = np.histogram(x, weights=weg, bins=50, density=1, range=(0,15)) #range
binWidth = edges[1] - edges[0]
xs, ys = fig.make_bars(edges[:-1], results * binWidth, binWidth / 2)

plt.plot(xs, ys, color='black', linestyle='--', linewidth=2, label=r'r = 0.1 - 0.27 ${\rm au}$', )
plt.show()

