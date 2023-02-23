def abbrev_name(name):
    fio = name.split()
    return fio[0][0].upper() + '.' + fio[1][0].upper()


abbrev_name('sam Harris')