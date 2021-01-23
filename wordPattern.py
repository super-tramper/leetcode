def wordPattern(pattern: str, s: str) -> bool:
    d = {}
    if len(pattern) != len(s.split()):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in d:
            d[pattern[i]] = s.split()[i]
        else:
            if d[pattern[i]] != s.split()[i]:
                return False
    if len(set(d.values())) != len(d):
        return False
    return True


def wordPattern2(pattern: str, s: str) -> bool:
    s1 = s.split(' ')
    if len(pattern) != len(s1):
        return False
    return len(set(zip(list(pattern), s1))) == len(set(s1)) == len(set(pattern))



if __name__ == '__main__':
    print(wordPattern(pattern="abba", s="dog dog dog dog"))
