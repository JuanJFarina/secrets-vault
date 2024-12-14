import pytest
from pydantic import ValidationError

from secrets_vault.domain_layer import Secret


def test_create_secret(secret_value: str) -> None:
    secret = Secret(secret_value=secret_value)
    assert secret.secret_value == secret_value


def test_create_secret_without_value() -> None:
    with pytest.raises(ValidationError):
        Secret()  # type: ignore
