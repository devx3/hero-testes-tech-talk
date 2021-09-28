from unittest import mock, TestCase
from unittest.mock import Mock

from services.companies_match import CompaniesMatch
from services.mock import RESPONSE_MOCK


class TestCompaniesMatch(TestCase):

    @mock.patch('services.companies_match.requests.get')
    def test_if_response_is_ok(self, mock_get):
        """Return json with response"""

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = RESPONSE_MOCK
        companies_match = CompaniesMatch()
        companies_match.get()
        self.assertIsInstance(companies_match._companies, list)
        self.assertEqual(companies_match._companies[0]['request_id'], 'REQUEST_UUID')

    @mock.patch('services.companies_match.requests.get')
    def test_if_response_is_nok(self, mock_get):
        """Return empty list if response is not ok."""
        mock_get.return_value = Mock(ok=False)
        companies_match = CompaniesMatch()
        companies_match.get()
        self.assertIsInstance(companies_match._companies, list)
        self.assertEqual(companies_match._companies, [])