from unittest import TestSuite, TextTestRunner

from tutorial_unittest.test_fixture_example import SetupTestCase


def suite():
    suite = TestSuite()

    suite.addTest(SetupTestCase('test_example'))

    return suite


if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(suite())
