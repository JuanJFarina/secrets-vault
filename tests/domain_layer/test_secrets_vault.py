import pytest
from pydantic import ValidationError

from secrets_vault.domain_layer import Secret, SecretsVault, VaultPath


def test_create_vault_without_secret(vault_path_mock: VaultPath) -> None:
    assert SecretsVault(path=vault_path_mock)


def test_modify_secret_to_empty_vault(
    empty_secrets_vault_with_mock_path: SecretsVault, secret_value: str
) -> None:
    assert not empty_secrets_vault_with_mock_path.secret
    empty_secrets_vault_with_mock_path.modify_secret(secret_value)
    assert empty_secrets_vault_with_mock_path.secret == secret_value


def test_modify_secret(
    secrets_vault_with_mock_values: SecretsVault, other_secret_value: str
) -> None:
    assert secrets_vault_with_mock_values.secret
    original_secret = secrets_vault_with_mock_values.secret
    secrets_vault_with_mock_values.modify_secret(other_secret_value)
    assert secrets_vault_with_mock_values.secret != original_secret


def test_delete_secret(secrets_vault_with_mock_values: SecretsVault) -> None:
    assert secrets_vault_with_mock_values.secret
    secrets_vault_with_mock_values.delete_secret()
    assert not secrets_vault_with_mock_values.secret


def test_create_vault_with_secret(
    vault_path_mock: VaultPath, secret_mock: Secret
) -> None:
    secret_vault = SecretsVault(path=vault_path_mock, secret=secret_mock)
    assert secret_vault.secret
    assert secret_vault.secret.secret_value == secret_mock.secret_value


def test_create_vault_without_path(secret_mock: Secret) -> None:
    with pytest.raises(ValidationError):
        SecretsVault(secret=secret_mock)  # type: ignore
