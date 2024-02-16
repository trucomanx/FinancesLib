#!/usr/bin/python
import pandas as pd

def load_cvs_nubank_rv(filename, active_type_list=['Ação']):
    df2 = pd.read_csv(  filename, 
                        encoding = "latin_1",
                        sep=None,
                        skiprows=1,
                        engine = 'python',
                        decimal=",", 
                        thousands="."
                        )
    
    for n in range(len(active_type_list)):
        if n==0:
            BOOL=df2['TIPO DE INVESTIMENTO'] == active_type_list[0];
        else:
            BOOL= BOOL | (df2['TIPO DE INVESTIMENTO'] == active_type_list[n]);
    df2 = df2.loc[BOOL];
    df2 = df2[["DESCRIÇÃO","TIPO DE INVESTIMENTO","QUANTIDADE","VALOR BRUTO"]]
  
    df2["VALOR BRUTO"]=df2["VALOR BRUTO"].str.replace('R\\$', '',regex=True).str.replace('.' , '',regex=True).str.replace(',' , '.',regex=True).astype(float);
  
  #df2["QUANTIDADE"] = pd.to_numeric(df2["QUANTIDADE"])

    return df2;
    
#print(load_cvs_nubank_rv('/home/fernando/Downloads/Exportar_custodia_2024-02-16.csv', active_type_list=['Ação','BDR']));
