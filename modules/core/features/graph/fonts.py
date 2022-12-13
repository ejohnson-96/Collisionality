import os
from matplotlib import font_manager
from modules.core.vars import char_man as cm, str_man as sm


def font_list(

):
    fpaths = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')

    res = {'name': [], 'dir': []}

    i = 0
    for font_name in fpaths:
        res['name'].append(os.path.basename(font_name))
        res['dir'].append(str(fpaths[i]))
        i += 1

    return res


def font_names(

):
    fonts = font_list()
    return fonts['name']


def font_dir(

):
    fonts = font_list()
    return fonts['dir']


def check_font_valid(
        font,
):
    font = sm.valid_str(font)

    valid_fonts = font_names()

    for i in range(len(valid_fonts)):
        valid_fonts[i] = cm.lower_all_letter(valid_fonts[i])

    input_font = cm.lower_all_letter(font)

    if input_font in valid_fonts:
        return True
    else:
        return False


def load_font(
        loc,
):
    sm.valid_str(loc)
    valid_file = 'ttf'
    file_check = loc.split('.')

    if cm.lower_all_letter(file_check[-1]) == valid_file:
        font_manager.fontManager.addfont(loc)
    else:
        raise ValueError(
            'Error: Directory location provided does not appear '
            'to be the correct file type, instead got '
            f'type {file_check[-1]}'
        )

    return


