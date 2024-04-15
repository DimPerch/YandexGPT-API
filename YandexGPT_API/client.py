from .models.entities import YandexModels
import requests
from .models.request_api import RequestAPI
from .models.entities import YandexModeURL


class Client:
    def __init__(self, api_key, folder_id, model=YandexModels.PRO):
        self._authorization = f"Api-key {api_key}"
        self._modelUri = f"gpt://{folder_id}/{model}"

    def make_request(self, request: RequestAPI):
        headers = {"Content-Type": "application/json",
                   "Authorization": self._authorization}
        request.modelUri = self._modelUri
        response = requests.post(YandexModeURL.SYNC,
                                 request,
                                 headers=headers)

        return response
