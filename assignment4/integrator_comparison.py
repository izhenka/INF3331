from integrator import *
from numba_integrator import *
from numpy_integrator import *
import math
import numpy as np

answer = 2

N=1E+5
print("=======Endpoint:=======")
result_integrator = integrate(math.sin, 0, math.pi, N)
result_numpy = numpy_integrate(np.sin, 0, math.pi, N)

print("result_integrator: {}\n result_numpy: {}".format(result_integrator, result_numpy))
print("""Difference:
integrator:{}
numpy:{}""".format(abs(answer - result_integrator), abs(answer - result_numpy)))

print("=======Midpoint:=======")
result_mp_integrator = midpoint_integrate(math.sin, 0, math.pi, N)
result_mp_numpy = numpy_midpoint_integrate(np.sin, 0, math.pi, N)

print("result_integrator: {}\n result_numpy: {}".format(result_mp_integrator, result_mp_numpy))
print("""Difference:
integrator:{}
numpy:{}""".format(abs(answer - result_mp_integrator), abs(answer - result_mp_numpy)))
