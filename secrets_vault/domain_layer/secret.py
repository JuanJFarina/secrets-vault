from pydantic import BaseModel


class Secret(BaseModel):
    secret_value: str

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Secret):
            return self.secret_value == other.secret_value
        if isinstance(other, str):
            return self.secret_value == other
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.secret_value)
