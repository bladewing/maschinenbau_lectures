def calc1(a, b):
    return a + b


def calc2(x, y):
    return (x + y) / 2


def calc3(r, s):
    return max(r, s)


def map_auf_listen(li1, li2, li3, fun):
    for i in range(0, len(li1)):
        li3[i] = fun(li1[i], li2[i])  # elementweiser Aufruf


L1 = [1, 2, 3, 7]
L2 = [10, 8, 6, 4]
L3 = [0, 0, 0, 0]

map_auf_listen(L1, L2, L3, calc3)
