#!/usr/bin/env python

def test_integral_of_constant_function():
    f = lambda x: 2;
    answer1 = integrate(f, 0, 1, N=1)
    answer20 = integrate(f, 0, 1, N=20)
    assert answer1 == 2
    assert answer20 == 2

def test_integral_of_constant_function():
    f = lambda x: 2 * x;
    answer10 = integrate(f, 0, 1, N=10)
    answer100 = integrate(f, 0, 1, N=100)
    expected_answer = 1
    assert abs(answer10 - expected_answer) <= 1/10
    assert abs(answer100 - expected_answer) <= 1/100
