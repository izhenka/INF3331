#!/usr/bin/env python
from polynomials import Polynomial

def test_polynomial_evaluate_0():
    p = Polynomial([1, 2, 3])
    assert p(0) == 1

def test_polynomial_evaluate_1():
    p = Polynomial([1, 2, 3])
    assert p(1) == 6

def test_polynomial_evaluate_minus_2():
    p = Polynomial([1, 2, 3])
    assert p(-2) == 9

def test_add_polynomials():
    p1 = Polynomial([1, 2, 3])
    p2 = Polynomial([1, 2, 3, 4])
    assert (p1 + p2) == Polynomial([2, 4, 6, 4])

def test_add_polynomials_with_zeroes():
    p1 = Polynomial([0, 2, 0])
    p2 = Polynomial([1, 0, 3, 0])
    assert (p1 + p2) == Polynomial([1, 2, 3])

def test_subtract_polynomials():
    p1 = Polynomial([1, 2, 3])
    p2 = Polynomial([1, 2, 3, 4])
    assert (p1 - p2) == Polynomial([0, 0, 0, -4])

def test_degree_no_zeroes():
    p = Polynomial([1, 2, 3, 4, 5])
    assert p.degree() == 4

def test_degree_highest_zero():
    p = Polynomial([1, 2, 3, 4, 0])
    assert p.degree() == 3

def test_degree_all_zeroes():
        p = Polynomial([0, 0, 0, 0, 0])
        assert p.degree() == -1

def test_repr_no_zeroes():
    p = Polynomial([1, 2, 3, 4, 5])
    assert str(p) == "5x^4 + 4x^3 + 3x^2 + 2x + 1 "

def test_repr_some_zeroes():
    p = Polynomial([0, 2, 0, 0, 5])
    assert str(p) == "5x^4 + 2x "

def test_repr_all_zeroes():
    p = Polynomial([0, 0, 0, 0, 0])
    assert str(p) == ""

def test_repr_negatives():
    p = Polynomial([-1, 2, -3, 4, -5])
    assert str(p) == "- 5x^4 + 4x^3 - 3x^2 + 2x - 1 "

def test_repr_ones():
    p = Polynomial([1, 1, 1])
    assert str(p) == "x^2 + x + 1 "


def test_eq():
    p1 = Polynomial([1, 0, 1, 0, 0, 0])
    p2 = Polynomial([1, 0, 1, 0])
    assert p1 == p2

def test_multiply():
    p = Polynomial([1, 0, 3])
    assert p*2 == Polynomial([2, 0, 6])


test_degree_no_zeroes()
test_degree_highest_zero()
test_degree_all_zeroes()
test_repr_no_zeroes()
test_repr_negatives()
test_repr_some_zeroes()
test_repr_all_zeroes()
test_repr_ones()
test_polynomial_evaluate_0()
test_polynomial_evaluate_1()
test_polynomial_evaluate_minus_2()
test_add_polynomials()
test_add_polynomials_with_zeroes()
test_subtract_polynomials()
test_eq()
test_multiply()
print("All tests are passed!")
