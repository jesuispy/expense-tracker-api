# from django.test import TestCase
from unittest import TestCase

# Create your tests here.


def two_intergers_sum(a, b):
    return 0


class TestSum(TestCase):
    def test_sum(self):
        self.assertEqual(two_intergers_sum(1, 2), 3)
