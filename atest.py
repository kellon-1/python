with open('city_code_hefeng.txt') as fobj:
    data = fobj.readlines()
    a = 1
    for line in data:
        d = line.split(',')
        print(d[0],d[2])
        a+=1
        if a == 4:
            break