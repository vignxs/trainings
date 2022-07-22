import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.rand(10, 4), 
                  columns=('col_1', 'col_2', 'col_3', 'col_4'))
# print(df)
print(df.plot())