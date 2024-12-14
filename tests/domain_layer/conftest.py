from unittest.mock import MagicMock

import pytest

from secrets_vault.domain_layer import Secret, SecretsVault, VaultPath


@pytest.fixture()
def secret_value() -> str:
    return "secret_value"


@pytest.fixture()
def other_secret_value() -> str:
    return "other_secret_value"


@pytest.fixture()
def path() -> str:
    return "path"


@pytest.fixture()
def vault_path() -> str:
    return MagicMock(VaultPath)


@pytest.fixture()
def secret(secret_value: str) -> Secret:
    secret = MagicMock(Secret)
    secret.secret_value = secret_value
    return secret


@pytest.fixture()
def empty_vault() -> SecretsVault:
    return SecretsVault(path=MagicMock(VaultPath))


@pytest.fixture()
def secrets_vault(secret: Secret) -> SecretsVault:
    return SecretsVault(path=MagicMock(VaultPath), secret=secret)
