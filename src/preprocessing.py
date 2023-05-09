# Tech preambel:
import numpy as np


def bar_color(data,color_pos,color_neg):
    
    """
    Function to specify bar color for bar plots, according to sign of given values:
    
    Parameters:
    ===========
    data: Pandas DataFrame containing the time series to be visualized.
    color_pos, color_neg: String to specify color for bars with positive and negative values, respectively.
    
    Returns:
    ========
    Numpy array of strings, corresponding to bar color.
    
    """    
    
    return np.where(data.values>0,color_pos,color_neg).T


def split_sequence(sequence, n_steps):
    
    """
    Function to split sequence into specified number of time steps:
    
    Parameters:
    ===========
    sequence: Numpy array or Pandas DataFrame containing the time series data to be split.
    n_steps: Integer number, specifies the number of time steps.
    
    Returns:
    ========
    Numpy array with split sequence data.
    
    """    
    
    X = list()
    for i in range(len(sequence)):
        # Find the end of this pattern
        end_ix = i + n_steps
        # Check if we are beyond the sequence
        if end_ix > len(sequence):
            break
        # Gather input and output parts of the pattern
        seq_x = sequence[i:end_ix]
        X.append(seq_x)
    return np.array(X)