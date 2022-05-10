import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

dati = pd.read_csv('/data/metalm/database_opt.csv',sep=';')

#togliamo LH dai dati
dati = dati.drop(dati[dati.materiale=='F304LH\n'].index) 

# Creazione dataframe colori materiali
colori_materiali =  pd.DataFrame ([['b'],['g'],['r']],
                    index=['F304L1\n','F304LO\n','F304LX\n'],
                    columns=['colore'])


prove = ['Speed variabile','Feed variabile', 'DOC variabile']


for prova in prove:
  
  df_prova = dati[dati.tipo_prova == prova]
  
  materiali = np.unique(df_prova.materiale)
  
  plt.figure()
  
  for materiale in materiali:
    
    df_materiale = df_prova[df_prova.materiale == materiale]
    
    schede = np.unique(df_materiale.sk)
    
    for scheda in schede:
      
      df_scheda = df_materiale[df_materiale.sk == scheda]
      medie_sk = df_scheda.groupby('passata').mean()
      sdt_sk = df_scheda.groupby('passata').std()
      
      colore = str(colori_materiali.loc[materiale,'colore'])
      
      medie_sk.columns = medie_sk.columns.str.lower()
      
      
      listaprova = prova.split()
      tipoprova1 = listaprova[0]
      tipoprova = tipoprova1.lower()
     
      prova_col1 = [col for col in medie_sk.columns if tipoprova in col]
      prova_col = prova_col1[0]
      
      plt.plot(medie_sk[prova_col],medie_sk['kn [n/mm2]'],'-v',label=scheda, color = colore )
  
  plt.legend(loc='best')
  plt.title(prova)
  plt.ylabel('Kn [N/mm2]')
  plt.show()
