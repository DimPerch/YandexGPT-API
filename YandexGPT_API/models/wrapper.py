class Wrapper(dict):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(self, *args, **kwargs)

    def __getattr__(self, key: str):
        value = self.get(key)
        if isinstance(value, dict):
            return self.__class__(key)

        return value
