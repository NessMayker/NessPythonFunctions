"""
Flatten lists of lists into a single list. 
"""

def flatten(t):
    return [item for sublist in t for item in sublist]