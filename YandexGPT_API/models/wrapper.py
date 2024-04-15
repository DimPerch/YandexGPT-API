class Wrapper:
    def __init__(self, request_dict: dict) -> None:
        super().__init__(self, request_dict)

    def __getattr__(self, key: str):
        value = self.get(key)
        if isinstance(value, dict):
            return self.__class__(key)

        return value
