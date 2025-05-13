def calc1(a, b):
    return a + b


def calc_and_print(a, b, calc_fun):
    c = calc_fun(a, b)
    print(c)


calc_and_print(1, 2, calc1)
