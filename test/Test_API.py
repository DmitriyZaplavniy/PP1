import unittest
from unittest.mock import mock_open, patch

from src.utils import read_json_file
from src.external_api import convert_currency


class TestReadJsonFile(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    def test_read_json_file_valid(self, mock_file):
        result = read_json_file('data/operations.json')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['amount'], 100)

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_read_json_file_empty(self, mock_file, mock_exists):
        result = read_json_file('data/operations.json')
        self.assertEqual(result, [])

    @patch('os.path.exists', return_value=False)
    def test_read_json_file_not_found(self, mock_exists):
        result = read_json_file('data/operations.json')
        self.assertEqual(result, [])


class TestConvertCurrency(unittest.TestCase):

    @patch('src.external_api.requests.get')
    @patch('os.getenv', return_value='test_api_key')
    def test_convert_currency_usd(self, mock_getenv, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'rates': {'RUB': 75.0}}
        transaction = {'amount': 100}
        result = convert_currency(transaction, 'USD')
        self.assertAlmostEqual(result, 7500.0)

    @patch('src.external_api.requests.get')
    @patch('os.getenv', return_value='test_api_key')
    def test_convert_currency_eur(self, mock_getenv, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'rates': {'RUB': 90.0}}
        transaction = {'amount': 100}
        result = convert_currency(transaction, 'EUR')
        self.assertAlmostEqual(result, 9000.0)

    def test_convert_currency_rub(self):
        transaction = {'amount': 100}
        result = convert_currency(transaction, 'RUB')
        self.assertEqual(result, 100.0)


if __name__ == '__main__':
    unittest.main()
