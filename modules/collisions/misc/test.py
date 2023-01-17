
#test file for data import

from urllib.request import urlopen

psp_url = "https://cdaweb.gsfc.nasa.gov/cgi-bin/eval2.cgi" #something probs with cookies
wind_url = "https://cdaweb.gsfc.nasa.gov/cgi-bin/eval2.cgi"


page = urlopen(psp_url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)



def data_cadence(
        data,
        factor=16,
):
    res = {}
    if factor == 0:
        return data
    else:
        for y in data.keys():
            res[y] = {}
            for z in data[y].keys():
                res[y][z] = []
                L = int(len(data[y][z]))
                for i in range(int(L/factor)):
                    arg_ = 0
                    for j in range(factor):
                        arg_ = arg_ + data[y][z][i + j]
                    if z == 'time':
                        arg_ = arg_
                    else:
                        arg_ = arg_/factor
                    res[y][z].append(arg_)
    return res


for encounter in range(enc.num_of_encs):

    if enc.encounter[encounter] == 'E4':
        factor = 16
    elif enc.encounter[encounter] == 'E6':
        factor = 0
    elif enc.encounter[encounter] == 'E7':
        factor = 1

    print(factor)

    solar_data[enc.encounter[encounter]] = data_cadence(solar_data[enc.encounter[encounter]], factor)
    if not error_data is None:
        error_data[enc.encounter[encounter]] = data_cadence(error_data[enc.encounter[encounter]], factor)

    # spc_data[enc.encounter[encounter]] = data_cadence(spc_data[enc.encounter[encounter]], factor)

    res = list(solar_data[enc.encounter[encounter]].keys())[0]
    t_ = solar_data[enc.encounter[encounter]][res][t]

    for y in solar_data[enc.encounter[encounter]].keys():
        xp = solar_data[enc.encounter[encounter]][y][t]
        for z in solar_data[enc.encounter[encounter]][y].keys():
            fp = solar_data[enc.encounter[encounter]][y][z]
            solar_data[enc.encounter[encounter]][y][z] = np.interp(t_, xp, fp)
            # mm_data[x][y][z] = np.resize(mm_data[x][y][z], min_len)

    if enc.error_files_loaded:
        for y in error_data[enc.encounter[encounter]].keys():
            xp = error_data[enc.encounter[encounter]][y][t]
            for z in error_data[enc.encounter[encounter]][y].keys():
                fp = error_data[enc.encounter[encounter]][y][z]
                error_data[enc.encounter[encounter]][y][z] = np.interp(t_, xp, fp)
                # error_data[x][y][z] = np.resize(error_data[x][y][z], min_len)

    for y in spc_data[enc.encounter[encounter]].keys():
        xp = spc_data[enc.encounter[encounter]][y][t]
        for z in spc_data[enc.encounter[encounter]][y].keys():
            fp = spc_data[enc.encounter[encounter]][y][z]
            spc_data[enc.encounter[encounter]][y][z] = np.interp(t_, xp, fp)
            # sc_data[x][y][z] = np.resize(sc_data[x][y][z], min_len)
