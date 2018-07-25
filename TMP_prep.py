import pandas as pd
import numpy as np

# Import CVS file. First row of csv should be: [date, prcp]
#maxminall = pd.read_csv(r'D:\Nick\Documents\Scripts\minmaxall.csv', index_col=0, squeeze=True)

new_headers = ['max','min',]
mm = pd.read_csv(r'D:\Nick\Documents\Scripts\input_tmp.csv',index_col=0, skiprows=1,names=new_headers)
mm.head()

# Replace missing dates in max with -99
idx = pd.date_range('01-01-1940', '12-31-2010')

mm.index = pd.DatetimeIndex(mm.index)
mm = mm.reindex(idx, fill_value=-99)

# mmnn = [Date, Max, Min] with NaN values = -99
mmnn = mm.fillna(-99)
#print(mmnn)

# Write to TMP_output.cvs
new_header = ['19400101']
mmnn.to_csv('tmpNOHEADER.txt', header=False, index=None, mode='w')
c= open('tmpNOHEADER.txt')
f= open("TMP_output.txt","w+")
f.write("19400101" + '\n')
f.close()

f= open("TMP_output.txt", "a")
f.write(c.read())
f.close()
c.close()