from secrets_vault.domain_layer.vault import Vault


def test_create_empty_vault() -> None:
    vault = Vault()
    assert vault.secrets_vaults == {}
