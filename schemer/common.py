__version__='0.0.1'

def atom(x):
    return not isinstance(x, list) and x is not None

def null(lat):
    return not len(lat)

def cons(x, lat):
    new_list = lat.copy()
    new_list.insert(0, x)
    return new_list

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
        return lat(cdr(x))
    else:
        return False

def member(a, lat):
    if null(lat):
        return False
    else:
        return car(lat) == a or member(a, cdr(lat))

def rember(a, lat):
    if null(lat):
        return []
    elif car(lat) == a:
        return cdr(lat)
    else:
        return cons(car(lat), rember(a, cdr(lat)))

def firsts(lat):
    if null(lat):
        return []
    else:
        return cons(car(car(lat)), firsts(cdr(lat)))

def insertL(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(new, cons(old, cdr(lat)))
    else:
        return cons(car(lat), insertL(new, old, cdr(lat)))

def insertR(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(old, cons(new, cdr(lat)))
    else:
        return cons(car(lat), insertR(new, old, cdr(lat)))

def subst(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(new, cdr(lat))
    else:
        return cons(car(lat), subst(new, old, cdr(lat)))






