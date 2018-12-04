import re


def count_patt(fname, patt):
    cpatt=re.compile(patt)
    ip_dict = {}
    with open(fname) as fobj:
        for line in fobj:
            ip = cpatt.search(line)  #如果匹配不到 返回None
            if ip:
                key = ip.group()
                ip_dict[key] = ip_dict.get(key,0) + 1
                #dict.get(key,0) 设置没找到不返回None  返回0

                # if not ip_dict.get(key):
                #     ip_dict[key] = 1
                # else:
                #     ip_dict[key] += 1
    return ip_dict


if __name__ == '__main__':
    fname = '/opt/access_log'
    ip = '^\d+(\.\d+){3}'
    print(count_patt(fname, ip))

    br = 'Firefox|MSIE|Chrome'
    print(count_patt(fname,br))
