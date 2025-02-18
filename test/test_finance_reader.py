import pytest
from unittest.mock import patch, MagicMock
from src.finance_reader import read_transactions_from_csv, read_transactions_from_excel


@patch('pandas.read_csv')
def test_read_transactions_from_csv(mock_read_csv):
    # Настройка mock-объекта
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{'id': 1, 'amount': 100}]
    mock_read_csv.return_value = mock_df

    result = read_transactions_from_csv('dummy_path.csv')

    assert result == [{'id': 1, 'amount': 100}]
    mock_read_csv.assert_called_once_with('dummy_path.csv')


@patch('pandas.read_excel')
def test_read_transactions_from_excel(mock_read_excel):
    # Настройка mock-объекта
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{'id': 1, 'amount': 200}]
    mock_read_excel.return_value = mock_df

    result = read_transactions_from_excel('dummy_path.xlsx')

    assert result == [{'id': 1, 'amount': 200}]
    mock_read_excel.assert_called_once_with('dummy_path.xlsx')
