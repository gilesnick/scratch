import pandas as pd
import numpy as np

# Import CVS file. First row of csv should be: [date, prcp]
data = pd.read_csv(r'D:\Nick\Documents\Scripts\tmpinput.csv', index_col=0, squeeze=True)

# Define date range of data (Start, End) in the format of mm-dd-yyyy.
idx = pd.date_range('01-01-1940', '12-31-2010')

# Define value which represents no data by changing FILL_VALUE
data.index = pd.DatetimeIndex(data.index)
data = data.reindex(idx, fill_value=-99)

# new_header is first row of output file.
new_header = ['19400101', ' ']
data.to_csv(r'D:\Nick\Documents\Scripts\tmpout.csv', header=new_header, index=None, mode='w')

# print("PCP data processing complete.")
