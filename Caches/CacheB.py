import requests

from Caches.CacheInterface import CacheInterface

""" == Tests == """
""" Wrong URL """
""" Wrong file name """
""" Wrong credentials """
""" Missing credentials """
""" Cache server offline """
""" Multiple requests from multiple origins """


class CacheB(CacheInterface):

    def get_content(self, file_name: str, server_url: str) -> bytes:
        # Request from Cache A for content
        response = requests.request("GET", server_url + file_name)
        return response.content

    def get_state(self) -> dict:
        # load instance state from local machine
        pass
