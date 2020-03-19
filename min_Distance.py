import math
import random


def creat():
    ball = []
    allnum = int(input('请输入生成点的数量：'))

    for i in range(allnum):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        ball.append([x, y])
    return ball


def merge(ball, start, mid, end):
    temp = []
    i = start
    j = mid + 1
    while i < mid + 1 and j < end + 1:
        if ball[i][0] > ball[j][0]:
            temp.append(ball[j])
            j = j + 1
        else:
            temp.append(ball[i])
            i = i + 1
    while i < mid + 1:
        temp.append(ball[i])
        i = i + 1
    while j < end + 1:
        temp.append(ball[j])
        j = j + 1
    ball[start:end + 1] = temp


def merge_sort(ball, start, end):
    if start < end:
        mid = start + (end - start) // 2
        merge_sort(ball, start, mid)
        merge_sort(ball, mid + 1, end)
        merge(ball, start, mid, end)


def distance(p1, p2):
    x = math.fabs(p1[0] - p2[0])
    y = math.fabs(p1[1] - p2[1])
    return math.sqrt(x * x + y * y)


def get_closest_distance(ball, l, r):
    if r <= l:
        return [0, 0, 65535]
    if r - l == 1:
        return [l, r, distance(ball[l], ball[r])]
    if r - l == 2:
        d1 = distance(ball[l], ball[l + 1])
        d2 = distance(ball[l + 1], ball[r])
        d3 = distance(ball[l], ball[r])
        if d1 <= d2 and d1 <= d3:
            return [l, l + 1, d1]
        elif d2 <= d1 and d2 <= d3:
            return [l + 1, r, d2]
        else:
            return [l, r, d3]

    m = l + (r - l) // 2
    result1 = get_closest_distance(ball, l, m)
    result2 = get_closest_distance(ball, m + 1, r)
    d = min(result1[2], result2[2])

    i = m
    j = m
    while i >= l:
        if ball[m][0] - ball[i][0] < d:
            i -= 1
        else:
            break
    while j <= r:
        if ball[j][0] - ball[m][0] < d:
            j += 1
        else:
            break
    if i < m:
        i += 1
    result3 = [0, 0, 65535]
    for a in range(i, m + 1):
        for b in range(m + 1, j):
            d0 = distance(ball[a], ball[b])
            if d0 < result3[2]:
                result3 = [a, b, d0]
    if result1[2] <= result2[2] and result1[2] <= result3[2]:
        return result1
    elif result2[2] <= result1[2] and result2[2] <= result3[2]:
        return result2
    else:
        return result3


p = creat()
print("随机生成点：")
print(p)
merge_sort(p, 0, len(p) - 1)
result = get_closest_distance(p, 0, len(p) - 1)
print("最近的两个点：" + str(p[result[0]]) + ", " + str(p[result[1]]))
print("距离为:" + str(result[2]))
