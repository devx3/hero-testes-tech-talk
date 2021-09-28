# import requests
# from typing import Dict, Any, List, Union
#
#
# class CompaniesMatch:
#
#     __baseurl: str = 'http://url.com.br'
#     _companies: Union[List[Dict[str, Any]], None] = None
#
#     def __init__(self):
#         self._companies = None
#
#     def get(self) -> None:
#         """Return companies"""
#         response = self._request()
#         if self._is_request_ok(response):
#             self._companies = response.json()
#
#     @classmethod
#     def save(cls, companies):
#         pass
#
#     @staticmethod
#     def _is_request_ok(response: requests.Response) -> bool:
#         return response.ok
#
#     def _request(self) -> requests.Response:
#         """Make the request for D-Legal."""
#
#         response = requests.get(self.__baseurl)
#         return response
#

import requests
from typing import List, Union, Dict, Any


class CompaniesMatch:

    _companies: Union[List, None] = None
    _baseurl: str = 'http://url.example'

    def __init__(self):
        self._companies = None

    def get(self) -> None:
        """Return companies"""
        response = self._request()
        self._companies = self._get_companies(response)

    @staticmethod
    def _get_companies(response: requests.Response) -> List[Dict[str, Any]]:
        data = []
        if response.ok:
            data = response.json()

        return data

    def _request(self) -> requests.Response:
        return requests.get(self._baseurl)
