import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    sum = 0 
    N = len(y_true)
    for i in range(N):
        p_i = y_pred[i][y_true[i]]
        sum += np.log(p_i)

    return (-sum/N)