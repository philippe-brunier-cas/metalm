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

materiali = np.unique(dati.materiale)

#prove = ['Speed variabile','Feed variabile', 'DOC variabile']

prove = ['speed [m/min]', 'feed [mm/rev]', 'DOC [mm]']

schede = np.unique(dati.sk)

for prova in prove:
  
  df_prova = dati[dati.tipo_prova == prova]
  
  plt.figure()
  
  for materiale in materiali:
    
    df_materiale = df_prova[df_prova.materiale == materiale]
    
    for scheda in schede:
      print(scheda,materiale,prova)
      df_scheda = df_materiale[df_materiale.sk == scheda]
      medie_sk = df_scheda.groupby('passata').mean()
      sdt_sk = df_scheda.groupby('passata').std()
      
      plt.plot(medie_sk[prova],medie_sk['Kn [N/mm2]'],'-v',label=scheda,color=colori_materiali[] )
      
