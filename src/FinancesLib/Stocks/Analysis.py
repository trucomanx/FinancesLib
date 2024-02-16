#!/usr/bin/python

import numpy as np
import yfinance as yf
from sklearn.metrics import mutual_info_score
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

################################################################################
def plot_bar_by_type(df,
                 column_type_str,
                 column_amount_str,
                 cmap='jet',
                 en_grid=True,
                 title='',xlabel='Type',ylabel='',figsize=(10,6),fontsize=13):
    setype  = set(df[column_type_str])
    dicamount = dict.fromkeys(setype, 0)
    
    Nr=df.shape[0];
    
    for id in range(Nr):
        dicamount[df[column_type_str][id]]=dicamount[df[column_type_str][id]]+df[column_amount_str][id];
    
    chd = matplotlib.colormaps[cmap];
    types=[];
    amounts=[];
    for key,value in dicamount.items():
        types.append(key);
        amounts.append(value);

    
    MAX=np.max(np.array(amounts));
    MIN=np.min(np.array(amounts));
    TOT=np.sum(np.array(amounts));

    colors=[];
    for n in range(len(types)):
        rgba = chd((amounts[n]-MIN)/(MAX-MIN));
        colors.append(rgba);

    plt.figure(figsize=figsize)
    plt.bar(types, amounts,color=colors)
    for xt,yt in zip(types,amounts):
        plt.annotate(str(round(100*yt/TOT,1))+'%',(xt,yt),fontsize=fontsize)
    plt.rcParams.update({'font.size': fontsize})
    plt.ylabel(ylabel,fontsize=fontsize)
    plt.xlabel(xlabel,fontsize=fontsize)
    plt.title(title,fontsize=fontsize)
    plt.grid(en_grid)
    plt.show()
    
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



def plot_stocks_heatmap(mat,stocks,cmap='jet',fontsize=13,title='',figsize=(14,14),fmt=".1f",percentage=True):
    MAT=mat.copy();
    if percentage==True:
        MAT=mat*100;
    
    plt.figure(figsize=figsize)
    sns.heatmap(MAT, 
                annot=True,
                fmt=fmt, 
                cmap=cmap,#"jet",
                xticklabels=stocks,
                yticklabels=stocks)
    plt.ylabel('stocks',fontsize=fontsize)
    plt.xlabel('stocks',fontsize=fontsize)
    plt.title(title,fontsize=fontsize)
    plt.show()


