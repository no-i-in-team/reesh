"""Common and useful functions"""

import pandas as pd
import numpy as np
from sklearn.utils import shuffle

class DFAnalysis:

    def __init__(self , DataFrame):
        self.df = DataFrame

    def null_count(self):
        return self.df.isnull().sum().sum()
    
    def randomize(self, seed = 19):
        return self.df.shuffle( random_state = seed )

"""Making sure it works"""

# test = pd.DataFrame({ "A" : [ np.NaN , 2 , 3 ] ,"B" : [ 4 , np.NaN , 6 ] ,"C" : [ 7 , 8 , np.NaN ] })

# test = DFAnalysis(df)

# print( test.null_count() )
# print()
# print( test.randomize( 19 ) )