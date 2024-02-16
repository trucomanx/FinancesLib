#!/usr/bin/python
import pandas as pd

def load_cvs_nubank_rv(filename, active_type='Ação'):
    df2 = pd.read_csv(  filename, 
                        encoding = "latin_1",
                        sep=None,
                        skiprows=1,
                        engine = 'python',
                        decimal=",", 
                        thousands="."
                        )
    
    df2 = df2.loc[df2['TIPO DE INVESTIMENTO'] == active_type];
    df2 = df2[["DESCRIÇÃO","TIPO DE INVESTIMENTO","QUANTIDADE","VALOR BRUTO"]]
  
    df2["VALOR BRUTO"]=df2["VALOR BRUTO"].str.replace('R\\$', '',regex=True).str.replace('.' , '',regex=True).str.replace(',' , '.',regex=True).astype(float);
  
  #df2["QUANTIDADE"] = pd.to_numeric(df2["QUANTIDADE"])

    return df2;
