#!/usr/bin/python

import pandas as pd

################################################################################
def filter_dataframe(df2, column_str:str,type_list:list):
    '''
    Selecciona en el dataframe df2 todas las filas que tengan algun elemento de
    type_list en la columna column_str. 
    '''
    for n in range(len(type_list)):
        if n==0:
            BOOL=df2[column_str] == type_list[0];
        else:
            BOOL= BOOL | (df2[column_str] == type_list[n]);
    
    df2 = df2.loc[BOOL];

    return df2;
