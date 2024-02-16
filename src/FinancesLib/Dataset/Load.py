#!/usr/bin/python
import pandas as pd

def load_cvs_nubank_rv(filename, active_type='Ação'):
  df2 = pd.read_csv(filename, encoding = "latin_1",sep=None,skiprows=1,engine = 'python')
  
  df2 = df2.loc[df2['TIPO DE INVESTIMENTO'] == active_type];
  df2 = df2[["DESCRIÇÃO","TIPO DE INVESTIMENTO","QUANTIDADE", "VALOR BRUTO"]]

  return df2;
