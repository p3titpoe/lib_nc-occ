import sys


if __name__ == "__main__":
    from lib_occ.logic import UserReg
    from getpass import getuser

    user = getuser()

    UserReg.set_user('www-data')
    sys.exit()