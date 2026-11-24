import pytest

from chainsleuth.config import MissingKeyError, get_settings, normalize_address


def test_missing_key_error_names_the_key(monkeypatch):
    monkeypatch.delenv("ETHERSCAN_API_KEY", raising=False)
    s = get_settings(load_env_file=False)
    with pytest.raises(MissingKeyError, match="ETHERSCAN_API_KEY.*etherscan.io"):
        s.require("ETHERSCAN_API_KEY")


def test_require_returns_value(monkeypatch):
    monkeypatch.setenv("ETHERSCAN_API_KEY", "abc123")
    assert get_settings(load_env_file=False).require("ETHERSCAN_API_KEY") == "abc123"


def test_anvil_default(monkeypatch):
    monkeypatch.delenv("ANVIL_RPC_URL", raising=False)
    assert get_settings(load_env_file=False).anvil_rpc_url == "http://127.0.0.1:8545"


def test_normalize_address_lowercases():
    a = "0xAbCdEf0123456789abcdef0123456789ABCDEF01"
    assert normalize_address(f"  {a} ") == a.lower()


@pytest.mark.parametrize("bad", ["", "0x123", "abcdef0123456789abcdef0123456789abcdef01",
                                 "0xZZcdef0123456789abcdef0123456789abcdef01"])
def test_normalize_address_rejects_bad(bad):
    with pytest.raises(ValueError):
        normalize_address(bad)
