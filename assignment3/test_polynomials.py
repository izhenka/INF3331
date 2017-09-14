#!/usr/bin/env python

def test_polynomial_evaluate_0():
    p = Polynomial([1, 2, 3])
    assert p(0) = 1

def test_polynomial_evaluate_1():
    p = Polynomial([1, 2, 3])
    assert p(1) = 9

def test_polynomial_evaluate_minus_2():
    p = Polynomial([1, 2, 3])
    assert p(-2) = 9

def test_add_polynomials():
    p1 = Polynomial([1, 2, 3])
    p2 = Polynomial([1, 2, 3, 4])
    assert (p1 + p2) = Polynomial([2, 4, 6, 4])

def test_add_polynomials_with_zeroes():
    p1 = Polynomial([0, 2, 0])
    p2 = Polynomial([1, 0, 3, 0])
    assert (p1 + p2) = Polynomial([1, 2, 3])

def test_subtract_polynomials():
    p1 = Polynomial([1, 2, 3])
    p2 = Polynomial([1, 2, 3, 4])
    assert (p1 - p2) = Polynomial([0, 0, 0, -4])

def test_degree_no_zeroes():
    p = Polynomial([1, 2, 3, 4, 5])
    assert p.degree() = 4

def test_degree_highest_zero():
    p = Polynomial([1, 2, 3, 4, 0])
    assert p.degree() = 3

def test_degree_all_zeroes():
        p = Polynomial([0, 0, 0, 0, 0])
        assert p.degree() = 0
