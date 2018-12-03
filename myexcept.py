def myage1(name,age):
    if not 0< age <120:
        raise ValueError('%s out of range(0,120)'%age)

def myage2(name,age):
    assert 0< age < 120 ,"%s out of range(0,120)"%age
    print('%s age is %s'%(name,age))



if __name__ == '__main__':
    myage1('kellon',999)
    myage2('molly',888)