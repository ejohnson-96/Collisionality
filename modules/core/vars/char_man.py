from modules.core.constants import sys_const
from modules.core.vars.bool_man import valid_bool
from modules.core.vars.num_man import valid_num
from modules.core.vars.str_man import valid_str, jwos, jws


def valid_char(
        *args,
        length=1,
        var=False,
):
    valid_bool(var)
    y = valid_num(length, floats=False)
    print(y)
    for arg in args:
        if not isinstance(arg, str):
            raise TypeError(
                f"Argument {arg} is of incorrect type, str type is "
                f"required and a length of {length}. Instead got type"
                f" of {type(arg)} and a length of {len(arg)}."
            )
        else:
            if len(arg) != length:
                raise ValueError(
                    f"Argument {arg} can only have a length of "
                    f"{length}, instead got length of {len(arg)}."
                )
            else:
                if var:
                    return args
                else:
                    return True


def cap_first_let(
        string,
):
    if valid_str(string):
        return string.capitalize()


def cap_all_first_let(
        string,
):
    if valid_str(string):
        return ' '.join(elem.capitalize() for elem in string.split())


def cap_all_let(
        string,
):
    if valid_str(string):
        return string.upper()


def low_first_let(
        string,
):
    if valid_str(string):
        return string[0].lower() + string[1:]


def low_all_first_let(
        string,
):
    if valid_str(string):
        return ' '.join(elem.lower() for elem in string.split())


def low_all_let(
        string,
):
    if valid_str(string):
        return string.lower()


def del_end(
        string,
):
    if valid_str(string):
        return string[:len(string) - 1]


def del_beg(
        string,
):
    if valid_str(string):
        return string[1:]


def rep_char(
        string,
        character,
        replacement,
):
    valid_str(string)
    valid_char(character, replacement)

    if character in string:
        return string.replace(character, replacement)
    else:
        raise ValueError(
            f"Argument {string} does not contain the character "
            f"{character}. Please try again."
        )


def rem_char(
        string,
        character,
):
    return rep_char(string, character, '')


def add_spc_beg(
        string,
):
    if valid_str(string):
        return ' ' + string


def add_spc_end(
        string,
):
    if valid_str(string):
        return string + ' '


def is_up(
        string,
):
    if valid_str(string):
        return string.isupper()


def is_low(
        string,
):
    if valid_str(string):
        return string.islower()


def nato(
        string,
        return_list=False,
):

    valid_str(string)
    valid_bool(return_list)

    if low_all_let(string.split()[0]) in sys_const.nato:
        phonetic = True
    else:
        phonetic = False

    res = ''
    res_list = []
    prev = None

    if not phonetic:
        first = True
        for letter in string:
            if low_all_let(letter) in sys_const.alphabet:
                arg = sys_const.alphabet.index(low_all_let(letter))
                if first:
                    res = jwos(res, sys_const.nato[arg])
                    res_list.append(cap_first_let(sys_const.nato[arg]))
                else:
                    res = jws(res, sys_const.nato[arg])
                    res_list.append(cap_first_let(sys_const.nato[arg]))
            elif letter in sys_const.numerical:
                if first:
                    res = jwos(res, letter)
                    res_list.append(letter)
                else:
                    if prev in sys_const.numerical:
                        res = jwos(res, letter)
                        res_list.append(letter)
                    else:
                        res = jws(res, letter)
                        res_list.append(letter)
            elif letter in sys_const.symbols:
                res = jwos(res, letter)
                res_list.append(letter)
            elif letter == ' ':
                if prev in sys_const.symbols:
                    continue
                else:
                    res = res + ','
                    res_list.append(' ')
            else:
                raise ValueError(
                    f"Argument {letter} does not appear in the "
                    f"alphabet. Please try again, {sys_const.alphabet}."
                )
            prev = letter
            first = False
    else:
        chars = string.split(' ')
        first = True
        prev = None

        for char in chars:
            if low_all_let(char) in sys_const.nato:
                arg = sys_const.nato.index(low_all_let(char))
                if first:
                    res = jwos(res, sys_const.alphabet[arg])
                    res_list.append(cap_first_let(sys_const.alphabet[arg]))
                else:
                    res = jws(res, sys_const.alphabet[arg])
                    res_list.append(' ')
                    res_list.append(cap_first_let(sys_const.alphabet[arg]))
            else:
                second = True
                for digit in char:
                    if digit in sys_const.numerical:
                        if first:
                            res = jwos(res, digit)
                            res_list.append((cap_first_let(digit)))
                        else:
                            if prev in sys_const.numerical:
                                if second:
                                    res = jws(res, digit)
                                    res_list.append(' ')
                                    res_list.append(digit)
                                else:
                                    res = jwos(res, digit)
                                    res_list.append(cap_first_let(digit))
                            else:
                                res = jws(res, digit)
                                res_list.append(' ')
                                res_list.append(cap_first_let(digit))
                    elif digit in sys_const.symbols:
                        res = jwos(res, digit)
                        res_list.append(digit)
                    else:
                        raise ValueError(
                            f"Argument {digit} does not appear in the "
                            f"NATO alphabet. Please try again, {sys_const.nato}."
                        )
                    second = False
                    prev = digit
            first = False

    if res_list:
        return res_list
    else:
        return cap_all_first_let(res)

