import os
import pytest
from bank_transactions.transaction_utils import load_transactions_from_json


def test_load_transactions_from_json():
    test_file_path = os.path.join(os.path.dirname(__file__), '../bank_transactions/test_data.json')
    transactions = load_transactions_from_json(test_file_path)
    assert isinstance(transactions, list)




