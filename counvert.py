import os

class Counvert:
    def __init__(self,fname):
        self.fname = fname

    def to_linux(self):
        dest_fname=os.path.splitext(self.fname)[0] + '.linux'
        #os.path.splitext('/root/test.txt')  -> ('/root/test','.txt')
        with open(self.fname,'r') as sobj:
            with open(dest_fname,'w') as dobj:
                data = sobj.readlines()
                for line in data:
                    line = line.strip('\t\n')+'\n'
                    dobj.write(line)

    def to_windows(self):
        dest_fname = os.path.splitext(self.fname)[0] + '.windows'
        with open(self.fname,'r') as sobj:
            with open(dest_fname,'w') as dobj:
                data = sobj.readlines()
                for line in data:
                    line = line.strip('\t\n')+'\t\n'
                    dobj.write(line)

if __name__ == '__main__':
    c = Counvert('/opt/hosts')
    c.to_linux()
    c.to_windows()