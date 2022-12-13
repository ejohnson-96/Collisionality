from modules.core.loadsave import file_dir as fd
from modules.core.vars.string_man import valid_string


def type_check(
        loc,
        ftype,
):
    loc = valid_string(loc)
    ftype = valid_string(ftype)

    if fd.file_ext(loc) != ftype:
        raise ValueError(
            "Error: File extension provided is not appropriate, "
            f"'{ftype} is the required file type, instead got {fd.file_ext(loc)}."

        )
    else:
        return True


def data_type(
        data,
):
    return type(data)


class types:
    valid_file_types = ['.csv', '.xlsx', '.pkl', '.txt']

