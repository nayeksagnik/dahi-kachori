
# Phantom Consensus

## Team Information
- **Team Name**: TEAM DAHI KACHORI
- **Year**: 1ST YEAR
- **All-Female Team**: No

## Architecture Overview

The Phantom Consensus Engine is a resilient multi-agent political consensus simulator designed to generate stable agreements under adversarial and corrupted governance conditions. The architecture follows a layered pipeline consisting of data ingestion, sanitization, graph construction, probabilistic trust analysis, anomaly detection, proposal evaluation, coalition optimization, and explainable consensus generation.

The ingestion layer parses heterogeneous JSON and CSV datasets containing representatives, proposals, objections, and asymmetric political relationships. A defensive sanitization engine normalizes identifiers, removes duplicates, validates cross-references, resolves malformed records, and clamps corrupted numerical values to maintain graph consistency and prevent pipeline failure.

Political interactions are modeled as a weighted directed graph (G=(V,E)), where representatives form nodes and relationships form edges containing trust, rivalry, betrayal probability, and interaction recency. Relationship reliability is computed using probabilistic trust fusion:

1. Probabilistic Trust FusionThis formula calculates the primary trust relationship weight between two nodes:

$$R_{ab} = \alpha\left(\frac{T}{100}\right) + \beta\left(1 - \frac{R}{100}\right) + \gamma(1 - B) + \delta I_r$$

2. Dynamic Betrayal LikelihoodUpdated using Bayesian Inference to predict the probability of betrayal given current evidence:

$$P(B|E) = \frac{P(E|B) \cdot P(B)}{P(E)}$$

3. Sigmoid-Normalized Coalition ScoringDetermines proposal viability and the probability of acceptance within the mesh:

$$P(A_p) = \sigma(\sum S_i - \sum O_i - \lambda C_f)$$

4. Influence-Weighted ObjectionsComputed through logarithmic scaling of representative influence to prevent "vocal minority" corruption:

$$O_w = \sum(S_i \cdot \log(1 + I_i))$$

5. Z-Score Anomaly DetectionIntegrates PageRank-inspired influence propagation to identify anomalies in the trust network:

$$A_n = \frac{|x - \mu|}{\sigma}$$

These equations identify Trojan Horse representatives, Poison Pill proposals, and asymmetric alliances. This final consensus layer optimizes coalition stability while maximizing transparency through explainable, mathematically grounded decision outputs.


⚙️ Logic Execution Flow
The engine processes data through a four-stage deterministic pipeline:Ingestion & Normalization: DataLoader parses raw JSON/CSV inputs, normalizes identifiers to lowercase, and clamps influence values between $0$ and $100$ to prevent outlier corruption.Trust Fusion & PageRank: GraphEngine builds a directed network where edge weights are determined by a fusion of trust, rivalry, and betrayal probability. It then executes a PageRank algorithm to propagate and calculate the true relative influence of each node.Adversarial Filtering: The system applies Z-Score Anomaly Detection to the betrayal data. Any node with a betrayal likelihood $Z > 2.0$ is flagged as a "Trojan Horse" and purged from the potential coalition.Sigmoid Optimization: ConsensusLogic calculates the viability of each proposal by subtracting Logarithmic Influence-Weighted Objections from the base priority. The final result is passed through a Sigmoid function to determine the final acceptance probability:

$$P(A_p) = \frac{1}{1 + e^{-(Priority - Objection\_Weight)}}$$
