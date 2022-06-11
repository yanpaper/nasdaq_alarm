import FinanceDataReader as fdr
import ta.momentum as ta

#df_spx = fdr.StockListing('NASDAQ')
#df_spx.head()
# IXIC 	나스닥 지수
# US500 	S&P 500 지수
# NASDAQ 	나스닥 종목
# NYSE 	뉴욕 증권거래소 종목
# AMEX 	AMEX 종목
# SP500 	S&P500 종목


# df = fdr.DataReader('AAPL','2022-04-01', '2022-04-03')
# print(df)

df = fdr.DataReader('AAPL', '2022-04-01')
print(ta.rsi(df['Close']))

# def plot_graph(ticker, startdate, enddate=NULL, output_path):
#     df = fdr.DataReader('AAPL', '2022')
#     fig = df['Close'].plot()
#     fig.grid()
#     fig.title(ticker)
#     fig.get_figure().savefig('output2.png')