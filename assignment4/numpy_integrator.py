import numpy as np
def numpy_integrate (f, a, b, N):
    (x, step) = np.linspace(a, b, N+2, retstep=True) # +2 endpoints
    # print("x {}, step {}".format(x, step))
    # print(np.vectorize(f)(x[1:]))
    return np.sum(np.vectorize(f)(x[1:])*step)


if __name__ == '__main__':
    numpy_integrate(lambda x: x*2, 0, 1, 1)
