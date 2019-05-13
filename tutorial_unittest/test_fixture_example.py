# The unittest unit testing framework was originally inspired by JUnit - hence the naming convention used below.
from unittest import TestCase, main


class SetupTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setting up class...\n')

    @classmethod
    def tearDownClass(cls):
        """
        If an exception is raised during a setUpClass then the tests in the class are not run and
        the tearDownClass is not run.

        :return:
        """
        print('Tearing down class...')

    def setUp(self):
        """
        The testing framework will automatically call this function before every single test we run.
        :return:
        """
        self.phrase = "I'm setting up..."
        print(self.phrase)

    def tearDown(self):
        """
        The testing framework will automatically call this function after every single test we run.
        If setUp() succeeded, tearDown() will be run whether the test method succeeded or not.

        :return:
        """
        self.phrase = "I'm tearing down..."
        print(self.phrase)

    def test_example(self):
        print('Running `test_example`...')
        self.assertEqual("I'm setting up...", self.phrase)
        print('Exiting `test_example`...')

    def test_another_example(self):
        print('Running `test_another_example`...')
        self.assertEqual("I'm setting up...", self.phrase)
        print('Exiting `test_another_example`...')

    def prefix_example(self):
        """
        This test is automatically skipped since it doesn't have the 'test' prefix.

        :return:
        """
        print('Running `prefix_example`')
        self.assertEqual(1, False)
        print('Exiting `prefix_example`')


if __name__ == '__main__':
    main()
