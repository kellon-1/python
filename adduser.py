import subprocess, sys
from randpass import choice_pass


def adduser(username, password, fname):
    subprocess.call('useradd %s' % username, shell=True)
    subprocess.call(
        'echo %s | passwd --stdin %s' % (password, username), shell=True
    )
    with open(fname, 'a') as fobj:
        fobj.write("user information: %s  %s" % (username, password))


if __name__ == '__main__':
    username = sys.argv[1]
    password = choice_pass()
    adduser(username, password, '/opt/user.txt')
