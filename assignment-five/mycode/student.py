sid_list = [48302853, 10843184, 49382932]


def upload(filename, filetype):
    return filetype == '.zip' or filetype == '.py'


def remove_student(sid):
    if (sid in sid_list):
        return True
    else:
        return False
