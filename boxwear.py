import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('seaborn')

filename = '/data/tool_wear_304.txt'

df = pd.read_csv(filename,sep='|')
df = df.drop(df[df.materiale=='F304LH'].index)

myplot = df.boxplot(column='time',by='materiale')
myplot.set_ylabel('tempo limite usura [min]')
myplot.set_title('')
myplot.set_xlabel('')
plt.savefig('bwear_mat.png')


myplot = df.boxplot(column='time',by=['materiale','sk'],rot=90)
myplot.set_ylabel('tempo limite usura [min]')
myplot.set_title('')
myplot.set_xlabel('')
plt.savefig('bwear_sk.png')
plt.style.use('default')

