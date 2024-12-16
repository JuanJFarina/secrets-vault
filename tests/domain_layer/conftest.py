import os
from unittest.mock import MagicMock

import pytest

from secrets_vault.domain_layer import (
    Secret,
    SecretsVault,
    Vault,
    VaultPath,
)


@pytest.fixture()
def secret_value() -> str:
    return "secret_value"


@pytest.fixture()
def other_secret_value() -> str:
    return "other_secret_value"


@pytest.fixture()
def path() -> str:
    return "path" + os.path.sep + "test.txt"


@pytest.fixture()
def vault_path_mock() -> str:
    return MagicMock(VaultPath)


@pytest.fixture()
def secret(secret_value: str) -> Secret:
    return Secret(secret_value=secret_value)


@pytest.fixture()
def secret_mock(secret_value: str) -> Secret:
    secret = MagicMock(Secret)
    secret.secret_value = secret_value
    return secret


@pytest.fixture()
def empty_secrets_vault_with_mock_path(vault_path_mock: VaultPath) -> SecretsVault:
    return SecretsVault(path=vault_path_mock)


@pytest.fixture()
def secrets_vault_with_mock_values(
    secret_mock: Secret, vault_path_mock: VaultPath
) -> SecretsVault:
    return SecretsVault(path=vault_path_mock, secret=secret_mock)


@pytest.fixture()
def empty_vault() -> Vault:
    return Vault()
