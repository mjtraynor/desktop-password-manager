from getpass import getpass
from keyring import set_password, get_credential, delete_password
from keyring.errors import PasswordDeleteError

def set_pswrd(system, username):
    password = getpass()
    
    set_password(system, username, password)

def get_greds(system, username):
    creds = get_credential(system, username)

    key_password = creds.password

    return key_password

def del_pswrd(system, username):
    del_check = input('Are you sure you want to delete these credentials? [y/n] ').lower()

    if del_check == 'y':
        try:
            delete_password(system, username)
            text = 'The credentials have been deleted.'
        except PasswordDeleteError:
            text = 'The credentials do not exist.'
    else:
        text = 'The credentials were not deleted.'

    print(text)