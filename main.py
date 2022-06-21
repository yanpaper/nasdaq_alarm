import FinanceDataReader as fdr
import ta.momentum as ta
import pandas as pd
import datetime

#token : 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

#df_spx = fdr.StockListing('NASDAQ')
#df_spx.head()
# IXIC 	나스닥 지수
# US500 	S&P 500 지수
# NASDAQ 	나스닥 종목
# NYSE 	뉴욕 증권거래소 종목
# AMEX 	AMEX 종목
# SP500 	S&P500 종목

def before_today(day):
    days = (datetime.datetime.now() - datetime.timedelta(days=day)).strftime('%Y-%m-%d')
    return days


def main():
    mylist = ['ABBV', 'BX', 'AVGO', 'JNJ', 'SYY', 'TSM']
    for ticker in range(0, len(mylist)):
        df = fdr.DataReader(mylist[ticker], before_today(60))
        if (ticker == 0):
            info_df = pd.DataFrame(columns=['ticker', 'rsi'])
        info_df.loc[ticker]={'ticker':mylist[ticker], 'rsi':ta.rsi(df['Close']).values[-1]}
    print(info_df)
    del info_df

main()

# def plot_graph(ticker, startdate, enddate=NULL, output_path):
#     df = fdr.DataReader('AAPL', '2022')
#     fig = df['Close'].plot()
#     fig.grid()
#     fig.title(ticker)
#     fig.get_figure().savefig('output2.png')