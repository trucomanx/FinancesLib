#!/usr/bin/python

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

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
                        labels,
                        xlabel='labels',
                        ylabel='labels',
                        cmap='jet',
                        title='',
                        fontsize=13,
                        figsize=(14,14),
                        fmt=".1f",
                        percentage=True):
    MAT=mat.copy();
    if percentage==True:
        MAT=mat*100;
    
    plt.figure(figsize=figsize)
    sns.heatmap(MAT, 
                annot=True,
                fmt=fmt, 
                cmap=cmap,#"jet",
                xticklabels=labels,
                yticklabels=labels)
    plt.ylabel(xlabel,fontsize=fontsize)
    plt.xlabel(xlabel,fontsize=fontsize)
    plt.title(title,fontsize=fontsize)
    plt.show()


