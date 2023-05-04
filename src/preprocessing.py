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