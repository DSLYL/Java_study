def s(list):
    if len(list) == 0:
        return [list]
    else:
        s1 = []
        s2 = s(list[1:])
        for i in s2:
            s1.append([list[0]] + i)
        return s1 + s2


if __name__ == '__main__':
    print(s([1, 2, 3]))
