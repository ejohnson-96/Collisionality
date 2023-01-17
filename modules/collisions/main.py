from modules.collisions.model import file_gen as fg, data_gen as dg, enc_gen as eg
from modules.core.loadsave import file_dir as fd

slash = fd.slash()
encounter = eg.enc_selector()
root, valid_encs, particles = dg.gen_const()

parker, position = dg.data_import(encounter)
parker, position, errors = dg.data_validate(parker, position)
#print('slow here')
parker, position = dg.data_resize(parker, position)
parker, position = dg.data_combine(parker, position, particles)

print(parker.keys())
for key in parker.keys():
    print(key, key.keys())


# x[valid_enc["EX"][enc]]   [ 0 (dict), 1 (error bool)] [file]
print("throw error here")
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
