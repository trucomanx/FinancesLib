#!/usr/bin/python

import numpy as np
import yfinance as yf
from sklearn.metrics import mutual_info_score


################################################################################

def get_corr_matrix(stock_list,period="24mo",post_name='',verbose=True):
    '''
    Retorna la matriz de correlacion de los precios de cada un de las acciones de 
    una lista de acciones stock_list.
    '''
    hist=dict();
    for stock in stock_list:
        handler = yf.Ticker(stock.upper()+post_name.upper())
        hist[stock]=handler.history(period=period);
      
    C=np.zeros((len(stock_list),len(stock_list)));
    
    for n1 in range(len(stock_list)):
        for n2 in range(len(stock_list)):
            x1=hist[stock_list[n1]]['Open'].to_numpy();
            x2=hist[stock_list[n2]]['Open'].to_numpy();
            
            if (x1.size>0) and (x2.size>0):
                L=x1.size;
                if x1.size!=x2.size:
                    if verbose:
                        print(stock_list[n1],x1.size,stock_list[n2],x2.size)
                    L=min(x1.size,x2.size);
                    x1=x1[-L:];
                    x2=x2[-L:];

                BOOL=np.isnan(x1)|np.isnan(x2);
                x1 = x1[~BOOL];
                x2 = x2[~BOOL];
                C[n1,n2]=np.corrcoef(x1,x2)[0,1];
            else:
                if verbose:
                    print(stock_list[n1],x1.size,stock_list[n2],x2.size)
                C[n1,n2]=0.0;
    return C;

################################################################################

def calc_MI(x, y, nbins):
    c_xy = np.histogram2d(x, y, nbins)[0]
    
    mi = mutual_info_score(None, None, contingency=c_xy)
    return mi

def get_nmi_matrix(stock_list,period="24mo",post_name='',nbins=8,verbose=True):
    '''
    Retorna la matriz de informacion mutua de los precios de cada un de las acciones de 
    una lista de acciones stock_list.
    Los datos son discretizado en un histograma con un numero de bins igual a nbins.
    '''
    hist=dict();
    for stock in stock_list:
        handler = yf.Ticker(stock.upper()+post_name.upper())
        hist[stock]=handler.history(period=period);
      
    C=np.zeros((len(stock_list),len(stock_list)));
    
    for n1 in range(len(stock_list)):
        for n2 in range(len(stock_list)):
            x1=hist[stock_list[n1]]['Open'].to_numpy();
            x2=hist[stock_list[n2]]['Open'].to_numpy();
        
            if (x1.size>0) and (x2.size>0):
                L=x1.size;
                if x1.size!=x2.size:
                    if verbose:
                        print(stock_list[n1],x1.size,stock_list[n2],x2.size)
                    L=min(x1.size,x2.size);
                    x1=x1[-L:];
                    x2=x2[-L:];
                BOOL=np.isnan(x1)|np.isnan(x2);
                x1 = x1[~BOOL];
                x2 = x2[~BOOL];
                C[n1,n2]=calc_MI(x1,x2,nbins);
            else:
                if verbose:
                    print(stock_list[n1],x1.size,stock_list[n2],x2.size)
                C[n1,n2]=0.0;
        
    return C/np.max(C);



