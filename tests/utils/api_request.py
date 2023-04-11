import requests
from requests import HTTPError, Timeout

from tests.utils.logger_util import logger


class ApiRequests:
    """This class contains methods to send requests to an API"""

    def __init__(self, headers: dict, base_url: str):
        """
        :param base_url : The base URL of the API
        :param headers : A dictionary of headers to pass with the request
        """
        self.base_url = base_url
        self.headers = headers

    def get_request(self, endpoint: str) -> requests.Response:
        """
        Executes a GET request on a given endpoint
        :param endpoint: the endpoint of the request
        :return: The response of the request
        """
        try:
            response = requests.get(url=self.base_url + endpoint, headers=self.headers)
            self.__log_response(response)
        except HTTPError as e:
            raise Exception(f'Error making the request: {e}')
        except Timeout as e:
            raise Exception(f'Request timed out: {e}')
        return response

    def post_request(self, endpoint: str, payload: dict) -> requests.Response:
        """
        Executes a POST request on a given endpoint
        :param endpoint: the endpoint of the request
        :param payload: The payload data to be sent with the request
        :return: The response of the request
        """
        try:
            response = requests.post(url=self.base_url + endpoint, headers=self.headers, json=payload)
            self.__log_response(response)
        except HTTPError as e:
            raise Exception(f'Error making the request: {e}')
        except Timeout as e:
            raise Exception(f'Request timed out: {e}')
        return response

    def put_request(self, endpoint: str, payload: dict) -> requests.Response:
        """
        Executes a PUT request on a given endpoint
        :param endpoint: the endpoint of the request
        :param payload: The payload data to be sent with the request
        :return: The response of the request
        """
        try:
            response = requests.put(url=self.base_url + endpoint, headers=self.headers, json=payload)
            self.__log_response(response)
        except HTTPError as e:
            raise Exception(f'Error making the request: {e}')
        except Timeout as e:
            raise Exception(f'Request timed out: {e}')
        return response

    def patch_request(self, endpoint: str, payload: dict) -> requests.Response:
        """
        Executes a PATCH request on a given endpoint
        :param endpoint: the endpoint of the request
        :param payload: The payload data to be sent with the request
        :return: The response of the request
        """
        try:
            response = requests.patch(url=self.base_url + endpoint, headers=self.headers, json=payload)
            self.__log_response(response)
        except HTTPError as e:
            raise Exception(f'Error making the request: {e}')
        except Timeout as e:
            raise Exception(f'Request timed out: {e}')
        return response

    def delete_request(self, endpoint: str) -> requests.Response:
        """
        Executes a DELETE request on a given endpoint
        :param endpoint: the endpoint of the request
        :return: The response of the request
        """
        try:
            response = requests.delete(url=self.base_url + endpoint, headers=self.headers)
            self.__log_response(response)
        except HTTPError as e:
            raise Exception(f'Error making the request: {e}')
        except Timeout as e:
            raise Exception(f'Request timed out: {e}')
        return response

    @staticmethod
    def __log_response(response):
        logger.info(response.json())
        logger.info(response.status_code)
