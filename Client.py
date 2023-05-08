import requests as requests

from Caches.CacheA import CacheA
from Caches.CacheB import CacheB
from Router import Router
from Logger import Logger

"""" == Tests == """
""" Wrong URL """
""" Wrong file name """
""" Cache server offline """
""" Empty response """
""" Corrupted response """


class Client:
    router = Router()
    logger = Logger("client")

    def get_video(self, file_name):
        try:
            server_url = self.router.get_cache()
            if "region-x" and "cache-a" in server_url:
                content_from_cache_a = CacheA()
                response = content_from_cache_a.get_content(file_name, server_url)
            elif "region-y" and "cache-b" in server_url:
                content_from_cache_b = CacheB()
                response = content_from_cache_b.get_content(file_name, server_url)
            else:
                response = requests.request("GET", server_url + file_name)
            self.logger.log("ok")
            return response.content
        except Exception as e:
            self.logger.error(e)
