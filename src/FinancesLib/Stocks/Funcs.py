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
            print(keys+separator,values)

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

################################################################################

def add_info_of_stocks(df_in,column_name,post_name='',
                       longname=True,
                       sector=True,
                       price=True,
                       pl=True,
                       lpa=True,
                       pvp=True,
                       dy=True,
                       beta=True):
    '''

    '''

    N=df_in.shape[0];

    df=df_in.reset_index(drop=True);

    if longname==True:
        df['longName']=['']*N;
    if sector==True:
        df['sector']=['']*N;
    if price==True:
        df['price']=[np.nan]*N;
    if pl==True:
        df['pl']=[np.nan]*N;
    if lpa==True:
        df['lpa']=[np.nan]*N;
    if pvp==True:
        df['pvp']=[np.nan]*N;
    if dy==True:
        df['dy%']=[0.0]*N;
    if beta==True:
        df['beta']=[np.nan]*N;

    for n in range(N):
        handler = yf.Ticker(df.at[n,column_name].upper()+post_name.upper())
      
        if longname==True and 'longName' in handler.info.keys():
            df.loc[n,'longName']=handler.info['longName'];

        if sector==True and 'sector' in handler.info.keys():
            df.loc[n,'sector']=handler.info['sector'];

        if price==True and 'currentPrice' in handler.info.keys():
            df.loc[n,'price']=float(handler.info['currentPrice']);

        if pl==True and 'trailingPE' in handler.info.keys():
            df.loc[n,'pl']=float(handler.info['trailingPE']);

        if lpa==True and 'trailingEps' in handler.info.keys():
            df.loc[n,'lpa']=float(handler.info['trailingEps']);
        
        if pvp==True and 'priceToBook' in handler.info.keys():
            df.loc[n,'pvp']=float(handler.info['priceToBook']);

        if dy==True and 'trailingAnnualDividendYield' in handler.info.keys():
            df.loc[n,'dy%']=float(handler.info['trailingAnnualDividendYield'])*100;

        if beta==True and 'beta' in handler.info.keys():
            df.loc[n,'beta']=float(handler.info['beta']);

    return df;


