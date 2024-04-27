from .models.entities import YandexModels
import requests
from .models.promt_manager import PromtManager
from .models.entities import YandexModeURL


class Client:
    def __init__(self, api_key, folder_id, model=YandexModels.PRO):
        self._authorization = f"Api-key {api_key}"
        self._modelUri = f"gpt://{folder_id}/{model}"

    def make_request(self, query: PromtManager):
        headers = {"Content-Type": "application/json",
                   "Authorization": self._authorization}
        response = requests.post(YandexModeURL.SYNC.value,
                                 headers=headers,
                                 json=query)

        return response
