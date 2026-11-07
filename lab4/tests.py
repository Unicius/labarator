"""UnitTest для тестирования модулей validators и operations."""

import unittest
import math
from operations import (
    calculate_w_rectangle,
    calculate_w_circle,
    calculate_w_i_beam,
    calculate_stress_and_status
)
from constants import CLASS_HIGH_MARGIN, CLASS_ACCEPTABLE, CLASS_OVERLOAD


class TestBeamOperations(unittest.TestCase):

    def test_calculate_w_rectangle(self):
        # b=10, h=20 -> W = 10 * 400 / 6 = 666.666...
        self.assertAlmostEqual(calculate_w_rectangle(10, 20), 666.6666666666666)

    def test_calculate_w_circle(self):
        # d=10 -> W = pi * 1000 / 32
        expected = (math.pi * 1000) / 32
        self.assertAlmostEqual(calculate_w_circle(10), expected)

    def test_calculate_w_i_beam(self):
        # h=12 -> W = 12^3 / 12 = 144
        self.assertAlmostEqual(calculate_w_i_beam(12), 144.0)

    def test_calculate_stress_and_status_high_margin(self):
        # W=10000 mm3, M=1 kNm -> sigma = 1e6 / 10000 = 100 MPa
        # allowable = 300 MPa -> utilization = 100/300 = 0.333 < 0.5
        sigma, util, status = calculate_stress_and_status(10000, 1.0, 300.0)
        self.assertEqual(status, CLASS_HIGH_MARGIN)

    def test_calculate_stress_and_status_acceptable(self):
        # W=10000 mm3, M=2 kNm -> sigma = 2e6 / 10000 = 200 MPa
        # allowable = 300 MPa -> utilization = 200/300 = 0.666 (между 0.5 и 1.0)
        sigma, util, status = calculate_stress_and_status(10000, 2.0, 300.0)
        self.assertEqual(status, CLASS_ACCEPTABLE)

    def test_calculate_stress_and_status_overload(self):
        # W=10000 mm3, M=4 kNm -> sigma = 4e6 / 10000 = 400 MPa
        # allowable = 300 MPa -> utilization = 400/300 = 1.333 > 1.0
        sigma, util, status = calculate_stress_and_status(10000, 4.0, 300.0)
        self.assertEqual(status, CLASS_OVERLOAD)


if __name__ == "__main__":
    unittest.main()