from unittest.mock import MagicMock

import pytest

from secrets_vault.domain_layer import Secret, VaultPath


@pytest.fixture()
def secret_key() -> str:
    return "secret_key"


@pytest.fixture()
def secret_value() -> str:
    return "secret_value"


@pytest.fixture()
def path() -> str:
    return "path"


@pytest.fixture()
def vault_path() -> str:
    return MagicMock(VaultPath)


@pytest.fixture()
def list_with_one_secret() -> list[Secret]:
    return [MagicMock(Secret)]


@pytest.fixture()
def list_with_many_secrets() -> list[Secret]:
    return [MagicMock(Secret) for _ in range(4)]
