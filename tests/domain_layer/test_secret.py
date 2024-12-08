import pytest
from pydantic import ValidationError

from secrets_vault.domain_layer import Secret


def test_create_secret(secret_key: str, secret_value: str) -> None:
    secret = Secret(key=secret_key, value=secret_value)
    assert secret.key == secret_key
    assert secret.value == secret_value


def test_create_secret_without_key(secret_value: str) -> None:
    with pytest.raises(ValidationError):
        Secret(value=secret_value)  # type: ignore


def test_create_secret_without_value(secret_key: str) -> None:
    with pytest.raises(ValidationError):
        Secret(value=secret_key)  # type: ignore
