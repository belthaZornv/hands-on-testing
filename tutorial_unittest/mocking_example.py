from unittest import TestCase, main, mock
from random import randint


def rand_calc():
    # dynamic, not deterministic
    num = randint(1, 2000)

    if num < 100:
        return True

    return False


class MockTestCase(TestCase):
    @mock.patch('mocking_example.randint', return_value=99)
    def test_rand_calc_success(self, randint_mock: mock.Mock):
        self.assertEqual(rand_calc(), True)
        randint_mock.assert_called_once_with(1, 2000)

    @mock.patch('mocking_example.randint', return_value=100)
    def test_rand_calc_false_success(self, randint_mock: mock.Mock):
        self.assertEqual(rand_calc(), False)
        randint_mock.assert_called_once_with(1, 2000)

    def test_rand_calc_type_failure(self):
        with self.assertRaises(TypeError):
            rand_calc('hello')


if __name__ == '__main__':
    main()
