import math


def fun1(x):
    return ...  # Berechnung


x0_1 = nullstellensuche(0, 5, fun1)


def nullstellensuche(a, b, f):
    if f(a) * f(b) > 0:
        return  # none, keine Nullstelle
    m = (a + b) / 2
    ya = f(a)
    ym = f(m)
    while abs(ym) > 1e-7:
        if ya * ym < 0:  # NST links
            b = m
        else:  # NST rechts
            a = m
        m = (a + b) / 2
        ya = f(a)
        ym = f(m)
    return m


x0 = nullstellensuche(0, 5, lambda x: math.cos(x / 3))


def fun2(x):
    return math.cos(x / 3)


x0 = nullstellensuche(0, 5, fun2)
