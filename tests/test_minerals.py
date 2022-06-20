import re
import unittest

from alphabet_detector import AlphabetDetector
from faker import Faker

from faker_geoscience.minerals.el_GR import Provider as ElGrMineralsProvider


class ElGrMineralsProviderTest(unittest.TestCase):
    """This class contains tests for greek provider about minerals"""
    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)
        self.fake.add_provider(ElGrMineralsProvider)

        self.ad = AlphabetDetector()

    def test_gemstone_name(self):
        """
        Test for 100 random gemstone names 
        - if  characters are greek 
        - if first character is capital 
        """
        for _ in range(100):
            output = self.fake.gemstone_name()
            self.assertTrue(self.ad.only_alphabet_chars(output, "GREEK"))
            self.assertTrue(re.search(r'^[Α-ΩΆΈΉΊΌΎΏ]', output))
