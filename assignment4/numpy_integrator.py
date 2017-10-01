import numpy as np
import time

def numpy_integrate (f, a, b, N):
    (x, step) = np.linspace(a, b, N+2, retstep=True) # +2 endpoints
    # f = np.vectorize(f) takes a lot of time
    return np.sum(f(x[1:]))*step

def numpy_midpoint_integrate(f, a, b, N):
    (x, step) = np.linspace(a, b, N+2, retstep=True) # +2 endpoints
    x = x - step/2
    return np.sum(f(x[1:]))*step


if __name__ == '__main__':
    t0 = time.clock()
    result = numpy_integrate(lambda x: x**2, 0, 1, N=1E+6)
    t1 = time.clock()

    print('{:.4f} sec'.format(t1-t0))

    result_midpoint = numpy_midpoint_integrate(lambda x: x**2, 0, 1, N=1E+6)
    print("result:{}, result_midpoint:{}".format(result, result_midpoint))
