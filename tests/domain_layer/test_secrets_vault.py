import pytest
from pydantic import ValidationError

from secrets_vault.domain_layer import Secret, SecretsVault, VaultPath


def test_create_vault_without_secret(vault_path: VaultPath) -> None:
    assert SecretsVault(path=vault_path)


def test_modify_secret_to_empty_vault(
    empty_vault: SecretsVault, secret_value: str
) -> None:
    assert not empty_vault.secret
    empty_vault.modify_secret(secret_value)
    assert empty_vault.secret


def test_modify_secret(secrets_vault: SecretsVault, other_secret_value: str) -> None:
    assert secrets_vault.secret
    original_secret = secrets_vault.secret
    secrets_vault.modify_secret(other_secret_value)
    assert secrets_vault.secret != original_secret


def test_delete_secret(secrets_vault: SecretsVault) -> None:
    assert secrets_vault.secret
    secrets_vault.delete_secret()
    assert not secrets_vault.secret


def test_create_vault_with_secret(vault_path: VaultPath, secret: Secret) -> None:
    secret_vault = SecretsVault(path=vault_path, secret=secret)
    assert secret_vault.secret
    assert secret_vault.secret.secret_value == secret.secret_value


def test_create_vault_without_path(secret: Secret) -> None:
    with pytest.raises(ValidationError):
        SecretsVault(secret=secret)  # type: ignore
