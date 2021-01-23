# 1.长度超过8位
#
# 2.包括大小写字母.数字.其它符号,以上四种至少三种
#
# 3.不能有相同长度大于2的子串重复
# professional
# SHA256: 7d4a9f9515537f8c7e047300d909b57eec09f59a3a535af68896e1b00b1d20d2
# MD5: 5e676da829731bf25f0a438582f35e77
# enterprise
# SHA256: e61b6208ecafcbc0d44a5bec245c8029e6e905e324083557ab45a1a1c4c72e25
# MD5: db6811453c89297bab956f3bfd6e52c6
# enterprise linux
# SHA256: ecdf695f9e3dc64514f5f6c7de4036147376e981aef89a5bfe1975ff4272c264
# MD5: 31cd787c98f8cca2094e3b6fda22687b
import re

while True:
    score = 0
    s = input().strip()
    flag = False
    if s.strip() == '':
        break
    if len(s) < 9:
        print('NG')
        continue
    if re.findall(r'[a-z]', s):
        score += 1
    if re.findall(r'[A-Z]', s):
        score += 1
    if score >= 1 and re.findall(r'[0-9]', s):
        score += 1
    if score >= 2 and re.findall(r'[^A-Za-z0-9]', s):
        score += 1
    if score < 3:
        print('NG')
        continue
    for i in range(len(s) - 3):
        for j in range(i + 3, len(s) - 3):
            # print(s[i:i + 3], s[j:j + 3])
            if s[i:i + 3] == s[j:j + 3]:
                print('NG')
                flag = True
                break
        if flag:
            break
    if not flag:
        print('OK')
