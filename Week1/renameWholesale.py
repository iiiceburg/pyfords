# padas lib
import pandas as pd
from pandas import DataFrame 
#paht to dataset
data_url = 'D:\course\pythonForDataScience\Assignment\Week1\Wholesale customers data.csv'
whscdata = pd.read_csv(data_url)
# print (whscdata)
# z = whscdata[['Channel','Region']]
whscdata.loc[whscdata['Channel'] < 2, 'Channel']  = 'ice'

whscdata.to_csv('D:\course\pythonForDataScience\Assignment\Week1\Wholesale customers data.csv')   