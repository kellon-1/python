import hashlib

# def check_md5(fname):
#     m = hashlib.md5()
#     with open(fname, 'rb') as fobj:
#         while True:
#             data = fobj.read(4096)
#             if not data:
#                 break
#             m.update(data)
#     return m.hexdigest()

def check(fname):
    m = hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()
print(check('/etc/hosts'))
