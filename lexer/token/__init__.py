class Token:
    def __init__(self, type: str, value: str) -> None:
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        return self.value
