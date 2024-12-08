import pytest
from pydantic import ValidationError

from secrets_vault.domain_layer import VaultPath


def test_create_vault_path_without_path() -> None:
    with pytest.raises(ValidationError):
        VaultPath()  # type: ignore


def test_create_vault_path(path: str) -> None:
    vault_path = VaultPath(path=path)
    assert vault_path.path == path
