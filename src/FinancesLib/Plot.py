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
    Los datos son agrupados por los tipos (set) encontrados en la columna column_type
    y la altura de las barras se extraen desde la columa column_amount
    '''
    setype  = set(df[column_type])
    dicamount = dict.fromkeys(setype, 0)
    
    Nr=df.shape[0];
    
    for ii in range(Nr):
        dicamount[df[column_type][ii]]=dicamount[df[column_type][ii]]+df[column_amount][ii];
    
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
def plot_bar2_gain_by_type(df,
                 column_type:str,
                 column_amount1:str,
                 column_amount2:str,
                 label_amount1=None,
                 label_amount2=None,
                 en_grid=True,
                 title='',
                 xlabel='Type',
                 ylabel='',
                 legend_loc="upper right",
                 figsize=(10,6),
                 fontsize=13):
    '''
    Crea un grafico de barras extrayendo datos desde el dataframe df.
    Los datos son agrupados por los tipos (set) encontrados en la columna column_type
    y la altura de las barras se extraen desde las columas column_amount1 y column_amount2
    '''
    setype  = set(df[column_type])
    dicamount1 = dict.fromkeys(setype, 0)
    dicamount2 = dict.fromkeys(setype, 0)
    
    if label_amount1==None:
        label_amount1=str(column_amount1);
        
    if label_amount2==None:
        label_amount2=str(column_amount2);
    
    Nr=df.shape[0];
    
    for ii in range(Nr):
        dicamount1[df[column_type][ii]]=dicamount1[df[column_type][ii]]+df[column_amount1][ii];
        dicamount2[df[column_type][ii]]=dicamount2[df[column_type][ii]]+df[column_amount2][ii];
    
    types=[];
    amounts1=[];
    amounts2=[];
    for key,value in dicamount1.items():
        types.append(key);
        amounts1.append(value);
        amounts2.append(dicamount2[key]);
    
    X = np.arange(len(types))  # the label locations
    width = 0.4  # the width of the bars
    
    TOT=np.sum(np.array(amounts1));
    
    plt.figure(figsize=figsize)
    plt.bar(X    , amounts1,width=width,label=label_amount1)
    plt.bar(X+width/2.0, amounts2,width=width,label=label_amount2)
    for n in range(len(types)):
        plt.annotate(   str(round(100*(amounts1[n]/amounts2[n]-1),1))+'%',
                        (X[n],amounts1[n]),
                        fontsize=fontsize,
                        ha='center');
    plt.legend(loc=legend_loc)
    plt.rcParams.update({'font.size': fontsize})
    plt.ylabel(ylabel,fontsize=fontsize)
    plt.xlabel(xlabel,fontsize=fontsize)
    plt.xticks(X, types)
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


