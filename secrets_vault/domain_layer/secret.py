from pydantic import BaseModel


class Secret(BaseModel):
    key: str
    value: str
