import datetime

def validator_name(name):
    if name.replace(" ", "").isalpha() and name[0].isupper() and len(name) > 2:
        return True
    return False


def validator_stime(stime):
    if str(stime[0:10:]) > str(datetime.datetime.utcnow())[0:10:]:
        return True
    return False


def validator_etime(stime, etime):
    if str(stime[0:10:]) > str(etime[0:10:]):
        return False
    else:
        st1 = str(stime)[11:13]
        st2 = str(etime)[11:13]
        if int(st2) - int(st1) < 1:
            return False
    return True
