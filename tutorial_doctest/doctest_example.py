# What's a doctest?
# A doctest is a piece of text that look like interactive Python sessions, and is then executed to verify that they work exactly as shown.
#
# There are several common ways to use doctest:
#
# To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
# To write tutorial documentation for a package, liberally illustrated with input-output examples. (as shown in the tutorial_doctest.txt)


def example(a: float, b: float) -> float:
    return a - b


# adding doctest
def doctest_example(a: float, b: float) -> float:
    """
    Doctest Example

    >>> doctest_example(5, 2)
    3
    >>> doctest_example('a', 1)
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for -: 'str' and 'int'

    :param a:
    :param b:
    :return:
    """
    return a - b


if __name__ == '__main__':
    import doctest
    doctest.testfile('tutorial_doctest.txt')
