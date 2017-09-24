import matplotlib.pyplot as plt
import seaborn

def integrate (f, a, b, N):
    step = abs(b-a)/(N+1)
    sum = 0
    for index in range(1, N+2):
        sum += f(index*step)*step
    return sum

def plotError():
    x = [1, 2, 4 , 10, 20, 40, 100, 200, 400]
    func = lambda i: abs(integrate(lambda z: z**2, 0, 1, i) - 1/3)
    y = list(map(func, x))

    plt.plot(x, y,
    label="Quadratic error as a function of the N number of points")
    plt.xlabel("Number points")
    plt.ylabel("Error")
    plt.legend()
    plt.show()


plotError()
