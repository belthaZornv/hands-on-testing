from unittest import TestLoader, TextTestRunner


def run_by_prefix():
    """
    Run tests by different prefix.

    This example is added to give more insight into the importance of using the 'test' prefix.
    :return:
    """
    loader = TestLoader()
    loader.testMethodPrefix = "prefix_"
    tests = loader.discover("tutorial_unittest")

    runner = TextTestRunner()
    runner.run(tests)


if __name__ == '__main__':
    run_by_prefix()
