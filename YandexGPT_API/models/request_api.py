from .wrapper import Wrapper
from .entities import YandexRole


class RequestAPI(Wrapper):
    def __init__(self, modelUri, temperature, max_tokens):
        body = {"modelUri": None,
                "completionOptions": {
                    "stream": True,
                    "temperature": temperature,
                    "maxTokens": max_tokens
                },
                "messages": []
                }

        super().__init__(body)

    def _add_message(self, text: str, role=YandexRole.USER) -> None:
        message = {"role": role,
                   "text": text}
        self.messages.append(message)
