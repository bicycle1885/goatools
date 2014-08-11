import unittest
import numpy as np
from goatools.multiple_testing import (
    Bonferroni,
    Sidak,
    HolmBonferroni,
    calc_qval
)


class TestMultipleTesting(unittest.TestCase):
    def test_bonferroni(self):
        bonferroni = Bonferroni([0.01, 0.01, 0.03, 0.05, 0.005], a=0.05)
        actual = bonferroni.corrected_pvals
        expected = np.array([0.05, 0.05, 0.15, 0.25, 0.025])
        self.assertTrue(np.allclose(actual, expected))

    def test_sidak(self):
        sidak = Sidak([0.01, 0.01, 0.03, 0.05, 0.005], a=0.05)
        actual = sidak.corrected_pvals
        expected = np.array([0.04898974,
                             0.04898974,
                             0.14696923,
                             0.24494871,
                             0.02449487])
        self.assertTrue(np.allclose(actual, expected))

    def test_holm_bonferroni(self):
        holm_bonferroni = HolmBonferroni([.01, .01, .03, .05, .005], a=.05)
        actual = holm_bonferroni.corrected_pvals
        expected = np.array([0.04, 0.04, 0.06, 0.05, 0.025])
        self.assertTrue(np.allclose(actual, expected))

    def test_fdr(self):
        pass


class TestFunctions(unittest.TestCase):
    def test_calc_qval(self):
        pass
