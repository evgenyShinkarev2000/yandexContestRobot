import unittest as ut
import main as m


class TestSolveLeftStep(ut.TestCase):
    def test0(self):
        self.assertEqual(m.solveLeftSteps(0), (0, 0))
    def test1(self):
        self.assertEqual(m.solveLeftSteps(1), (0, 1))
    def test2(self):
        self.assertEqual(m.solveLeftSteps(2), (1, 1))
    def test8(self):
        self.assertEqual(m.solveLeftSteps(8), (7, 1))
    def test9(self):
        self.assertEqual(m.solveLeftSteps(9), (0, 2))
    def test10(self):
        self.assertEqual(m.solveLeftSteps(10), (1, 2))
    def test24(self):
        self.assertEqual(m.solveLeftSteps(24), (15, 2))
    def test25(self):
        self.assertEqual(m.solveLeftSteps(25), (0, 3))
    def test26(self):
        self.assertEqual(m.solveLeftSteps(26), (1, 3))

class TestFindBeginPoint(ut.TestCase):
    def test0(self):
        self.assertEqual(m.findBeginPoint(0), (0, 0))
    def test1(self):
        self.assertEqual(m.findBeginPoint(1), (-1, 0))
    def test2(self):
        self.assertEqual(m.findBeginPoint(2), (-2, 1))