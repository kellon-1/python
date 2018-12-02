import sys, keyword, string

first_chars = string.ascii_letters + '_'
all_chars = first_chars + string.digits


def check_id(idt):
    if keyword.iskeyword(idt):
        return '%s is keyword' % idt
    if idt[0] not in first_chars:
        return '1st is invalid'
    err_ind=[]
    for ind in range(1,len(idt)):
        if idt[ind] not in all_chars:
            err_ind.append(ind+1)
    if err_ind:
        return "char in postion #%s is invalid"%err_ind
    else:
        return "%s is valid"%(idt)
if __name__ == '__main__':
    print(check_id(sys.argv[1]))
