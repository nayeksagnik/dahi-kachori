import networkx as nx
import statistics

class GraphEngine:
    def __init__(self, relations):
        self.relations = relations
        self.trust_graph = nx.Graph() 
        self.pagerank_scores = {}

    def build_networks(self):
        # Theorem 1: Probabilistic Trust Fusion
        # R_ab = alpha(T/100) + beta(1 - R/100) + gamma(1 - B)
        alpha, beta, gamma = 0.4, 0.2, 0.4 
        fusion_matrix = {}

        for rel in self.relations:
            u, v = rel['from'], rel['to']
            trust_norm = rel['trust'] / 100.0
            rivalry_norm = rel['rivalry'] / 100.0
            betrayal_safe = 1.0 - rel['betrayal_prob']
            
            # Fusion Score
            r_ab = (alpha * trust_norm) + (beta * (1.0 - rivalry_norm)) + (gamma * betrayal_safe)
            fusion_matrix[(u, v)] = r_ab
            
            # Construct base directed graph for PageRank propagation
            self.trust_graph.add_edge(u, v, weight=r_ab)

        # Theorem 2: PageRank Influence Propagation
        self.pagerank_scores = nx.pagerank(self.trust_graph, weight='weight')

        # Theorem 3: Asymmetric Alliance Resolution
        self.trust_graph.clear() # Rebuild as strict undirected for Cliques
        for (u, v), r_ab in fusion_matrix.items():
            r_ba = fusion_matrix.get((v, u), 0)
            if r_ab >= 0.60 and r_ba >= 0.60: # Mutual high trust fusion
                self.trust_graph.add_edge(u, v)

    def extract_alliances(self):
        cliques = list(nx.find_cliques(self.trust_graph))
        return sorted([c for c in cliques if len(c) >= 2], key=len, reverse=True)

    def get_trojan_horses(self):
        # Theorem 4: Z-Score Anomaly Detection for Betrayal Likelihood
        betrayals = [r['betrayal_prob'] for r in self.relations]
        if not betrayals or len(betrayals) < 2: return set()
        
        mu = statistics.mean(betrayals)
        sigma = statistics.stdev(betrayals)
        if sigma == 0: return set()

        trojans = set()
        for rel in self.relations:
            # Z-Score Formula: |x - mu| / sigma
            z_score = (rel['betrayal_prob'] - mu) / sigma
            # Anomaly threshold: Z-Score > 2.0 (Top ~2.5% of betrayers)
            if z_score > 2.0:
                trojans.add(rel['from'])
                
        return trojans