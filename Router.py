from Monitor import Monitor

""" == Tests == """
""" Wrong URL """
""" Wrong file name """
""" Cache server offline """
""" Multiple requests from multiple origins """


class Router:
    monitor = Monitor()

    def get_cache(self):
        server_url = "https://server.region-x.amazonaws.com"
        states = self.monitor.get_states()
        url_cache_a = states["cache_a"]["url"]
        url_cache_b = states["cache_b"]["url"]

        if states["cache_a"]["state"] == "online":
            return url_cache_a
        elif states["cache_b"]["state"] == "online":
            return url_cache_b
        else:
            return server_url

        # logic on states and return cache  url
        pass
