import unittest
from main import return_age_between_two_years


class TestAge(unittest.TestCase):

    def test_age_between_two_years(self):
        """Should return age between two given years"""
        expected_age = 22
        received_age = return_age_between_two_years(1993, 2015)
        self.assertEqual(received_age, expected_age)
