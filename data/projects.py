from model.project import Project
import random
import string


def var_or_fixed(maxlen, fixedlen):
    if fixedlen:
        return maxlen
    else:
        return random.randrange(maxlen)


def random_string(prefix, maxlen, fixedlen=False, punctuation=False, spaces=True):
    symbols = string.ascii_letters + string.digits
    if punctuation:
        symbols = symbols + string.punctuation
    if spaces:
        symbols = symbols + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(var_or_fixed(maxlen, fixedlen))])


def random_status():
    status_list = ("development", "release", "stable", "obsolete")
    return random.choice(status_list)


def random_inherit_global():
    inherit_global_list = (True, False)
    return random.choice(inherit_global_list)


def random_view_status():
    view_state_list = ("public", "private")
    return random.choice(view_state_list)


testdata = [Project(name=random_string("Proj_", 15),
                    status=random_status(),
                    inherit_global=random_inherit_global(),
                    view_status=random_view_status(),
                    description=random_string("Desc_", 30))
            for i in range(5)]

# for project in testdata:
#    print(project)

