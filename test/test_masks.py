import unittest

from src.masks.masks import get_mask_account, get_mask_card_number


class TestMasks(unittest.TestCase):

    def test_get_mask_card_number(self):
        self.assertEqual(get_mask_card_number(700079636361), "7000 79** **** 6361")

    def test_get_mask_account(self):
        self.assertEqual(get_mask_account(73654108430135874305), "**4305")


if __name__ == "__main__":
    unittest.main()
