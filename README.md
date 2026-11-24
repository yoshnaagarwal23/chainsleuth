# ChainSleuth

Give it an Ethereum wallet address. A team of AI agents pulls the wallet's on-chain history,
follows the money, scores the risk with ML, and writes a case report:
**scam, mixer, exchange, or normal?**

Built eval-first: rules baseline → ML → agents, and each layer stays only if it beats the last.

- Design: [docs/design.md](docs/design.md)
- Decisions: [DECISIONS.md](DECISIONS.md)
- Learning notes: [learn/](learn/)

## Setup
```bash
uv sync
cp .env.example .env   # then fill in keys
uv run pytest
```

*Work in progress. Results table coming in Phase 9.*
