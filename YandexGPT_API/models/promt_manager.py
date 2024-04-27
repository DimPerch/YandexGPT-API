from .wrapper import Wrapper
from .entities import YandexRole


class PromtManager(Wrapper):
    def __init__(self,
                 client,
                 temperature=.5,
                 max_tokens=100,
                 stream=False):

        body = {"modelUri": client._modelUri,
                "completionOptions": {
                    "stream": stream,
                    "temperature": temperature,
                    "maxTokens": max_tokens
                },
                "messages": []
                }

        super().__init__(**body)

    def add_message(self, text: str, role=YandexRole.USER.value) -> None:
        message = {"role": role,
                   "text": text}
        self.messages.append(message)

    def clear(self) -> None:
        self.messages.clear()
