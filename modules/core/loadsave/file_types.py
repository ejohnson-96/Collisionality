from modules.core.loadsave import file_dir as fd
from modules.core.vars.str_man import valid_str


class types:
    valid_file_types = ['.csv', '.xlsx', '.pkl', '.txt']


def valid_type(
        loc,
        ftype,
):
    valid_str(loc, ftype)

    if ftype in types.valid_file_types:
        if fd.file_ext(loc) != ftype:
            raise ValueError(
                f""
            )
        else:
            return True

    else:
        raise ValueError(
            f""
        )


def data_type(
        data,
):
    return type(data)



