# import pandas as pd
from pandas import isnull
from numpy import sum


def count_missing(vec):
    """Count the number of missing values in a vector
    """
    null_vec = isnull(vec)
    return sum(null_vec)
