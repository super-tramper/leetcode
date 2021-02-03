def generic_dict():
    code_dict = {chr(i): (i - 7) % 9 + 1for i in range(97, 123)}
    print(code_dict)


code_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9, 's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8}


def verifyInvitationCode(code):
    sumn = 0
    for i, v in enumerate(code[::-1]):
        if i % 2 == 0:
            if v.isdigit():
                sumn += int(v)
            else:
                sumn += code_dict[v]
        else:
            if v.isdigit():
                sumn += int(v)*2
            else:
                sumn += code_dict[v]*2
    if sumn % 10:
        return 'error'
    else:
        return 'ok'


if __name__ == '__main__':
    code = '123456789qwertyu'
    print(verifyInvitationCode(code))
    # generic_dict()
