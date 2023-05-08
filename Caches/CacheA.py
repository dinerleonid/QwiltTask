import requests

from Caches.CacheInterface import CacheInterface

""" == Tests == """
""" Wrong URL """
""" Wrong file name """
""" Wrong certificate """
""" Missing certificate """
""" Cache server offline """
""" Multiple requests from multiple origins """


class CacheA(CacheInterface):
    path_to_cert_file = '/my_cert.cert'

    def get_content(self, file_name: str, server_url: str) -> bytes:
        # Request from Cache A for content
        response = requests.request("GET", server_url + file_name)
        return response.content

    def get_state(self) -> dict:
        # connect to ec2 instance use boto3 and get instance state
        pass
