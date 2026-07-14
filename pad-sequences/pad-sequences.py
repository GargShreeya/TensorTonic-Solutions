import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    L = max_len if max_len is not None else max(len(seq) for seq in seqs)
    padded_seqs = []
    for seq in seqs:
        n = len(seq)
        if n < L:
            seq = seq + [pad_value]*(L-n)
        elif n > L:
            seq = seq[:L]
        padded_seqs.append(seq)
    return padded_seqs
            
        
    
    