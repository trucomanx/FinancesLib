#!/usr/bin/python

import numpy as np
import yfinance as yf
from sklearn.metrics import mutual_info_score

################################################################################

def get_corr_matrix(stock_list,period="24mo",post_name=''):

    hist=dict();
    for stock in stock_list:
      handler = yf.Ticker(stock.upper()+post_name.upper())
      hist[stock]=handler.history(period=period);
      
    C=np.zeros((len(stock_list),len(stock_list)));
    
    for n1 in range(len(stock_list)):
      for n2 in range(len(stock_list)):
        x1=hist[stock_list[n1]]['Open'].to_numpy();
        x2=hist[stock_list[n2]]['Open'].to_numpy();
        
        if (x1.size>0) and (x1.size>0):
            L=x1.size;
            if x1.size!=x2.size:
                L=min(x1.size,x2.size);
            C[n1,n2]=np.corrcoef(x1[0:L],x2[0:L])[0,1];
        else:
            C[n1,n2]=0.0;
    return C;

################################################################################

def calc_MI(x, y, bins):
    c_xy = np.histogram2d(x, y, bins)[0]
    
    mi = mutual_info_score(None, None, contingency=c_xy)
    return mi

def get_nmi_matrix(stock_list,period="24mo",post_name='',bins=8):

    hist=dict();
    for stock in stock_list:
      handler = yf.Ticker(stock.upper()+post_name.upper())
      hist[stock]=handler.history(period=period);
      
    C=np.zeros((len(stock_list),len(stock_list)));
    
    for n1 in range(len(stock_list)):
      for n2 in range(len(stock_list)):
        x1=hist[stock_list[n1]]['Open'].to_numpy();
        x2=hist[stock_list[n2]]['Open'].to_numpy();
        
        if (x1.size>0) and (x1.size>0):
            L=x1.size;
            if x1.size!=x2.size:
                L=min(x1.size,x2.size);
            C[n1,n2]=calc_MI(x1[0:L],x2[0:L],bins);
        else:
            C[n1,n2]=0.0;
        
    return C/np.max(C);

################################################################################

import seaborn as sns
import matplotlib.pyplot as plt

def plot_stocks_heatmap(mat,stocks,cmap='gray',fontsize=13,title='',figsize=(14,14)):
    plt.figure(figsize=figsize)
    sns.heatmap(mat, 
                annot=True,
                fmt='g', 
                cmap=cmap,#"jet",
                xticklabels=stocks,
                yticklabels=stocks)
    plt.ylabel('stocks',fontsize=fontsize)
    plt.xlabel('stocks',fontsize=fontsize)
    plt.title(title,fontsize=fontsize)
    plt.show()
