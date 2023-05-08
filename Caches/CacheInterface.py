from abc import abstractmethod


class CacheInterface:
    @abstractmethod
    def get_content(self, file_name: str, server_url: str) -> bytes:
        pass

    @abstractmethod
    def get_state(self) -> dict:
        pass
