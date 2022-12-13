from matplotlib import colors as mcolors, lines as line, markers as mark
from modules.core.vars.str_man import valid_str


def valid_styles_list(

):
    return list(list(line.lineStyles.keys()) + list(mark.MarkerStyle.markers.keys()))


def colour_validate(
        colour,
):
    default_colour = 'black'
    colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
    by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                    for name, color in colors.items())
    valid_colors = [name for hsv, name in by_hsv]

    if colour is None:
        return default_colour
    else:
        valid_str(colour)
        if colour in valid_colors:
            return colour
        else:
            raise ValueError(
                f"Argument {colour}, is not a valid colour. \n"
                f"Please select from the following:\n{valid_colors}"
            )


def style_validate(
        line_style,
):
    valid_styles = valid_styles_list()

    valid_str(line_style)
    if line_style in valid_styles:
        return line_style
    else:
        raise ValueError(
            f"Argument {line_style}, is not a valid line style. \n"
            f"Please select from the following:\n{valid_styles}"
        )

