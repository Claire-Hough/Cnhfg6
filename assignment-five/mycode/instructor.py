assignment_list = ['Resume', 'Pytest']

def add_instructor( fname, lname, usertype ):
    return usertype == 'instructor'


def create_assignment( title, description ):
    if (title in assignment_list):
        return False
    else:
        return True