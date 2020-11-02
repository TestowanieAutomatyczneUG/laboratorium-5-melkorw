import unittest
from zad2 import Roman

class RomanNumeralsTest(unittest.TestCase):
  def setUp(self):
        self.temp = Roman()
        
    def test_1_is_a_single_i(self):
        self.assertEqual(self.temp.roman(1), "I")

    @unittest.skip("demonstrating skipping")
    def test_2_is_two_i_s(self):
        self.assertEqual(self.temp.roman(2), "II")

    @unittest.skip("demonstrating skipping")
    def test_3_is_three_i_s(self):
        self.assertEqual(self.temp.roman(3), "III")

    @unittest.skip("demonstrating skipping")
    def test_4_being_5_1_is_iv(self):
        self.assertEqual(self.temp.roman(4), "IV")

    @unittest.skip("demonstrating skipping")
    def test_5_is_a_single_v(self):
        self.assertEqual(self.temp.roman(5), "V")

    @unittest.skip("demonstrating skipping")
    def test_6_being_5_1_is_vi(self):
        self.assertEqual(self.temp.roman(6), "VI")

    @unittest.skip("demonstrating skipping")
    def test_9_being_10_1_is_ix(self):
        self.assertEqual(self.temp.roman(9), "IX")

    @unittest.skip("demonstrating skipping")
    def test_20_is_two_x_s(self):
        self.assertEqual(self.temp.roman(27), "XXVII")

    @unittest.skip("demonstrating skipping")
    def test_48_is_not_50_2_but_rather_40_8(self):
        self.assertEqual(self.temp.roman(48), "XLVIII")

    @unittest.skip("demonstrating skipping")
    def test_49_is_not_40_5_4_but_rather_50_10_10_1(self):
        self.assertEqual(self.temp.roman(49), "XLIX")

    @unittest.skip("demonstrating skipping")
    def test_50_is_a_single_l(self):
        self.assertEqual(self.temp.roman(59), "LIX")

    @unittest.skip("demonstrating skipping")
    def test_90_being_100_10_is_xc(self):
        self.assertEqual(self.temp.roman(93), "XCIII")

    @unittest.skip("demonstrating skipping")
    def test_100_is_a_single_c(self):
        self.assertEqual(self.temp.roman(141), "CXLI")

    @unittest.skip("demonstrating skipping")
    def test_60_being_50_10_is_lx(self):
        self.assertEqual(self.temp.roman(163), "CLXIII")

    @unittest.skip("demonstrating skipping")
    def test_400_being_500_100_is_cd(self):
        self.assertEqual(self.temp.roman(402), "CDII")

    @unittest.skip("demonstrating skipping")
    def test_500_is_a_single_d(self):
        self.assertEqual(self.temp.roman(575), "DLXXV")

    @unittest.skip("demonstrating skipping")
    def test_900_being_1000_100_is_cm(self):
        self.assertEqual(self.temp.roman(911), "CMXI")

    @unittest.skip("demonstrating skipping")
    def test_1000_is_a_single_m(self):
        self.assertEqual(self.temp.roman(1024), "MXXIV")

    @unittest.skip("demonstrating skipping")
    def test_3000_is_three_m_s(self):
        self.assertEqual(self.temp.roman(3000), "MMM")

if __name__ == '__main__':
    unittest.main()