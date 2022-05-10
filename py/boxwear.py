import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('seaborn')

filename = '/data/metalm/tool_wear.txt'

#leggiamo le colonne separate da |
df = pd.read_csv(filename,sep='|')
#togliamo LH dai dati
df = df.drop(df[df.materiale=='F304LH'].index)  

#boxplot materiale
myplot = df.boxplot(column='wear_time',by='materiale')
myplot.set_ylabel('tempo limite usura [min]')
myplot.set_title('')
myplot.set_xlabel('')
plt.savefig('/data/metalm/output/bwear_mat.png')

#boxplot materiale e scheda
myplot = df.boxplot(column='wear_time',by=['materiale','sk'],rot=90, fontsize=10, figsize=(10, 10))
myplot.set_ylabel('tempo limite usura [min]')
myplot.set_title('')
myplot.set_xlabel('')
plt.savefig('/data/metalm/output/bwear_sk.png')
plt.style.use('default')
