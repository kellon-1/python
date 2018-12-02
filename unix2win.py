import sys


def unix2win(fname):
    dname = fname + '.txt'
    with open(fname) as sobj:
        with open(dname, 'w') as dobj:
            for line in sobj:
                line = line.rstrip('\r\n') + '\r\n'
                dobj.write(line)


if __name__ == '__main__':
    unix2win(sys.argv[1])
