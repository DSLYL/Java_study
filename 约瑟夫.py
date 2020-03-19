def j(n, k):
    l = list(range(1, n + 1))
    ind = 0
    print('The failer is')
    for loop_i in range(n - 1):
        ind = (ind + k) % len(l)
        ind -= 1
        print(l[ind], end=" ")
        del l[ind]
        if ind == -1:
            ind = 0
    print()
    print('The winner is :', l[0])


if __name__ == '__main__':
    j(101, 12)
