__version__='0.0.1'

# x is an atom
def atom(x):
    return not isinstance(x, list) and x is not None

# lat is empty
def null(lat):
    return not len(lat)

# construct new lat with x and lat
def cons(x, lat):
    new_list = lat.copy()
    new_list.insert(0, x)
    return new_list

# return first atom in lat
def car(lat):
    if isinstance(lat, list):
        return lat[0]

# return all of lat without its first atom
def cdr(lat):
    new_list = lat.copy()
    if new_list:
        new_list.pop(0)
    return new_list

# x is a lat
def lat(x):
    if isinstance(x, list) and not null(x):
        return True
    elif atom(car(x)):
        return lat(cdr(x))
    else:
        return False

# lat contains at least one occurance of a
def member(a, lat):
    if null(lat):
        return False
    else:
        return car(lat) == a or member(a, cdr(lat))

# remove first occurance of a from lat
def rember(a, lat):
    if null(lat):
        return []
    elif car(lat) == a:
        return cdr(lat)
    else:
        return cons(car(lat), rember(a, cdr(lat)))

# return new lat containing first elements from lat's lats
def firsts(lat):
    if null(lat):
        return []
    else:
        return cons(car(car(lat)), firsts(cdr(lat)))

# insert new atom into lat, to the left of first occurance of old
def insertL(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(new, cons(old, cdr(lat)))
    else:
        return cons(car(lat), insertL(new, old, cdr(lat)))

# insert new atom into lat, to the right of first occurance of old
def insertR(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(old, cons(new, cdr(lat)))
    else:
        return cons(car(lat), insertR(new, old, cdr(lat)))

# replace first occurance of old in lat with new
def subst(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(new, cdr(lat))
    else:
        return cons(car(lat), subst(new, old, cdr(lat)))

# replace first occurance of o1 or 2 in lat with new
def subst2(new, o1, o2, lat):
    if null(lat):
        return []
    elif car(lat) == o1:
        return cons(new, cdr(lat))
    elif car(lat) == o2:
        return cons(new, cdr(lat))
    else:
        return cons(car(lat), subst2(new, o1, o2, cdr(lat)))

# remove all occurances of a from lat
def multirember(a, lat):
    if null(lat):
        return []
    elif car(lat) == a:
        return multirember(a, cdr(lat))
    else:
        return cons(car(lat), multirember(a, cdr(lat)))

# insert new atom into lat, to the left of all occurances of old
def multiinsertL(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(new, cons(old, multiinsertL(new, old, cdr(lat))))
    else:
        return cons(car(lat), multiinsertL(new, old, cdr(lat)))

# insert new atom into lat, to the right of all occurances of old
def multiinsertR(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(car(lat), cons(new, multiinsertR(new, old, cdr(lat))))
    else:
        return cons(car(lat), multiinsertR(new, old, cdr(lat)))

# replace all occurances of old in lat with new
def multisubst(new, old, lat):
    if null(lat):
        return []
    elif car(lat) == old:
        return cons(new, multisubst(new, old, cdr(lat)))
    else:
        return cons(car(lat), multisubst(new, old ,cdr(lat)))




