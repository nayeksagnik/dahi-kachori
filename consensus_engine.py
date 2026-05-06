import json
from src.sanitization_engine import DataLoader
from src.trust_fusion_graph import GraphEngine
from src.consensus_optimizer import ConsensusLogic

def run():
    print("1. Ingesting Data...")
    loader = DataLoader()
    loader.load_all()

    print("2. Mapping Political Networks & Executing PageRank...")
    graph = GraphEngine(loader.relations)
    graph.build_networks()
    alliances = graph.extract_alliances()

    print("3. Executing Sigmoid Consensus Logic...")
    # Passing the PageRank scores into the optimizer
    logic = ConsensusLogic(loader.reps, loader.proposals, loader.objections, graph.pagerank_scores)
    selected_proposals = logic.score_proposals()
    
    # Passing Trojans found via Z-Score
    trojans = graph.get_trojan_horses()
    supporting_reps = logic.form_coalition(selected_proposals, trojans)

    print("4. Generating Output...")
    output = {
        "final_agreement": {
            "proposals": selected_proposals,
            "supporting_reps": supporting_reps
        },
        "alliances": alliances
    }

    with open('output/result.json', 'w') as f:
        json.dump(output, f, indent=4)
        
    print("✅ Success! Output saved to output/result.json")

if __name__ == "__main__":
    run()