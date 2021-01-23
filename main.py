import re


def main(stdin):
    ret_list = []
    location = [0,0]
    for i in stdin.split(';'):
        ret = re.match(r'[ASDW]\d\d?', i)
        if ret:
            ret_list.append(ret.group())
    for i in ret_list:
        if i[0] == 'A':
            location[0] -= int(i[1:])
        elif i[0] == 'S':
            location[1] -= int(i[1:])
        elif i[0] == 'D':
            location[1] += int(i[1:])
        elif i[0] == 'W':
            location[0] += int(i[1:])
    return location[0], location[1]