from YandexGPT_API.client import Client
from YandexGPT_API.models.promt_manager import PromtManager
from YandexGPT_API.models.entities import YandexRole
import pprint

client = Client(folder_id="b1gqq2ubunchvfteuhso",
                api_key="AQVNzBqX3Mava9xtgPbiYeNal5R7gLcX2058-FNl")

message = PromtManager(client).add_message("Ты учитель истории",
                                           role=YandexRole.SYSTEM.value)
message.add_message("Кто открыл америку")
print(message)
response = client.make_request(message)
pprint.pprint(response.text)
