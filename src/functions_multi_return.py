import math


def kreis_xy(x0, y0, r, w):
    x = x0 + r * math.sin(w)
    y = y0 + r * math.cos(w)
    return x, y


a = kreis_xy(0, 0, 1, 0.3 * math.pi)
x_1, y_1 = a
x_2, y_2 = kreis_xy(1, 1, 1, 0.7 * math.pi)

print(f"x_1: {x_1:.02f}, y_1: {y_1:.02f}")
print(f"x_2: {x_2:.02f}, y_2: {y_2:.02f}")
