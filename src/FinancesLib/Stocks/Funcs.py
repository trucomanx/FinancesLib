#  
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.metrics import mutual_info_score

################################################################################

def get_dataframe_of_stocks(stocks_list,labels_list):
  init=True;
  for stock in stocks_list:
    handler = yf.Ticker(stock+'.SA')
    #for keys,values in handler.info.items():
    #  print('['+keys+']',values)

    ddict=dict();
    ddict['name']=[stock];
    for key in labels_list:
      ddict[key]=[''];
      if key in handler.info.keys():
        ddict[key]=[handler.info[key]];
    
    df = pd.DataFrame(ddict);

    if init==True:
      DF=df.copy();
    else:
      DF=pd.concat([DF,df], ignore_index=True);

    init=False;
  return DF;

################################################################################

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

################################################################################

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

################################################################################

import seaborn as sns
import matplotlib.pyplot as plt

def plot_stocks_heatmap(mat,stocks,cmap='gray',fontsize=13,title=''):
    plt.figure(figsize=(15,15))
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
