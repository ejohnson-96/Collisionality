from modules.core.loadsave import file_dir as fd
from modules.core.vars import num_man as nm, str_man as sm

slash = fd.slash()

def root(

):
    root = fd.dir_path()
    for i in range(3):
        root = fd.dir_drop(root)
    return root

def enc_gen(

):

    data_path = root() + slash + "data" + slash + "load" + slash

    encs = []
    encs_num = []

    for folder in fd.dir_list(data_path):
        if folder[0] == 'E':
            encs.append(folder)
            encs_num.append(folder[-1])

    return encs, encs_num


def load_generate(
        encounter,

):
    encounter = nm.valid_num(encounter, integer=True)

    path = sm.jwos(root(), slash, 'data', slash, 'save', slash)
    print(enc_gen()[0])
    h = 1
    while h > 1:
        if encounter == 0:
            return 'EA'
        elif encounter in enc_gen()[0]:
            return sm.jwos('E', str(int(encounter)))


load_generate(1)
