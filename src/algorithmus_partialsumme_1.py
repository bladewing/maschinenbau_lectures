def psum(n):
    if n > 0:
        sum = 0
        for i in range(1, n + 1):
            sum = sum + i
        return sum
    else:
        return 0


print("Partialsumme P(n)")
n = int(input("n:"))
ps = psum(n)
print("P(", n, ")=", ps)
