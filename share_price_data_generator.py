# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 14:46:21 2020

@author: DELL
"""
import pandas as pd
import yfinance as yf
import yahoofinancials 
from datetime import datetime,timedelta

date_last_train = (datetime.today()-timedelta(weeks = 26)).strftime('%Y-%m-%d')
date_begin_train = (datetime.today() - timedelta(weeks = 520)).strftime('%Y-%m-%d')

date_last_test = datetime.today().strftime('%Y-%m-%d')
date_begin_test = (datetime.today() - timedelta(weeks = 26)).strftime('%Y-%m-%d')

yahoo_financials = yahoofinancials.YahooFinancials('INFY.NS')

data_train = yahoo_financials.get_historical_price_data(start_date=date_begin_train, 
                                                  end_date=date_last_train, 
                                                  time_interval='daily')
data_test = yahoo_financials.get_historical_price_data(start_date=date_begin_test, 
                                                  end_date=date_last_test, 
                                                  time_interval='daily')

train_df = pd.DataFrame(data_train['INFY.NS']['prices'])
train_df = train_df.drop('date', axis=1).set_index('formatted_date')
train_df = train_df.rename(columns = {'open' : 'Open'})

test_df = pd.DataFrame(data_test['INFY.NS']['prices'])
test_df = test_df.drop('date', axis=1).set_index('formatted_date')
test_df = test_df.rename(columns = {'open' : 'Open'})

train_df.to_csv('share_price_train.csv')
test_df.to_csv('share_price_test.csv')

