"""Settings loaded from environment variables / .env (never hard-code secrets)."""
from __future__ import annotations

import os
import re
from dataclasses import dataclass

from dotenv import load_dotenv

# Where to get each key, shown in error messages so a missing key is easy to fix.
KEY_HELP = {
    "ETHERSCAN_API_KEY": "free at https://etherscan.io/myapikey",
    "ALCHEMY_API_KEY": "free tier at https://dashboard.alchemy.com",
    "ANTHROPIC_API_KEY": "https://console.anthropic.com/settings/keys",
}

# LEARN: an Ethereum address is 20 bytes, written as "0x" + 40 hex characters.
# It's the last 20 bytes of the Keccak-256 hash of a public key (for normal wallets, a.k.a. EOAs).
ADDRESS_RE = re.compile(r"^0x[0-9a-fA-F]{40}$")


class MissingKeyError(RuntimeError):
    pass


@dataclass(frozen=True)
class Settings:
    etherscan_api_key: str | None
    alchemy_api_key: str | None
    anthropic_api_key: str | None
    anvil_rpc_url: str

    def require(self, name: str) -> str:
        """Return a key's value, or raise with instructions for getting it."""
        value = getattr(self, name.lower(), None)
        if not value:
            hint = KEY_HELP.get(name, "")
            raise MissingKeyError(f"{name} is not set. Add it to .env ({hint}).")
        return value


def get_settings(load_env_file: bool = True) -> Settings:
    if load_env_file:
        load_dotenv()
    return Settings(
        etherscan_api_key=os.getenv("ETHERSCAN_API_KEY") or None,
        alchemy_api_key=os.getenv("ALCHEMY_API_KEY") or None,
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY") or None,
        anvil_rpc_url=os.getenv("ANVIL_RPC_URL", "http://127.0.0.1:8545"),
    )


def normalize_address(address: str) -> str:
    """Validate an address and return it lowercase (so cache keys and lookups match)."""
    address = address.strip()
    if not ADDRESS_RE.match(address):
        raise ValueError(f"Not a valid Ethereum address: {address!r}")
    return address.lower()
