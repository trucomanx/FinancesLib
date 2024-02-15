#  

import numpy as np
import yfinance as yf
from sklearn.metrics import mutual_info_score

def get_corr_matrix(stock_list,period="24mo",post_name='.SA'):

    hist=dict();
    for stock in stock_list:
      handler = yf.Ticker(stock.upper()+post_name.upper())
      hist[stock]=handler.history(period=period);
      
    C=np.zeros((len(stock_list),len(stock_list)));
    
    for n1 in range(len(stock_list)):
      for n2 in range(len(stock_list)):
        x1=hist[stock_list[n1]]['Open'].to_numpy();
        x2=hist[stock_list[n2]]['Open'].to_numpy();

        C[n1,n2]=np.corrcoef(x1,x2)[0,1];
    return C;


def calc_MI(x, y, bins):
    c_xy = np.histogram2d(x, y, bins)[0]
    
    mi = mutual_info_score(None, None, contingency=c_xy)
    return mi


def get_nmi_matrix(stock_list,period="24mo",post_name='.SA',bins=8):

    hist=dict();
    for stock in stock_list:
      handler = yf.Ticker(stock.upper()+post_name.upper())
      hist[stock]=handler.history(period=period);
      
    C=np.zeros((len(stock_list),len(stock_list)));
    
    for n1 in range(len(stock_list)):
      for n2 in range(len(stock_list)):
        x1=hist[stock_list[n1]]['Open'].to_numpy();
        x2=hist[stock_list[n2]]['Open'].to_numpy();

        C[n1,n2]=calc_MI(x1,x2,bins);
        
    return C/np.max(C);


