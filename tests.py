import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "Hello World"
        self.assertEqual(task.my_func(), expected)


if __name__ == '__main__':
    unittest.main()
