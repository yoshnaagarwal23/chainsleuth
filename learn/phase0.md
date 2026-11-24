# Phase 0: Design doc first

## Concepts

### 1. What a design doc is
A design doc is the **blueprint before the house**. You don't pour concrete and then decide
where the kitchen goes. It answers, in about one page:
- **Problem:** what hurts, and for whom?
- **Inputs / outputs:** what goes in, what comes out, in what shape?
- **Success metrics:** how will we *know* it works, as a number?
- **Non-goals:** what we are deliberately *not* doing (this prevents scope creep).
- **Risks:** what could make this fail, and what we'll do about it.

### 2. Why AI engineers write one first
With normal code, "does it work?" is mostly yes/no: the test passes or it doesn't.
With ML and LLMs, the output is *sometimes* right. So "works" has to be a **metric** you pick
*before* building, or you'll unconsciously pick whichever metric makes your system look good.

> Analogy: decide the grading rubric *before* reading the essays, not after.

### 3. Eval-first
Order of work in this project:
1. Define the metric (this phase)
2. Build the labeled eval set (Phase 4)
3. Simplest baseline: hand-written rules (Phase 5), which is **the number to beat**
4. Fancier things (ML in Phase 6, agents in Phase 7) only stay if they beat it

### 4. Precision vs recall (our headline metric)
Our headline metric is **scam recall at ≥70% precision**.
- **Recall** = of all real scam wallets, what fraction did we catch?
- **Precision** = of all wallets we *flagged* as scam, what fraction really were scams?

> Analogy: a metal detector at the airport. High recall = it catches every knife.
> High precision = when it beeps, there's actually a knife (not a belt buckle).
> Turn up the sensitivity and recall rises while precision falls. We pick the sensitivity where
> precision stays ≥ 70%, then try to maximize recall there.

## Worked example (real numbers)
Say the eval set has **10 scam wallets** and **20 non-scam wallets**. Our system flags 9 wallets:
7 really are scams, 2 are normal wallets wrongly flagged.

| | Actually scam | Actually not scam |
|---|---|---|
| **Flagged** | 7 (true positive) | 2 (false positive) |
| **Not flagged** | 3 (false negative) | 18 (true negative) |

- Recall = 7 / (7 + 3) = **0.70**
- Precision = 7 / (7 + 2) = **0.78** (≥ 0.70, so this setting is allowed)
- Accuracy = (7 + 18) / 30 = **0.83**

Now imagine a lazy system that says "not scam" for everything:
- Accuracy = 20 / 30 = **0.67**, which still looks OK
- Recall = 0 / 10 = **0.00**: it is useless

That's why we don't use accuracy as the headline. (More on this in Phase 4.)

## Quiz
1. Why do we write the success metric down *before* building the system?
2. A system flags 4 wallets; 2 are scams. There are 8 scams total. What are precision and recall?
3. Why is "victim" not one of our labels, even though it's an interesting question?

---
---
---

### Answers (scroll down only after trying)
1. So we can't pick whichever metric flatters the result after seeing it. The metric is fixed, so the
   comparison between rules, ML, and agents is fair.
2. Precision = 2/4 = **0.50**. Recall = 2/8 = **0.25**. (This setting fails our ≥ 70% precision bar.)
3. We need trustworthy *labels* to evaluate against. Public sources (Etherscan tags, Kaggle) label
   scams, mixers, and exchanges, but almost never victims. A label we can't verify can't be measured.

## Try it yourself (no AI)
1. Open `docs/design.md`. Add one more **risk** you can think of, with a one-line mitigation.
2. In the worked example above, suppose we tune the system to flag 12 wallets: 9 scams and 3 normal.
   Compute precision and recall by hand. Is the new setting allowed by our ≥ 70% precision rule?
   Is it better than the old one?
