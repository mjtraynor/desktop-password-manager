import keychain_functions as kf

def main():
    system = input('Please enter the system name: ')
    username = input('Please enter the username: ')
    
    kf.set_pswrd(system, username)

if __name__ == main():
    main()