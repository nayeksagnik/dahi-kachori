
# Phantom Consensus

## Team Information
- **Team Name**: TEAM DAHI KACHORI
- **Year**: 1ST YEAR
- **All-Female Team**: No

## Architecture Overview

The Phantom Consensus Engine is a resilient multi-agent political consensus simulator designed to generate stable agreements under adversarial and corrupted governance conditions. The architecture follows a layered pipeline consisting of data ingestion, sanitization, graph construction, probabilistic trust analysis, anomaly detection, proposal evaluation, coalition optimization, and explainable consensus generation.

The ingestion layer parses heterogeneous JSON and CSV datasets containing representatives, proposals, objections, and asymmetric political relationships. A defensive sanitization engine normalizes identifiers, removes duplicates, validates cross-references, resolves malformed records, and clamps corrupted numerical values to maintain graph consistency and prevent pipeline failure.

Political interactions are modeled as a weighted directed graph (G=(V,E)), where representatives form nodes and relationships form edges containing trust, rivalry, betrayal probability, and interaction recency. Relationship reliability is computed using probabilistic trust fusion:

R_ab = α(T/100) + β(1 - R/100) + γ(1 - B) + δI_r

Dynamic betrayal likelihood is updated using Bayesian inference:

P(B|E) = [P(E|B) * P(B)] / P(E)

Proposal viability and acceptance probability are determined using sigmoid-normalized coalition scoring:

P(A_p) = σ(ΣS_i - ΣO_i - λC_f)

while influence-weighted objections are computed through:

O_w = Σ(S_i * log(1 + I_i))

The engine further integrates PageRank-inspired influence propagation and Z-score anomaly detection:

A_n = |x - μ| / σ
to identify Trojan Horse representatives, Poison Pill proposals, asymmetric alliances, and faction infiltrators. The final consensus layer optimizes coalition stability while maximizing transparency through explainable, mathematically grounded decision outputs.
