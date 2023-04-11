import datetime
from modules.core.loadsave import file_import as fi, file_dir as fd, file_export as fe
from modules.core.vars import char_man as cm, str_man as sm

def datetime_format(
        entry,
        epoch=False,
):
    sm.valid_str(entry)
    entry = cm.del_end(entry)
    entry = sm.split(entry, 'T')

    date = sm.split(entry[0], '-')
    time = sm.split(entry[1], ':')

    if epoch:
        return datetime_epoch(datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(float(time[2]))))
    else:
        return datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(float(time[2])))

def datetime_epoch(
        entry,
):
    entry = valid_datetime(entry)
    return (entry - datetime.datetime(1970, 1, 1)).total_seconds()

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



slash = fd.slash()
path = fd.dir_path()
for i in range(3):
    path = fd.dir_drop(path)

encounter = 6
filename = "Wind_Speed.csv"
path = path + slash + "data" + slash + "load" + slash + "E" + str(encounter) + slash + "Position" + slash
if fd.file_exists(path + slash + filename):
    print(filename, path)
    file = fi.load_csv(filename, path)

key = list(file.keys())[0]

if key == "EPOCH_yyyy-mm-ddThh:mm:ss.sssZ":
    print("dsfsd")
elif key == "time":
    if isinstance(file[key][1], str):
        for i in range(len(file[key])):
            file[key][i] = float(datetime_format(file[key][i], epoch=True))
    print(file, filename, path)
    fe.save_csv(file, filename, path)

else:
    print(key)

