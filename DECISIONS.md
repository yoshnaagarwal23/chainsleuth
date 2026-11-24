# Decisions log

Format: **Chose** / **Why** / **Didn't pick**

## Phase 0
### Primary user
- **Chose:** me + reviewers (learning / portfolio project)
- **Why:** optimizes for clear code, honest evals, and a good demo over production polish
- **Didn't pick:** compliance analyst, everyday crypto user

### Label set
- **Chose:** 4 classes: `scam`, `mixer`, `exchange`, `normal`
- **Why:** matches labels we can actually source (Etherscan tags, Kaggle); "victim" can't be labeled honestly
- **Didn't pick:** adding `victim` (5 classes); binary risky/not-risky

### Headline metric
- **Chose:** scam recall at ≥ 70% precision, with PR-AUC reported alongside
- **Why:** missing scammers is the costly error, but flags must stay trustworthy
- **Didn't pick:** PR-AUC alone (hard to explain), macro F1 (hides scam performance)

### Budgets
- **Chose:** < $0.10 LLM cost and < 60 s per investigation
- **Why:** lets us re-run the full eval set cheaply and still demo live
- **Didn't pick:** $0.50 / $0.02 cost caps; 15 s or unlimited latency

### Repo visibility
- **Chose:** public on GitHub from day one
- **Why:** shows a real, consistent commit history
- **Didn't pick:** private until Phase 9

### Tooling (small decisions, made without asking)
- **Chose:** `uv` + Python 3.12, `pyproject.toml` for config, plus `requirements.txt` kept in sync
- **Why:** uv is fast and already installed; 3.12 has the widest library support (3.14 is too new for some ML wheels)
- **Didn't pick:** plain `venv` + pip; Python 3.13/3.14
