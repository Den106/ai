from pandas_datareader import data as pdr
import fix_yahoo_finance
#Yahoo_finance_API_the _best

data = pdr.get_data_yahoo('BLK', start='1999-10-01', end='2019-03-22')
