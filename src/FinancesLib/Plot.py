#!/usr/bin/python

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

################################################################################
def plot_bar_by_type(df,
                 column_type:str,
                 column_amount:str,
                 cmap='jet',
                 en_grid=True,
                 title='',xlabel='Type',ylabel='',figsize=(10,6),fontsize=13):
    '''
    Crea un grafico de barras extrayendo datos desde el dataframe df.
    Los datos so agrupados por los tipos (set) encontrados en la columna column_type
    y la altura de las barras se extraen desde la columan column_amount
    '''
    setype  = set(df[column_type])
    dicamount = dict.fromkeys(setype, 0)
    
    Nr=df.shape[0];
    
    for id in range(Nr):
        dicamount[df[column_type][id]]=dicamount[df[column_type][id]]+df[column_amount][id];
    
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
        plt.annotate(   str(round(100*yt/TOT,1))+'%',
                        (xt,yt),
                        fontsize=fontsize,
                        ha='center');
    plt.rcParams.update({'font.size': fontsize})
    plt.ylabel(ylabel,fontsize=fontsize)
    plt.xlabel(xlabel,fontsize=fontsize)
    plt.title(title,fontsize=fontsize)
    plt.grid(en_grid)
    plt.show()


################################################################################

def plot_matrix_heatmap(mat,
                        labelsx:list,
                        labelsy:list,
                        xlabel='labels',
                        ylabel='labels',
                        cmap='jet',
                        title='',
                        fontsize=13,
                        figsize=(14,14),
                        fmt=".1f",
                        percentage=True):
    '''
    Crea un heatmap con los datos de la matriz map.
    las etiquetas de las lineas y columnas estan agrupadas en las listas labelsx y labelsy, respectivamente.
    '''
    
    MAT=mat.copy();
    if percentage==True:
        MAT=mat*100;
    
    plt.figure(figsize=figsize)
    sns.heatmap(MAT, 
                annot=True,
                fmt=fmt, 
                cmap=cmap,#"jet",
                xticklabels=labelsx,
                yticklabels=labelsy)
    plt.ylabel(xlabel,fontsize=fontsize)
    plt.xlabel(xlabel,fontsize=fontsize)
    plt.title(title,fontsize=fontsize)
    plt.show()


