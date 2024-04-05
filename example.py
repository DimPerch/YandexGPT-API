from YandexGPT_API import YandexGPTApi
from pprint import pprint


if __name__ == "__main__":
    gpt = YandexGPTApi(config="config.ini")
    message = [{
        "role": "user",
        "text": "Привет, давай знакомиться"
    }]
    answer = gpt.make_request(message)
    pprint(answer)
