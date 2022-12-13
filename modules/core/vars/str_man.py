import validators
from modules.core.sys.config import windows_os
from modules.core.vars.bool_man import valid_bool


def valid_str(
        *args,
        var=False,
):
    valid_bool(var)
    for arg in args:
        if not isinstance(arg, str):
            raise TypeError(
                f"Argument {arg} is of incorrect type, str type is "
                f"required. Instead got type of {type(arg)}."
            )
    if var:
        return args
    else:
        return True


def jws(
        *args,
):
    res = ''
    for arg in args:
        valid_str(arg)
        res = ' '.join([res, arg])
    return res


def jwos(
        *args,
):
    res = ''
    for arg in args:
        valid_str(arg)
        res = ''.join([res, arg])
    return res


def slash_dir(
        arg,
):
    valid_str(arg)
    if arg.endswith("/") or arg.endswith("\\"):
        return arg
    else:
        if windows_os():
            return jwos(arg, '\\')
        else:
            return jwos(arg, '/')


def valid_url(
        url,
):
    valid_str(url)

    if url[:7] == 'http://':
        pass
    elif url[:3] == 'www':
        url = 'http://' + url
    else:
        url = 'http://' + 'www.' + url

    if url[-1] != '/':
        url = url + '/'

    if validators.url(url):
        return url
    else:
        raise ValueError(
            f"Argument {url} is not a valid URL, please try again."
        )


def split(
        string,
        character=" ",
):
    valid_str(string, character)

    if len(character) > 1:
        raise ValueError(
            f"Argument {character} for the split location value, can "
            f"only be a single value. Instead got length of {len(character)}."
        )
    else:
        return string.split(character)
