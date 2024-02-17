#  
import pandas as pd
import numpy as np
import yfinance as yf



################################################################################

def print_all_info_of_stocks(stocks_list,post_name='',separator='::'):
    '''
    Muestra por pantalla todas las informaciones de una lista de stoks
    '''
    for stock in stocks_list:
        handler = yf.Ticker(stock.upper()+post_name.upper())
        print('\n\n')
        for keys,values in handler.info.items():
            print(keys+'separator',values)

################################################################################

def get_all_info_of_stock(stocks,post_name=''):
    '''
    Retorna un dict con todos los datos del stock
    '''
    handler = yf.Ticker(stock.upper()+post_name.upper())
    return handler.info;
        
################################################################################

def get_info_of_stocks(stocks_list,labels_list,post_name=''):
    '''
    Retorna un dataframe con informacion de una lista de stocks
    
    Observa los posibles elementos en labels_list usando 
    la funcion get_all_info_of_stock() o print_all_info_of_stocks().
    
    Elementos de ejemplo:
    
    labels_list=[ 'longName',
                  'sector',
                  'currentPrice',
                  'trailingPE',#P/L
                  'trailingEps',#LPA
                  'dividendYield',
                  'beta',
                  ];
    '''
    init=True;
    for stock in stocks_list:
        handler = yf.Ticker(stock.upper()+post_name.upper())
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


