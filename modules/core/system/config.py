import sys
import warnings
import platform
import psutil
import GPUtil
import datetime as dt
from modules.core.vars.bool_man import valid_bool
from modules.core.vars.string_man import valid_string

windows = 'Windows'
mac = 'Mac OS'
linux = 'Linux'


def get_platform(

):
    platforms = {
        'linux1': linux,
        'linux2': linux,
        'darwin': mac,
        'win32': windows
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


def windows_os(

):
    if get_platform() == windows:
        return True
    else:
        return False


def mac_os(

):
    if get_platform() == mac:
        return True
    else:
        return False


def linux_os(

):
    if get_platform() == linux:
        return True
    else:
        return False


def kill(
        warning=False,
):
    warning = valid_bool(warning)

    if warning:
        warnings.warn(
            "Warning: Application exit process initiated."
        )
        sys.exit()
    else:
        sys.exit()


def sys_info(
        system=True,
        name=False,
        release=False,
        version=False,
        machine=False,
        processor=False,
        complete=False,
):
    inpts = [system, name, release, version, machine, processor, complete]

    for arg_name in inpts:
        valid_bool(arg_name)

    uname = platform.uname()
    res = {}

    if not any(inpts):
        raise warnings.warn(
            "Warning: Function was provided with only False arguments."
        )
    else:
        if complete:
            if uname.system == "Darwin":
                res['System'] = mac
            else:
                res['System'] = uname.system
            res['Name'] = uname.node
            res['Release'] = uname.release
            res['Version'] = uname.version
            res['Machine'] = uname.machine
            res['Processor'] = uname.processor
        else:
            if system:
                if uname.system == "Darwin":
                    res['System'] = mac
                else:
                    res['System'] = uname.system
            if name:
                res['Name'] = uname.node
            if release:
                res['Release'] = uname.release
            if version:
                res['Version'] = uname.version
            if machine:
                res['Machine'] = uname.machine
            if processor:
                res['Processor'] = uname.processor

    return res


def boot_time(
        time=False,
        date=False,
        us_date=False,
):
    time = valid_bool(time)
    date = valid_bool(date)
    us_date = valid_bool(us_date)

    boot_time_timestamp = psutil.boot_time()
    bt = dt.datetime.fromtimestamp(boot_time_timestamp)

    if us_date:
        d = str(bt.month) + "/" + str(bt.day) + "/" + str(bt.year)
    else:
        d = str(bt.day) + "/" + str(bt.month) + "/" + str(bt.year)

    t = str(bt.hour) + ":" + str(bt.minute) + ":" + str(bt.second)
    if time:
        return t
    if date:
        return d

    if not time and not date:
        return t + " " + d


def get_size(
        bytes,
        suffix="B"
):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor


def cpu_info(

):
    # let's print CPU information
    print("=" * 40, "CPU Info", "=" * 40)
    # number of cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    # CPU frequencies
    cpufreq = psutil.cpu_freq(percpu=True)
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    return


def ram_info(
        total=True,
        available=False,
        used=False,
        percent=False,
        complete=False,

):
    inpts = [total, available, used, percent, complete]
    svmem = psutil.virtual_memory()
    res = {}

    if not any(inpts):
        raise warnings.warn(
            "Warning: "
        )
    else:
        if complete:
            res['Total'] = get_size(svmem.total)
            res['Available'] = get_size(svmem.available)
            res['Used'] = get_size(svmem.used)
            res['Percent'] = svmem.percent
        else:
            if total:
                res['Total'] = get_size(svmem.total)
            if available:
                res['Available'] = get_size(svmem.available)
            if used:
                res['Used'] = get_size(svmem.used)
            if percent:
                res['Percent'] = svmem.percent
    return res


def memory_info(

):
    swap = psutil.swap_memory()
    print(swap)
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")

    return

def gpu_info(

):
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        # get the GPU id
        gpu_id = gpu.id
        # name of GPU
        gpu_name = gpu.name
        # get % percentage of GPU usage of that GPU
        gpu_load = f"{gpu.load*100}%"
        # get free memory in MB format
        gpu_free_memory = f"{gpu.memoryFree}MB"
        # get used memory
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        # get total memory
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        # get GPU temperature in Celsius
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
            gpu_total_memory, gpu_temperature, gpu_uuid
        ))
    return list_gpus

