class Polynomial:

    def __init__(self, coefficients):
        """coefficients should be a list of numbers with
        the i-th element being the coefficient a_i."""

        self.coefficients = withoutLeadZeroes(coefficients)


    def degree(self):
        """Return the index of the highest nonzero coefficient.
        If there is no nonzero coefficient, return -1."""

        for index in reversed(range(len(self.coefficients))):
            if self.coefficients[index] != 0:
                return index

        return -1


    def getCoefficients(self):
        """Return the list of coefficients.

        The i-th element of the list should be a_i, meaning that the last
        element of the list is the coefficient of the highest degree term."""
        return self.coefficients

    def __call__(self, x):
        """Return the value of the polynomial evaluated at the number x"""
        result = 0;
        for index in range(len(self.coefficients)):
            result+= self.coefficients[index]*(x**index)

        return result

    def __add__(self, p):
        """Return the polynomial which is the sum of p and this polynomial
        Should assume p is Polynomial([p]) if p is int.

        If p is not an int or Polynomial, should raise ArithmeticError."""
        if isinstance(p, int):
            return (self+[p])
        elif isinstance(p, Polynomial):
            coefficients =[]
            len_self = len(self.coefficients)
            len_p = len(p.coefficients)
            max_len = max(len_self, len_p)
            for index in range(max_len):
                val_self = self.coefficients[index] if index<len_self else 0
                var_p = p.coefficients[index] if index<len_p else 0
                coefficients.append(val_self+var_p)
            return Polynomial(coefficients)
        else:
            raise ArithmeticError


    def __sub__(self, p):
        """Return the polynomial which is the difference of p and this polynomial
        Should assume p is Polynomial([p]) if p is int.

        If p is not an int or Polynomial, should raise ArithmeticError."""
        if isinstance(p, int):
            return (self-p)
        elif isinstance(p, Polynomial):
            coefficients =[]
            len_self = len(self.coefficients)
            len_p = len(p.coefficients)
            max_len = max(len_self, len_p)
            for index in range(max_len):
                val_self = self.coefficients[index] if index<len_self else 0
                var_p = p.coefficients[index] if index<len_p else 0
                coefficients.append(val_self-var_p)
            return Polynomial(coefficients)
        else:
            raise ArithmeticError

    def __mul__(self, c):
        """Return the polynomial which is this polynomial multiplied by given integer.
        Should raise ArithmeticError if c is not an int."""
        if isinstance(c, int):
            return Polynomial([x * c for x in self.coefficients])
        else:
            raise ArithmeticError


    def __rmul__(self, c):
        """Return the polynomial which is this polynomial multiplied by some integer"""
        return self*c

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
        if type(self)!=type(p):
            return False

        if len(self.coefficients)!=len(p.coefficients):
            return False

        for index in range(len(self.coefficients)):
            if self.coefficients[index]!=p.coefficients[index]:
                return False

        return True

def withoutLeadZeroes(array):
    """cuts all zero-values on the end of array"""
    index_until = len(array)
    for value in reversed(array):
        if value==0:
            index_until-=1
        else:
            break
    return array[:index_until]

def sample_usage():
    p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
    q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3


    print("The value of {} at {} is {}".format(p, 7, p(7)))

    print("The coefficients of {} are {}".format(p, p.getCoefficients()))


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

sample_usage()
