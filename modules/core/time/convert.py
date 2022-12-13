import datetime

from modules.core.vars.num_man import valid_num


def epoch_time(
        epoch_time,
):
    epoch_time = valid_num(epoch_time)
    return datetime.datetime.fromtimestamp(epoch_time)






