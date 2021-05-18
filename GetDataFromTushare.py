import tushare as ts
from WorldQuant101 import WorldQuant101  as WQ

print(ts.__version__)

ts.set_token('c8e86deed77c011c432f5e6d4f19d45bb67a6378b474c8032cd55d0e')

pro = ts.pro_api()

df = pro.daily(ts_code='000001.SZ', start_date='20210101', end_date='20210514')

df.columns = ['ts_code', 'trade_date', 'S_DQ_OPEN', 'S_DQ_HIGH', 'S_DQ_LOW', 'S_DQ_CLOSE', 'pre_close',
                'change', 'S_DQ_PCTCHANGE', 'S_DQ_VOLUME', 'S_DQ_AMOUNT']
dfdata = WQ.get_alpha(df)

dfdata.to_excel('Theend.xlsx')

print(df)
