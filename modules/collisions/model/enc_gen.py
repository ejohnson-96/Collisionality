from modules.core.loadsave import file_dir as fd
from modules.core.vars import char_man as cm, str_man as sm


slash = fd.slash()


def root(

):
    root_dir = fd.dir_path()
    for i in range(2):
        root_dir = fd.dir_drop(root_dir)
    return root_dir + slash


def enc_gen(

):
    data_path = root() + slash + "data" + slash + "load" + slash

    encs = []
    encs_num = []

    for folder in fd.dir_list(data_path):
        if folder[0] == 'E' and len(folder) < 4:
            encs.append(folder)
            encs_num.append(folder[1:len(folder)])

    return {"EX":encs, "X":encs_num}


def enc_selector(

):
    print('Currently loaded encounters:', enc_gen()["EX"], '\n')

    valid_full = ['f', 'full', 'ful', 'fu', 'ull', 'ff']
    valid_single = ['s', 'single', 'ss', 'sngle', 'sig', 'ingle', ]

    h = 1
    while h > 0:
        data_set_input = input('Full data set or singular? (F/S)')
        sm.valid_str(data_set_input)
        data_set_input = cm.low_all_let(data_set_input)
        if data_set_input in valid_full:
            encounter = 0
            h = 0
        elif data_set_input in valid_single:
            g = 1
            while g > 0:
                enc_input = input('Please enter an encounter:')
                if enc_input.isdigit():
                    if enc_input in enc_gen()["X"]:
                        encounter = int(enc_input)
                        g = 0
                    else:
                        print(f"Input argument 'enc_input' is not a valid input. Valid inputs are {enc_gen()[1]}, "
                              f"please try again.")
                else:
                    print(
                        f"Input argument {enc_input} is not valid, str type is required, instead got type {type(enc_input)}.")
            h = 0
        else:
            print('Error: Please make a valid selection.')

    return int(encounter)


def particle_gen(

):
    p = 'proton'
    a = 'alpha'
    return  [p, a]
