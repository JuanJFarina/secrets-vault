from pydantic import BaseModel, Field

from .secret import Secret
from .vault_path import VaultPath


class SecretsVault(BaseModel):
    path: VaultPath
    version: int = 0
    secrets: list[Secret] = Field(default_factory=list[Secret])

    def add_secret(self, key: str, value: str) -> None:
        self.secrets.append(Secret(key=key, value=value))
