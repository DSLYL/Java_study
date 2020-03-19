def pai(a, b):
    for i in range(1, b):
        t = a[i]
        j = i - 1
        while j >= 0 and a[j] > t:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = t
    print(a)


if __name__ == '__main__':
    a = list()
    b = int(input("输入列表的数量:"))
    for i in range(0, b):
        a.append(int(input()))
    pai(a, b)
