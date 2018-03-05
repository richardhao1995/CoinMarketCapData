import pandas as pd
import datetime
from pandas_datareader import data
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df = pd.read_csv('CoinMarketCapData.csv')

#print(df.head())

#BTC_df = df[df['symbol'].isin(['BTC'])]

BTC_df = df.loc[df['symbol'] == 'BTC']

BTC_df.to_csv('BTC.csv', encoding='utf-8', index = False)

#print(BTC_df.head())

BTC_df = pd.read_csv('BTC.csv')

#print(BTC_df.head())

BTC_df[['date', 'time']] = BTC_df.current_time.str.split(' ', expand = True)
BTC_df[['current_time']] = BTC_df[['date']]
BTC_df.drop(['date', 'time'], axis= 1, inplace = True )

print(BTC_df.head())

average_value_btc = BTC_df.price_usd.mean()
print(average_value_btc)

# for index, row in BTC_df.iterrows():
# 	#print(index)
# 	print(row['current_time'])

Cleaned_DF = pd.DataFrame(columns= BTC_df.columns)

no_of_datapoints = 1

for i in range(1, len(BTC_df)):

	if BTC_df.loc[i-1,'current_time'] == BTC_df.loc[i,'current_time']:
		no_of_datapoints = no_of_datapoints + 1
	else:

		curr_row = BTC_df.iloc[i-1,:]
		Cleaned_DF = Cleaned_DF.append(curr_row)
		Cleaned_DF.loc[i-1,'price_usd'] = BTC_df.loc[i - no_of_datapoints:i-1,'price_usd'].median()
		no_of_datapoints = 1	

Cleaned_DF = Cleaned_DF.reset_index()
Cleaned_DF.drop(['index'], axis= 1, inplace = True)
Cleaned_DF.to_csv('BTC_Daily.csv', encoding='utf-8', index = False)
print(Cleaned_DF.head())

Cleaned_DF.plot(x='current_time',y= 'price_usd')
plt.show()
