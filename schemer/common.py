__version__='0.0.1'

def atom(x):
    return not isinstance(x, list) and x is not None

def null(lat):
    return not len(lat)

def car(lat):
    if isinstance(lat, list):
        return lat[0]

def cdr(lat):
    new_list = lat.copy()
    if new_list:
        new_list.pop(0)
    return new_list

def lat(x):
    if isinstance(x, list) and not null(x):
        return True
    elif atom(car(x)):
        lat(cdr(x))
    else:
        return False

def member(a, lat):
    if null(lat):
        return False
    else:
        return car(lat) == a or member(a, cdr(lat))
