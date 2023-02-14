import pandas as pd
import numpy as np

pd.DataFrame(data, index, columns, dtype, copy)

df = pd.DateFrame(
    date = {'列1' : np.array([10, 20, 30, 40]),  
            '列2' : np.array([50, 60, 70, 80]), 
            '列3' : np.array(['a', 'b', 'c', 'd'])}
)

print(df)