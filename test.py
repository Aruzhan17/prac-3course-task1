import unittest
import numpy as np
from nash import nash_equilibrium, find_negative_min


class TestNash(unittest.TestCase):
    def test_1(self):
        A = np.array([[8, 7, 0, 6],
                      [6, 8, 5, 10]])
        p = np.array([0, 1], dtype=np.float64)
        q = np.array([0, 0, 1, 0], dtype=np.float64)
        val = 5

        res = nash_equilibrium(A)

        self.assertEqual(res[0], val)
        assert(np.sum(np.abs(res[1] - p)) < 0.001 )
        assert(np.sum(np.abs(res[2] - q)) < 0.001 )

    def test_2(self):
        A = np.array([[4, 0, 6, 2, 2, 1],
                      [3, 8, 4, 10, 4, 4],
                      [1, 2, 6, 5, 0, 0],
                      [6, 6, 4, 4, 10, 3],
                      [10, 4, 6, 4, 0, 9],
                      [10, 7, 0, 7, 9, 8]])
        p = np.array([0, 4/31, 3/31, 27/62, 21/62, 0], dtype=np.float64)
        q = np.array([0, 0, 257/372, 9/62, 55/372, 1/62], dtype=np.float64)
        val = 151/31

        res = nash_equilibrium(A)

        assert(res[0] == val)
        assert(np.sum(np.abs(res[1] - p)) < 0.001)
        assert(np.sum(np.abs(res[2] - q)) < 0.001)

    def test_3(self):
        A = np.array([[0, 1, -1],
                       [-1, 0, 1],
                       [1, -1, 0]])
        p = np.array([1/3, 1/3, 1/3], dtype=np.float64)
        q = np.array([1/3, 1/3, 1/3], dtype=np.float64)
        val = 0

        res = nash_equilibrium(A)

        assert(res[0] == val)
        assert(np.sum(np.abs(res[1] - p)) < 0.001)
        assert(np.sum(np.abs(res[2] - q)) < 0.001)

    def test_4(self):
        A = np.array([[0, 1, -1],
                       [-1, 0, 1],
                       [1, -1, 0]])
        p = np.array([1/3, 1/3, 1/3], dtype=np.float64)
        q = np.array([1/3, 1/3, 1/3], dtype=np.float64)
        val = 0

        res = nash_equilibrium(A)

        assert(res[0] == val)
        assert(np.sum(np.abs(res[1] - p)) < 0.001)
        assert(np.sum(np.abs(res[2] - q)) < 0.001)

    def test_3(self):
        A = np.array([[0, 0, 0, 0, 1, -1, 0],
                       [0, 0, 1, 0, 0, 0, -1],
                       [0, -1, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0],
                       [-1, 0, 0, 0, 0, 1, 0],
                       [1, 0, 0, 0, -1, 0, 0],
                       [0, 1, -1, 0, 0, 0, 0]])
        p = np.array([0, 1/3, 1/3, 0, 0, 0, 1/3], dtype=np.float64)
        q = np.array([0, 1/3, 1/3, 0, 0, 0, 1/3], dtype=np.float64)
        val = 0

        res = nash_equilibrium(A)

        assert(res[0] == val)
        assert(np.sum(np.abs(res[1] - p)) < 0.001)
        assert(np.sum(np.abs(res[2] - q)) < 0.001)


if __name__ == "__main__":
    unittest.main()
