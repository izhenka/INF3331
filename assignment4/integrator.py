def integrate (f, a, b, N):
    step = abs(b-a)/(N+1)
    sum = 0
    for index in range(1, N+2):
        sum += f(index*step)*step
    return sum

print(integrate(lambda x: x**2, 0, 1, 1E+5))
