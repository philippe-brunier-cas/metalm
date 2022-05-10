import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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

#calcolo medie per materiale

materiali=list(np.unique(df.materiale))

dfa = pd.DataFrame()

all_count = []
all_mean = []
all_std = []
all_mat = []
for mat in materiali:
  media=df[df.materiale==mat].wear_time.mean()
  std=df[df.materiale==mat].wear_time.std()
  count=df[df.materiale==mat].wear_time.count()
  print(mat,media,std,count)
  all_mean.append(media)
  all_std.append(std)
  all_count.append(count)
  all_mat.append(mat)

dfa['materiale'] = all_mat  
dfa['media_wear'] = all_mean
dfa['media_std'] = all_std
dfa['media_cont'] = all_count


L1=float(dfa[dfa.materiale=='F304L1'].media_wear)
dfa['diff_perc1']=((dfa.media_wear-L1)/L1)*100

dfa.to_csv('/data/metalm/output/resumed_usura.txt',sep='|', float_format='%1.2f', index=False)



#boxplot materiale e scheda
myplot = df.boxplot(column='wear_time',by=['materiale','sk'],rot=90, fontsize=10, figsize=(10, 10))
myplot.set_ylabel('tempo limite usura [min]')
myplot.set_title('')
myplot.set_xlabel('')
plt.savefig('/data/metalm/output/bwear_sk.png')
plt.style.use('default')
