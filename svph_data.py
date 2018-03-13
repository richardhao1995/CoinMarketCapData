import pandas as pd
import numpy as np
import datetime
from pandas_datareader import data
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df = pd.read_csv('20180228 - SVHAUsageAndPrice12Months.csv', encoding = "latin1")

#print(df.head())

#print(df.dtypes)

#SPLIT THE CSV INTO EACH HOSPITAL'S SEPARATE DATA

inventory_df = df.iloc[:,0:14]

SVHN_df = df.filter(regex= 'SVHN')
SVPHS_df = df.filter(regex= 'SVPHS')
MHS_df = df.filter(regex= 'MHS')
SVHM_df = df.filter(regex= 'SVHM')
SVPHMF_df = df.filter(regex= 'SVPHMF')
SVPHMK_df = df.filter(regex= 'SVPHMK')
SVPHME_df = df.filter(regex= 'SVPHME')
SVPHMW_df = df.filter(regex= 'SVPHMW')
HSNPH_df = df.filter(regex= 'HSNPH')
SVPHT_df = df.filter(regex= 'SVPHT')
SVPHB_df = df.filter(regex= 'SVPHB')
SVCS_df = df.filter(regex= 'SVCS')
SVPCHG_df = df.filter(regex= 'SVPCHG')
SVHA_df = df.filter(regex= 'SVHA')
Total_df = df.filter(regex= 'Total')



export_df = pd.concat([inventory_df,SVPHME_df], axis=1)

export_df = export_df[np.isfinite(df['SVPHME REC VAL'])]

print(inventory_df.head())
export_df.to_csv('SVPHME.csv',encoding = 'utf-8')
