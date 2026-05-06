import json
import csv
import os

class DataLoader:
    def __init__(self, data_dir="data/raw"):
        self.data_dir = data_dir
        self.reps = {}
        self.proposals = {}
        self.objections = []
        self.relations = []

    def load_all(self):
        with open(os.path.join(self.data_dir, 'representatives.json'), 'r') as f:
            for r in json.load(f):
                clean_id = str(r.get('id', '')).strip().lower()
                if clean_id:
                    val = r.get('influence')
                    influence = max(0, min(100, int(val))) if val not in [None, ""] else 0
                    self.reps[clean_id] = {'id': clean_id, 'influence': influence}
        
        with open(os.path.join(self.data_dir, 'proposals.json'), 'r') as f:
            for p in json.load(f):
                clean_id = str(p.get('id', '')).strip().lower()
                if clean_id and clean_id not in self.proposals:
                    self.proposals[clean_id] = {
                        'id': clean_id,
                        'priority': int(p.get('priority', 1)),
                        'sponsor': str(p.get('sponsor', '')).strip().lower()
                    }
        
        with open(os.path.join(self.data_dir, 'objections.json'), 'r') as f:
            for o in json.load(f):
                self.objections.append({
                    'rep_id': str(o.get('rep_id', '')).strip().lower(),
                    'proposal_id': str(o.get('proposal_id', '')).strip().lower(),
                    'severity': int(o.get('severity', 1))
                })
                
        with open(os.path.join(self.data_dir, 'relations.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.relations.append({
                    'from': str(row.get('from', '')).strip().lower(),
                    'to': str(row.get('to', '')).strip().lower(),
                    'trust': float(row.get('trust', 0.0)),
                    'rivalry': float(row.get('rivalry', 0.0)),
                    'betrayal_prob': float(row.get('betrayal_prob', 0.0))
                })
                
        valid_reps, valid_props = set(self.reps.keys()), set(self.proposals.keys())
        self.proposals = {k: v for k, v in self.proposals.items() if v['sponsor'] in valid_reps}
        self.objections = [o for o in self.objections if o['rep_id'] in valid_reps and o['proposal_id'] in valid_props]