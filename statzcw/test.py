import unittest

import statzcw.stats


class MyTestCase(unittest.TestCase):
    def test_zcount(self):

        a = (1, 2, 3, 4, 5)
        expected = 5
        actual =statzcw.stats.zcount(a)
        self.assertEqual(expected, actual)  # add assertion here







if __name__ == '__main__':
    unittest.main()
