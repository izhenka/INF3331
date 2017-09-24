#!/usr/bin/env python
from integrator import integrate

def test_integral_of_constant_function():
    f = lambda x: 2;
    answer1 = integrate(f, 0, 1, N=1)
    answer2 = integrate(f, 0, 1, N=1000)
    expected_answer = 2
    print ("test_integral_of_constant_function N=1:{}, N=1000:{}\nexpected:{}".format(answer1, answer2, expected_answer))
    assert answer1 == expected_answer
    assert abs(answer2 - expected_answer) < 1E-10
    print("ok")

def test_integral_of_linear_function():
    f = lambda x: 2 * x;
    answer1 = integrate(f, 0, 1, N=10)
    answer2 = integrate(f, 0, 1, N=10000)
    expected_answer = 1
    print ("test_integral_of_linear_function N=10:{}, N=10000:{}\nexpected:{}".format(answer1, answer2, expected_answer))
    assert abs(answer1 - expected_answer) <= 1E-1
    assert abs(answer2 - expected_answer) <= 1E-4
    print("ok")

test_integral_of_constant_function()
test_integral_of_linear_function()
