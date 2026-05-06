import math

class ConsensusLogic:
    def __init__(self, reps, proposals, objections, pagerank_scores):
        self.reps = reps
        self.proposals = proposals
        self.objections = objections
        self.pagerank = pagerank_scores

    def score_proposals(self):
        scored = []
        for p_id, prop in self.proposals.items():
            
            # Theorem 5: Influence-weighted objections with Logarithmic scaling
            # O_w = Sum(Severity * log(1 + Influence))
            o_w = 0
            for obj in self.objections:
                if obj['proposal_id'] == p_id:
                    rep_inf = self.reps[obj['rep_id']]['influence']
                    # Apply PageRank multiplier to raw influence
                    pr_multiplier = self.pagerank.get(obj['rep_id'], 0.01) * 100
                    effective_inf = rep_inf * pr_multiplier
                    
                    o_w += obj['severity'] * math.log(1 + effective_inf)
            
            # Theorem 6: Sigmoid-normalized coalition scoring
            # P(A_p) = sigmoid(Priority - Objection_Weight)
            raw_score = prop['priority'] - (o_w / 10) 
            
            # Sigmoid function: 1 / (1 + e^-x)
            try:
                sigmoid_score = 1 / (1 + math.exp(-raw_score))
            except OverflowError:
                sigmoid_score = 0
                
            if sigmoid_score > 0.5: # 50% acceptance probability threshold
                scored.append({'id': p_id, 'score': sigmoid_score})
                
        scored.sort(key=lambda x: x['score'], reverse=True)
        return [p['id'] for p in scored[:2]]

    def form_coalition(self, selected_proposals, trojans):
        coalition = set(self.reps.keys())
        coalition -= trojans
        
        for obj in self.objections:
            if obj['proposal_id'] in selected_proposals and obj['severity'] > 5:
                coalition.discard(obj['rep_id'])
                
        return list(coalition)