from pydantic import BaseModel


class VaultPath(BaseModel):
    path: str
