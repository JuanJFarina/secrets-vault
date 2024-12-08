import pytest
from pydantic import ValidationError

from secrets_vault.domain_layer import Secret, SecretsVault, VaultPath


def test_create_vault_without_secrets(vault_path: VaultPath) -> None:
    assert SecretsVault(path=vault_path)  # type: ignore


def test_create_vault_with_one_secret(
    vault_path: VaultPath, list_with_one_secret: list[Secret]
) -> None:
    secret_vault = SecretsVault(path=vault_path, secrets=list_with_one_secret)
    assert len(secret_vault.secrets) == len(list_with_one_secret)


def test_create_vault_with_many_secrets(
    vault_path: VaultPath, list_with_many_secrets: list[Secret]
) -> None:
    secrets_vault = SecretsVault(path=vault_path, secrets=list_with_many_secrets)
    assert len(secrets_vault.secrets) == len(list_with_many_secrets)


def test_create_vault_without_path(list_with_one_secret: list[Secret]) -> None:
    with pytest.raises(ValidationError):
        SecretsVault(secrets=list_with_one_secret)  # type: ignore
