from pydantic import BaseModel, Field

from .secrets_vault import SecretsVault
from .vault_path import VaultPath


class Vault(BaseModel):
    secrets_vaults: dict[str, SecretsVault] = Field(
        default_factory=dict[str, SecretsVault]
    )

    def add_vault(self, path: str, secret: str | None = None) -> None:
        self.secrets_vaults[path] = SecretsVault(path=VaultPath(path=path))
        if secret:
            self.modify_vault_secret(path, secret)

    def modify_vault_secret(self, path: str, value: str) -> None:
        self.secrets_vaults[path].modify_secret(value)
