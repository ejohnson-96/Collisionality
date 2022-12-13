import time
import datetime
from modules.core.vars import char_man as cm
from modules.core.vars.num_man import valid_int, valid_num
from modules.core.vars import string_man as sm


def validate_time(
        time,
):
    if len(time) != 11:
        return "Invalid time format! Format HH:MM:SS is required," \
               f" instead got {time}. Please try again..."
    else:
        if int(time[0:2]) > 24:
            return "Invalid HOUR format! Hour argument provided " \
                   f"{time[0:2]}. Please try again..."
        elif int(time[3:5]) > 59:
            return "Invalid MINUTE format! Minute argument provided " \
                   f"{time[3:5]}. Please try again..."
        elif int(time[6:8]) > 59:
            return "Invalid SECOND format! Second argument provided " \
                   f"{time[6:8]}. Please try again..."
        else:
            return time


def countdown(
        t_,
):
    t_ = valid_int(t_)
    if t_ < 0:
        raise ValueError(
            "Error: Countdown number cannot be negative."
        )
    elif t_ == 0:
        raise ValueError(
            "Warning: Countdown number set to zero."
        )
    else:
        while t_:
            mins, secs = divmod(t_, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t_ -= 1
    return


def alarm_clock(
        alarm_time,
):
    validate_time(alarm_time.lower())
    print(f"Setting alarm for {alarm_time}...")

    alarm_hour = alarm_time[0:2]
    alarm_min = alarm_time[3:5]
    alarm_sec = alarm_time[6:8]
    alarm_period = alarm_time[9:].upper()

    now = datetime.now()

    h = 0
    while h < 1:
        if alarm_period == now.strftime("%p"):
            if alarm_hour == now.strftime("%I"):
                if alarm_min == now.strftime("%M"):
                    if alarm_sec == now.strftime("%S"):
                        print("Wake Up!")
                        h = 1
    return


def datetime_format(
        entry,
        epoch=False,
):
    entry = sm.valid_string(entry)
    entry = cm.remove_end(entry)
    entry = sm.split(entry, 'T')

    date = sm.split(entry[0], '-')
    time = sm.split(entry[1], ':')

    if epoch:
        return datetime_epoch(datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(float(time[2]))))
    else:
        return datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(float(time[2])))


def valid_datetime(
        entry,
):
    if not isinstance(entry, datetime.datetime):
        raise TypeError(
            f"Error: Argument {entry}, is not a datetime type, "
            f"instead got type of {type(entry)}. "
        )
    else:
        return entry


def valid_date(
        entry,
):
    if not isinstance(entry, datetime.date):
        raise TypeError(
            f"Error: Argument {entry}, is not a datetime.date type, "
            f"instead got type of {type(entry)}. "
        )
    else:
        return entry


def valid_time(
        entry,
):
    if not isinstance(entry, datetime.time):
        raise TypeError(
            f"Error: Argument {entry}, is not a datetime.time type, "
            f"instead got type of {type(entry)}. "
        )
    else:
        return entry


def valid_all(
        entry,
):
    if not isinstance(entry, (datetime.time, datetime.datetime, datetime.date)):
        raise TypeError(
            f"Error: Argument {entry}, is not a datetime, datetime.time,"
            f" or datetime.date type. Instead got type of {type(entry)}. "
        )
    else:
        return entry

    return


def time_format(
        entry,
):
    entry = valid_datetime(entry)
    return entry.time()


def date_format(
        entry,
):
    entry = valid_datetime(entry)
    return entry.date()


def datetime_epoch(
        entry,
):
    entry = valid_datetime(entry)
    return (entry - datetime.datetime(1970, 1, 1)).total_seconds()


def epoch_datetime(
        entry,
):
    entry = valid_num(entry)
    return datetime.datetime.fromtimestamp(entry)


def time_dif(
        a,
        b,
):
    a = valid_all(a)
    b = valid_all(b)

    if type(a) != type(b):
        raise TypeError(
            f"Error: Arguments provided, {a} and {b}, must be of the"
            f" same datetime type. Instead got types of {type(a)} and"
            f" {type(b)}, respectively."
        )
    elif type(a) == datetime.time:
        date = gen_date(1,1,1971)
        a = datetime.datetime.combine(date, a)
        b = datetime.datetime.combine(date, b)

    return b - a


def gen_date(
        day,
        month,
        year,
):
    for arg_name in (day, month, year):
        if not isinstance(arg_name, (int, float)):
            raise TypeError(
                f"Error: Argument {arg_name}, is not of type int or "
                f"float. Instead got type of {type(arg_name)}."
            )

    if len(str(year)) != 4:
        raise ValueError(
            f"Error: Argument {year}, is not a valid year. Use "
            "a 4 digit format and please try again. "
        )
    elif month > 12:
        raise ValueError(
            f"Error: Argument {month}, cannot be greater than 12."
        )
    elif day > 31:
        raise ValueError(
            f"Error: Argument {day}, cannot be greater than 31."
        )
    else:
        return datetime.date(year, month, day)


def gen_time(
        hour,
        min,
        sec=0,
        microsec=0,
):
    for arg_name in (hour, min, sec, microsec):
        if not isinstance(arg_name, (int, float, str)):
            raise TypeError(
                f"Error: Argument {arg_name}, is not of type int or "
                f"float. Instead got type of {type(arg_name)}."
            )
        if isinstance(arg_name, str):
            if arg_name.isdigit():
                continue
            else:
                raise ValueError(
                    f"Error: Argument {arg_name}, is a str type, "
                    "however, entry is not a valid number. "
                )
    if hour > 24:
        raise ValueError(
            f"Error: Argument {hour}, cannot be greater than 24."
        )
    elif min > 59:
        raise ValueError(
            f"Error: Argument {min}, cannot be greater than 59"
        )
    elif sec > 59:
        raise ValueError(
            f"Error: Argument {sec}, cannot be greater than 59"
        )
    elif microsec > 59:
        raise ValueError(
            f"Error: Argument {microsec}, cannot be greater than 59"
        )
    else:
        return datetime.time(hour, min, sec, microsec)


def gen_datetime(
        day,
        month,
        year,
        hour,
        min,
        sec=0,
        microsec=0,
):
    date = gen_date(day, month, year)
    time = gen_time(hour, min, sec, microsec)

    return datetime.datetime.combine(date, time)

