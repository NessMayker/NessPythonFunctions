"""
Normalizes an array.
"""

def norm(probs):
    prob_factor = 1 / sum(probs)
    return [prob_factor * p for p in probs]