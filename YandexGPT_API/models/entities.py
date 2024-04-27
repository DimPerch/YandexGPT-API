from enum import Enum


class YandexModels(str, Enum):
    PRO = "yandexgpt/latest"
    LITE = "yandexgpt-lite/latest"
    SUMMARIZATION = "summarization/latest"


class YandexRole(str, Enum):
    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"


class YandexModeURL(str, Enum):
    SYNC = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    ASYNC = "..."
