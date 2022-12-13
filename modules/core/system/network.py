import os, ipaddress, socket, webbrowser, wikipedia, psutil

import modules.core.vars.string_man as sm
from modules.core.system.config import get_size
from modules.core.vars.num_man import valid_num


def get_host(

):
    return socket.gethostname()


def get_ip(

):
    host_name = get_host()
    ip_address = socket.gethostbyname(host_name)

    return ip_address


def get_website_ip(
        url,
):
    valid_url = sm.web_check(url)
    return socket.gethostbyname(valid_url)


def open_web(
        url,
):
    url = sm.web_check(url)
    webbrowser.open(url)
    return


def wiki_search(
        query,
        sound=True,
        text=True,
        sent_num=2,
):
    query = sm.valid_string(query)
    results = wikipedia.summary(query, sentences=sent_num)

    if text:
        print(results)

    return results


def email_strip(
        email,
):
    email = sm.valid_string(email)

    if '@' in email:
        return email[:email.index('@')], email[email.index('@') + 1:]
    else:
        raise ValueError(
            f"Error: Invalid email provided, {email}."
        )


def valid_ip(
        inpt,
):
    inpt = valid_num(inpt)
    os.system('cls')

    while True:
        try:
            ipaddress.ip_address(inpt)
            return True
        except:
            return False


# Network information
print("=" * 40, "Network Information", "=" * 40)
# get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")
# get IO statistics since boot
net_io = psutil.net_io_counters()
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
