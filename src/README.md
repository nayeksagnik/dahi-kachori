# Phantom Consensus Engine

A resilient, multi-agent political consensus simulator designed to generate stable agreements under adversarial governance conditions.

## Architecture & File Mapping

* `consensus_engine.py`: The main entry point. Orchestrates the pipeline from ingestion to final JSON output.
* `src/sanitization_engine.py`: (The Ingestion Layer) Defensively normalizes identifiers, clamps corrupted numerical values, and resolves missing foreign keys to maintain data integrity.
* `src/trust_fusion_graph.py`: (The Graph Layer) Constructs the directed $G=(V,E)$ network. Implements **Probabilistic Trust Fusion**, **Bayesian Betrayal Inference**, and **Z-Score Anomaly Detection** to isolate Trojan Horses and Faction Infiltrators. Calculates **PageRank** influence propagation.
* `src/consensus_optimizer.py`: (The Logic Layer) Calculates **Influence-Weighted Objections** using logarithmic scaling and determines final proposal viability via **Sigmoid-Normalized Coalition Scoring**. 
* `dashboard.html`: The UI/UX visualization tie-breaker displaying the extracted consensus and alliance network.

## Run Instructions
1. Ensure dependencies are installed: `pip install -r requirements.txt`
2. Run the engine: `python consensus_engine.py`
3. Check `output/result.json` for the mathematically verified consensus.