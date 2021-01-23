import re


error_list = []
while True:
    a = input()
    if a.strip() == '':
        break
    error = re.match(r'.*?(\w{1,16}\s\d+)', a.split('\\')[-1]).group(1)
    if error not in [i[0] for i in error_list]:
        error_list.append([error, 1])
    else:
        for i in error_list:
            if i[0] == error:
                i[1] += 1
                break
for i in error_list[-8:]:
    print('%s %d' % (i[0], i[1]))
