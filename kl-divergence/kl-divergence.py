import numpy as np

def kl_divergence(p, q, eps=1e-12):
    """
    Compute KL Divergence D_KL(P || Q).
    """
    # p and q are discrete probality mass function
    N = len(p)
    sum = 0
    for i in range(N):
        sum += p[i]*np.log((p[i]/q[i]) + eps)
    return sum