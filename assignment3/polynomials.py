class Polynomial:

    def __init__(self, coefficients):
        """coefficients should be a list of numbers with
        the i-th element being the coefficient a_i."""

        self.coefficients = coefficients

    def degree(self):
        """Return the index of the highest nonzero coefficient.
        If there is no nonzero coefficient, return -1."""

        for index in reversed(range(len(self.coefficients))):
            if self.coefficients[index] != 0:
                return index

        return -1;


    def coefficients(self):
        """Return the list of coefficients.

        The i-th element of the list should be a_i, meaning that the last
        element of the list is the coefficient of the highest degree term."""
        return self.coefficients

    def __call__(self, x):
        """Return the value of the polynomial evaluated at the number x"""
        result = 0;
        for index in range(len(self.coefficients)):
            result+= self.coefficients[index]*(x**index)

        return result;

    def __add__(self, p):
        """Return the polynomial which is the sum of p and this polynomial
        Should assume p is Polynomial([p]) if p is int.

        If p is not an int or Polynomial, should raise ArithmeticError."""

        raise NotImplemented

    def __sub__(self, p):
        """Return the polynomial which is the difference of p and this polynomial
        Should assume p is Polynomial([p]) if p is int.

        If p is not an int or Polynomial, should raise ArithmeticError."""

        raise NotImplemented

    def __mul__(self, c):
        """Return the polynomial which is this polynomial multiplied by given integer.
        Should raise ArithmeticError if c is not an int."""

        raise NotImplemented


    def __rmul__(self, c):
        """Return the polynomial which is this polynomial multiplied by some integer"""

        raise NotImplemented

    def __repr__(self):
        """Return a nice string representation of polynomial.

        E.g.: x^6 - 5x^3 + 2x^2 + x - 1
        """
        result = ""
        length = len(self.coefficients);
        for index in reversed(range(length)):
            value = self.coefficients[index];
            if value==0:
                continue

            if value>0:
                sign = ("+ " if index!=length-1 else "")
            else:
                sign = "- "

            value = abs(value)
            value = value if value!=1 or index==0 else ""

            degree = ("^{}".format(index) if index>1 else "")
            x = ("x" if index!=0 else "")

            result+= sign + str(value) + x + degree + " "

        return result



    def __eq__(self, p):
        """Check if two polynomials have the same coefficients."""

        raise NotImplemented

def sample_usage():
    p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
    q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3


    print("The value of {} at {} is {}".format(p, 7, p(7)))

    print("The coefficients of {} are {}".format(p, p.coefficients()))


    print("\nAdding {} and {} yields {}".format(p, q, p+q))

    p, q, r = map(Polynomial,
                  [
                      [1, 0, 1], [0, 2, 0], [1, 2, 1]
                  ]
    )

    print("\nWill adding {} and {} be the same as {}? Answer: {}".format(
        p, q, r, p+q == r
    ))
    print("\nIs {} - {} the same as {}? Answer: {}".format(
        p, q, r, p-q == r
    ))
