# ChainSleuth: Design Doc

*Author: Yoshna · Status: Phase 0 draft · Last updated: 2026-11-24*

## Problem
Given an Ethereum wallet address, I want to know what kind of wallet it is: a scammer, a mixer
user, an exchange, or a normal person. Today that means clicking through Etherscan by hand,
following money hop by hop, and guessing. ChainSleuth automates the investigation and explains
its verdict with evidence.

## Users
- **Primary: me and the people reviewing my work** (recruiters, interviewers). This is a learning
  project and a portfolio piece. What matters most: clear code, honest eval results, a good demo.
- Secondary (not optimized for): analysts or curious crypto users who want a quick second opinion.

## Inputs / outputs
**Input:** one Ethereum address (`0x` + 40 hex characters), on mainnet or our local anvil chain.

**Output:** a case report containing:
| Field | Example |
|---|---|
| `label` | one of `scam`, `mixer`, `exchange`, `normal` |
| `risk_score` | 0.0 to 1.0 |
| `reasons` | top features/rules that drove the score |
| `evidence` | tx hashes, counterparties, money-flow graph |
| `summary` | plain-English paragraph |
| `cost_usd`, `latency_s` | what this investigation cost |

## Success metrics
| Metric | Target | Why |
|---|---|---|
| **Scam recall at ≥ 70% precision** (headline) | beat the rules baseline | Missing a scammer is the costly error, but flags must still be trustworthy |
| PR-AUC (scam vs rest) | reported alongside | Threshold-free comparison between models |
| Accuracy (4-class) | reported, never the headline | Misleading on imbalanced data |
| LLM cost per investigation | **< $0.10** | Cheap enough to re-run the whole eval set often |
| Latency per investigation | **< 60 s** | Fine for a live demo with a progress display |

Every approach (rules → ML → single LLM call → agents) is scored on the same held-out test split.
A component that doesn't beat the simpler one gets cut, and the result is logged.

## Non-goals
- Chains other than Ethereum (no Bitcoin, Solana, L2s, bridges). Ethereum mainnet data plus our local anvil chain only.

## Risks and mitigations
| Risk | Mitigation |
|---|---|
| Too few labeled wallets, so metrics are noisy | Combine Etherscan labels, the Kaggle dataset, and our own simulated scams; report sample sizes next to every number |
| Label leakage (e.g. a wallet's Etherscan tag "Phish" leaking into features) | Never use label tags as features; hold out a test split that is never used for tuning |
| Free API rate limits (Etherscan ~5 req/s) | Cache every response to `data/cache/`; limit trace hops |
| LLM costs creep up | Log tokens and cost per call; enforce the $0.10 budget in the eval harness |
| Wrongly calling a wallet a scam | The report says it's a risk assessment with evidence, not a proof; precision floor of 70% |
| Huge wallets (exchanges have millions of txs) | Cap transactions fetched per wallet; exchanges are labeled from known-address lists |

## Plan
About 6–8 weeks part-time, roughly one phase per week (Phases 0–9 in the project brief).
The repo is public on GitHub from day one.
