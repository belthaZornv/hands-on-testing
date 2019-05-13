from unittest import TestCase, main
import warnings


class AssertionsTestCase(TestCase):
    def test_example(self):
        """
        The expected value is usually placed on the left hand side.

        :return:
        """
        self.assertEqual(1, True)
        self.assertDictEqual({"hello": 1}, {"hello": 1})
        self.assertFalse(False)
        self.assertTrue(True)
        self.assertIsInstance(TestCase, object)
        self.assertIn(1, [1, 2, 3, 4, 5])
        self.assertRaises(KeyError, self.exception)
        self.assertWarns(DeprecationWarning, self.warning)

        with self.assertRaises(KeyError) as exc:
            # do something here
            self.exception()

        # you can use `exc` from the context above here.

    def exception(self):
        raise KeyError

    def warning(self):
        warnings.warn("deprecated", DeprecationWarning)


if __name__ == '__main__':
    main()
