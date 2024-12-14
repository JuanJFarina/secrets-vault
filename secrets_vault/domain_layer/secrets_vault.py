from pydantic import BaseModel

from .secret import Secret
from .vault_path import VaultPath


class SecretsVault(BaseModel):
    path: VaultPath
    secret: Secret | None = None
    version: int = 1

    def modify_secret(self, secret_value: str) -> None:
        self.secret = Secret(secret_value=secret_value)
        self.version += 1

    def delete_secret(self) -> None:
        self.secret = None
        self.version += 1
