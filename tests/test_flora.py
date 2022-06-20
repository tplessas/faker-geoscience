import re
import unittest

from alphabet_detector import AlphabetDetector
from faker import Faker

from faker_geoscience.flora.el_GR import Provider as ElGrFloraProvider


class ElGrFloraProviderTest(unittest.TestCase):
    """This class contains tests for greek provider about flora"""
    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)
        self.fake.add_provider(ElGrFloraProvider)

        self.ad = AlphabetDetector()

    def test_plant_name(self):
        """
        Test for 100 random plant names 
        - if  characters are greek 
        - if first character is capital 
        """
        for _ in range(100):
            output = self.fake.plant_name()
            self.assertTrue(self.ad.only_alphabet_chars(output, "GREEK"))
            self.assertTrue(re.search(r'^[Α-ΩΆΈΉΊΌΎΏ]', output))
