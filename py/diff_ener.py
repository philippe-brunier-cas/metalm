import pandas as pd
import numpy as np
import matplotlib.table as tbl
import matplotlib.pyplot as plt

#leggo il file
file_mach = '/data/metalm/database_opt.csv'
df = pd.read_csv(file_mach,sep=';')

#droppo F304LH
df0 = df.drop(df[df.materiale=='F304LH\n'].index,axis=0).reset_index()

#estraggo le features che mi interessano
all_prove = np.unique(df.tipo_prova)
all_colate = np.unique(df.colata)


processed_data = []
for col in all_colate:
    df1 = df0[df0.colata == col].reset_index()
    df1 =df1.drop('level_0',axis=1)
    
    for prova in all_prove:
        if not 'DOE' in prova:
            df2 = df1[df1.tipo_prova==prova].reset_index()
            df2 =df2.drop('level_0',axis=1)
            all_materiali = np.unique(df2.materiale)
            
            for mat in all_materiali:
                
                df3 = df2[df2.materiale==mat].reset_index()
                all_schede = np.unique(df3.sk)
                df3 =df3.drop('level_0',axis=1)
                for scheda in all_schede:
                    df4 = df3[df3.sk==scheda].reset_index()
                    
                    dfg = df4.groupby('passata').mean()
                    
                    # print('%s|%s|%s|%d|%1.2f' %(prova,col, mat[:-1],scheda,dfg['Kn [N/mm2]'].mean()))
                    processed_data.append([prova,col, mat[:-1],scheda,dfg['Kn [N/mm2]'].mean()])

#creo il dataframe dai dati preprocessati
data = pd.DataFrame(processed_data,columns=['prova','colata','materiale','sk','Kn_mean'])

# raggruppo i dati per il barplot
dict_comparativa = {}
for prova in all_prove:
    if not 'DOE' in prova:
        confronto = []
    
        dati_i = data[data.prova == prova]
        dd = dati_i.groupby('materiale').mean().Kn_mean
        
        r = len(dd)
        # print(prova)
        for i in range(1,r):
            # print((dd[i]-dd[0])/dd[0]*100)
            confronto.append((dd[i]-dd[0])/dd[0]*100)
        dict_comparativa[prova] = confronto
    
       
dati = pd.DataFrame(dict_comparativa,index=['F304LO','F304LX'])

#faccio il plot delle differenze di energia
plot = dati.plot.bar(rot=0)

# formatto come 1.2f per rendere leggibile la tabells
dati.update(dati.applymap('{:,.2f}'.format))


# creo la tabella
table = tbl.table(plot, cellText = dati.values.T,
                      cellLoc='center',
                      colLabels = ['',''],
                      rowLabels = ['DOC variabile', 'Feed variabile', 'Speed variabile'],
                      loc ='bottom')
plot.add_table(table)
plot.set_xlabel(xlabel=None)
plot.set_ylabel('delta perc')
plot.set_title('F304L1 \nDifferenze medie percentuali di energia')
plt.savefig('/data/metalm/pics/energy_diff.png')
