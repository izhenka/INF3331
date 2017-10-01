import time
from numba import jit

@jit
def f(x):
    return x**2

@jit(nopython=True)
def numba_integrate (a, b, N):
    N = int(N)
    step = abs(b-a)/(N+1)
    sum = 0
    for index in range(1, N+2):
        sum += f(a+index*step)
    return sum*step

if __name__ == '__main__':
    t0 = time.clock()
    # numba_integrate(lambda x: x**2, 0, 1, N=1E+7)
    numba_integrate(0, 1, N=1E+7)
    t1 = time.clock()

    print('numba {:.4f} sec'.format(t1-t0))
