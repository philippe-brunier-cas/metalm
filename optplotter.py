import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

## grouped by materiale
dati = pd.read_csv('/data/metalm/database_opt.csv',sep=';')

all_prove = ['Speed variabile','Feed variabile', 'DOC variabile']

materiali = np.unique(dati.materiale)
prove = np.unique(dati.tipo_prova)

for prova in all_prove:
    
    dfp = dati[dati.tipo_prova == prova].reset_index()
    
    plt.figure()
    
    for mat in materiali:
        dfm = dfp[dfp.materiale == mat].reset_index()
        dfg = dfm.groupby('passata').mean()
        
        if 'Speed' in prova:
            xx = dfg['speed [m/min]']
            xlab = 'speed [m/min]'
        elif 'Feed' in prova:
            xx = dfg['feed [mm/rev]']
            xlab = 'feed [mm/rev]'

        elif 'DOC' in prova:
            xx = dfg['DOC [mm]']
            xlab = 'DOC [mm]'

        else:
            xx = range(0,dfg.shape[0])
            xlab = 'sequence'
            
        err = dfg['std_dev_Fn[%]']/100/2*dfg['Kn [N/mm2]']
        plt.plot(xx,dfg['Kn [N/mm2]'],'-v',label=mat)
        plt.fill_between(xx,dfg['Kn [N/mm2]']-err,dfg['Kn [N/mm2]']+err,alpha=0.3)

    plt.legend(loc='best')
    plt.title(prova)
    plt.ylabel('Kn [N/mm2]')
    plt.xlabel(xlab)
    plt.savefig('/data/metalm/output/'+prova+'.png')
## MATERIALI con tutte le schede

dati = pd.read_csv('/data/metalm/database.csv',sep=';')

prova = 'Speed variabile'

materiali = np.unique(dati.materiale)

dati = dati[dati.tipo_prova == prova]
# plt.figure()

for mat in materiali:
    df0 = dati[dati.materiale == mat]
    plt.figure()
    schede = np.unique(df0.sk)
    for scheda in schede:
        df = df0[df0.sk == scheda]
        df2 = df.groupby('passata').mean()
        # print(df2['Fn [N]'])
        plt.plot(df2['speed [m/min]'],df2['Kn [N/mm2]'],'-v',label=scheda)
        yerr = df2['std_dev_Fn[%]']/100*df2['Fn [N]']/2
        plt.fill_between(df2['speed [m/min]'],df2['Kn [N/mm2]']-yerr,df2['Kn [N/mm2]']+yerr,alpha=0.3)

    plt.xlabel('speed [m/min]')
    plt.ylabel('Kn [N/mm2]')
    plt.legend(loc = 'best')
    plt.title(mat+prova)   
    plt.savefig('/data/metalm/output/'+mat[0:6]+'speed.png')


dati = pd.read_csv('/data/metalm/database.csv',sep=';')

prova = 'Feed variabile'

materiali = np.unique(dati.materiale)

dati = dati[dati.tipo_prova == prova]
# plt.figure()

for mat in materiali:
    df0 = dati[dati.materiale == mat]
    plt.figure()
    schede = np.unique(df0.sk)
    for scheda in schede:
        df = df0[df0.sk == scheda]
        df2 = df.groupby('passata').mean()
        # print(df2['Fn [N]'])
        plt.plot(df2['feed [mm/rev]'],df2['Kn [N/mm2]'],'-v',label=scheda)
        yerr = df2['std_dev_Fn[%]']/100*df2['Kn [N/mm2]']/2
        plt.fill_between(df2['feed [mm/rev]'],df2['Kn [N/mm2]']-yerr,df2['Kn [N/mm2]']+yerr,alpha=0.3)

    plt.xlabel('feed [mm/rev]')
    plt.ylabel('Kn [N/mm2]')
    
    plt.legend(loc = 'best')
    plt.title(mat+prova)     
    plt.savefig('/data/metalm/output/'+mat[0:6]+'feed.png')

dati = pd.read_csv('/data/metalm/database.csv',sep=';')

prova = 'DOC variabile'

materiali = np.unique(dati.materiale)

dati = dati[dati.tipo_prova == prova]
# plt.figure()

for mat in materiali:
    df0 = dati[dati.materiale == mat]
    plt.figure()
    schede = np.unique(df0.sk)
    for scheda in schede:
        df = df0[df0.sk == scheda]
        df2 = df.groupby('passata').mean()
        # print(df2['Fn [N]'])
        plt.plot(df2['DOC [mm]'],df2['Kn [N/mm2]'],'-v',label=scheda)
        yerr = df2['std_dev_Fn[%]']/100*df2['Kn [N/mm2]']/2
        plt.fill_between(df2['DOC [mm]'],df2['Kn [N/mm2]']-yerr,df2['Kn [N/mm2]']+yerr,alpha=0.2)

    plt.xlabel('DOC [mm]')
    plt.ylabel('Kn [N/mm2]')
    
    plt.legend(loc = 'best')
    plt.title(mat+prova)     
    plt.savefig('/data/metalm/output/'+mat[0:6]+'doc.png')

plt.style.use('default')
