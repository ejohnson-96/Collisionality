import numpy as np
import matplotlib.pyplot as plt

from modules.core.features.graph.constants import constants as const
from modules.core.features.graph import validate
from modules.core.vars.bool_man import valid_bool
from modules.core.vars.char_man import cap_first_let
from modules.core.vars.num_man import valid_num
from modules.core.vars.str_man import valid_str


def graph(
        x_data,
        y_data=None,
        x_lim=None,
        y_lim=None,
        title='Output',
        x_axis='x Data',
        y_axis='y Data',
        degree=0,
        grid=True,
        y_log=False,
        x_log=False,
        line_width=const.line_width,
        colour=None,
        line_style=None,
        leg_loc='upper right'
):
    legend = True
    plt.figure(figsize=(const.x_dim, const.y_dim))

    if not isinstance(x_data, (list, np.ndarray, dict)):
        raise ValueError(
            "Argument x_data is of incorrect type, acceptable "
            "types are: list, np.ndarray or dict. Instead got "
            f"type of {type(x_data)}."
        )

    valid_num(line_width)

    if colour is None:
        colour = const.default_colour
    elif isinstance(colour, list):
        for i in range(len(colour)):
            colour[i] = validate.colour_validate(colour[i])
    elif not isinstance(colour, str):
        raise TypeError(
            f"Argument {colour} is of incorrect type, type required "
            f"is either str or list. Instead got type of {type(colour)}."
        )

    if line_style is None:
        line_style = const.default_line_style
    elif isinstance(line_style, list):
        for line in line_style:
            line_style[line] = validate.style_validate(line)
    elif not isinstance(line_style, str):
        raise TypeError(
            f"Argument {colour} is of incorrect type, type required "
            f"is either str or list. Instead got type of {type(line_style)}"
        )

    if y_data is None:
        if isinstance(x_data, (list, np.ndarray)):
            if not isinstance(colour and line_style, str):
                raise ValueError(
                    "Arguments colour and line style must be of type "
                    f"str, instead got types of {type(colour)} and "
                    f"{type(line_style)} respectively. "
                )
            else:
                plt.plot(x_data, c=colour, ls=line_style, )
                legend = False

        elif isinstance(x_data, dict):

            if isinstance(colour, str):
                if isinstance(line_style, str):
                    i = 0
                    for data in x_data:
                        plt.plot(data, c=colour, ls=line_style, label=data, lw=line_width)
                        i = i + 1
                else:
                    if len(line_style) != len(x_data):
                        raise ValueError(
                            "Argument line style must be the same length as"
                            f" the data, instead got lengths of {len(line_style)}"
                            f" and {len(x_data)} respectively. "
                        )
                    else:
                        i = 0
                        for data in x_data:
                            plt.plot(data, c=colour, ls=line_style[i], label=data, lw=line_width)
                            i = i + 1

            else:
                if isinstance(line_style, str):
                    if len(colour) != len(x_data):
                        raise ValueError(
                            "Argument colour must be the same length as"
                            f" the data, instead got lengths of {len(colour)}"
                            f" and {len(x_data)} respectively. "
                        )
                    else:
                        i = 0
                        for data in x_data:
                            plt.plot(data, c=colour[i], ls=line_style, label=data, lw=line_width)
                            i = i + 1
                else:
                    if len(colour) != len(x_data) and len(line_style) != len(x_data):
                        raise ValueError(
                            "Argument colour and line style must be of the same length as"
                            f" the data. Instead got lengths of {len(colour)}, {len(line_style)} "
                            f"and {len(x_data)} for colour, line style and x data respectively."
                        )
                    else:
                        i = 0
                        for data in x_data:
                            plt.plot(data, c=colour[i], ls=line_style[i], label=data, lw=line_width)
                            i = i + 1

    else:
        if not isinstance(y_data, (list, np.ndarray, dict)):
            raise ValueError(
                "Argument y_data is of incorrect type, acceptable "
                "types are: list, np.ndarray or dict. Instead got "
                f"type of {type(y_data)}."
            )
        if type(x_data) == type(y_data):
            if isinstance(x_data, dict):
                if len(x_data) != len(y_data):
                    raise ValueError(
                        "Arguments for the x and y data must be of "
                        "the same length, instead got lengths of "
                        f"{len(x_data)} and {len(y_data)}."
                    )
                else:
                    if isinstance(colour, str) and isinstance(line_style, str):
                        i = 0
                        for x in x_data:
                            for y in y_data:
                                plt.plot(x_data[x], y_data[y], c=colour, ls=line_style, label=cap_first_let(x + y), lw=line_width)
                            i = i + 1
                    elif isinstance(colour, str) and isinstance(line_style, list):
                        i = 0
                        for x in x_data:
                            for y in y_data:
                                plt.plot(x_data[x], y_data[y], c=colour, ls=line_style[i], label=cap_first_let(x + y), lw=line_width)
                            i = i + 1
                    elif isinstance(colour, list) and isinstance(line_style, str):
                        i = 0
                        for x in x_data:
                            for y in y_data:
                                print(i)
                                plt.plot(x_data[x], y_data[y], c=colour[i], ls=line_style, label=cap_first_let(x + y), lw=line_width)
                            i = i + 1
                    else:
                        if len(colour) != len(x_data) and len(line_style) != len(x_data):
                            raise ValueError(
                                "Arguments for colours and line styles must be "
                                "the same length as the data. Instead got lengths "
                                f"of {len(colour)} and {len(line_style)} for colour"
                                f" and line style, lengths of {len(x_data)} and "
                                f"{len(y_data)} for the x and y data respectively."
                            )
                        else:
                            i = 0
                            for x in x_data:
                                for y in y_data:
                                    plt.plot(x_data[x], y_data[y], c=colour[i], ls=line_style[i], label=cap_first_let(x + y), lw=line_width)
                                i = i + 1
            else:
                if not isinstance(colour and line_style, str):
                    raise ValueError(
                        "Arguments colour and line_style must be of "
                        "type str when x and y are single valued arrays."
                        f"Instead got {colour} and {line_style} of types "
                        f"{type(colour)} and {type(line_style)} respectively."
                    )
                else:
                    plt.plot(x_data, y_data, c=colour, ls=line_style, lw=line_width)
                    legend = False
        else:
            if type(x_data) == list or type(x_data) == np.ndarray:
                i = 0
                for data in y_data:
                    plt.plot(x_data, y_data[data], label=cap_first_let(data), lw=line_width)
                    i = i + 1
            else:
                raise ValueError(
                    "Argument type configuration for x_data and "
                    "y_data is not supported. Either x_data and "
                    "y_data must be of the same type, either (list, "
                    "np.ndarray) or dict. Only x_data maybe of type "
                    "(list, np.ndarray) while y_data is of type dict."
                )

    if x_lim is not None:
        valid_num(x_lim)
        plt.xlim(x_lim)
    if y_lim is not None:
        valid_num(y_lim)
        plt.ylim(y_lim)

    if legend:
        valid_str(leg_loc)
        plt.legend(loc=leg_loc, prop={'size': const.legend_size})

    if valid_str(title, y_axis, x_axis):
        plt.title(title, fontsize=const.title_size, fontname=const.font_family)
        plt.ylabel(y_axis, fontsize=const.label_size, fontname=const.font_family)
        plt.xlabel(x_axis, fontsize=const.label_size, fontname=const.font_family)

    if valid_bool(grid):
        if grid:
            plt.grid()

    if valid_bool(x_log, y_log):
        if x_log:
            plt.xscale('log')
        if y_log:
            plt.yscale('log')

    if valid_num(degree):
        plt.xticks(rotation=degree)

    plt.xticks(fontsize=const.tick_size)
    plt.yticks(fontsize=const.tick_size)
    plt.show()

    return


c = 'red'

y = [1,2,3,4,5,6,7]


graph(y, leg_loc='upper left', colour=c)
