import getpass

user_dirct = {}


def register():
    new_name = input('New name:')
    if new_name in user_dirct:
        print('%s already exists' % new_name)
    else:
        password = input('Password:')
        user_dirct[new_name] = password
        print('Username: %s register successfully.' % new_name)


def login():
    for i in range(3):
        username = input('Username:')
        password = getpass.getpass('Password:')
        if user_dirct.get(username) != password:
            print('Login failed.')
        else:
            print('login successfully.')
            break


def show_menu():
    cmds = {'0': register, '1': login}
    prompt = '''(0) register
(1) login
(2) exit
Please input ypur chioce(0/1/2):'''
    while True:
        chioce = input(prompt).strip()[0]
        if chioce not in '012':
            print('Invalid input. Please try again.')
            continue
        if chioce == '2':
            break
        cmds[chioce]()


if __name__ == '__main__':
    show_menu()
