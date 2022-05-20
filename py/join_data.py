import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plt.style.use('seaborn')

def JoinData(file_mach,file_ox,file_wear,file_met):

    df_mach = pd.read_csv(file_mach,sep=';')
    df_ox = pd.read_csv(file_ox,sep='\t')
    df_wear = pd.read_csv(file_wear,sep='|')
    df_met = pd.read_csv(file_met,sep=';',na_values='na')
    df_met = df_met[df_met.SK!='na']
    
    # dal momento che raggruppo per schede, e 
    # che alcuni df hanno dati ripetuti, faccio un prepocessing
    # raggruppando per SK. sk sarà il mio nuovo indice per i join
    # carico tutto in dfw

    #df_wear
    dfw = df_wear.groupby('sk').mean()
    dfs = df_wear.groupby('sk').std()
    dfc = df_wear.groupby('sk').count()
    
    dfw[['std_F0','std_Fmax','std_wear_time']] = dfs[['F0','Fmax','wear_time']]
    dfw['wear_count'] = dfc['F0']
    
    #df_ox
    dfo = df_ox.groupby('SK').mean()
    dfs = df_ox.groupby('SK').std()
    dfc = df_ox.groupby('SK').count()
    
    dfw[['AL2O3_mean','SIO2_mean','CAO_mean']] = dfo[['AL2O3_i','SIO2_i','CAO_i']]
    # dfm['metallurcial_count'] = dfc['col']
    
    dfw['dF_perc'] = (dfw.Fmax-dfw.F0)/dfw.F0*100

    #df_met
    dfm = df_met.groupby('SK').mean()
    dfs = df_met.groupby('SK').std()
    dfc = df_met.groupby('SK').count()
    
    features = ['C', 'S', 'P', 'SI', 'MN', 'CR', 'NI', 'MO', 'CU', 'SN', 'V',
           'W', 'CO', 'TI', 'NB', 'N2', 'O2 ', 'area', 'k2_OA', 'k2_OS', 'k2_OG',
           'k3_OA', 'k3_OS', 'k3_OG', 'As', 'Ag', 'Affs', 'Bs', 'Bg', 'Bffs', 'Cs',
           'Cg', 'Cffs', 'Ds', 'Dg', 'Dffs', 'rm_[Mpa]', 'rp_02_[Mpa]']
    
    dfw[features] = dfm[features]
    
    
    dfw = dfw.reset_index()
    dfw['Fmax/F0'] = dfw.Fmax/dfw.F0
    dfw['dF'] = dfw['Fmax/F0'] - 1
    mat = []
    for i in range(0,len(dfw.col)):
        mat.append(np.unique(df_wear[df_wear.col==dfw.col[i]].materiale.values)[0])
    
    dfw['materiale'] = mat
    
    
    
    
    dfw = dfw.dropna()
    #salvo i dati come csv
    
    dfw.to_csv('dbmm.csv',sep='|',index=False)
    return dfw

plt.style.use('default')

file_mach = '/data/metalm/database_opt.csv'
file_ox = '/data/metalm/tabella_ox.txt'
file_wear = '/data/metalm/tool_wear.txt'
file_met = '/data/metalm/metallurgical.csv'

df_mach = pd.read_csv(file_mach,sep=';')
df_ox = pd.read_csv(file_ox,sep='\t')
df_wear = pd.read_csv(file_wear,sep='|')
df_met = pd.read_csv(file_met,sep=';',na_values='na')
df_met = df_met[df_met.sk!='na']

# dal momento che raggruppo per schede, e 
# che alcuni df hanno dati ripetuti, faccio un prepocessing
# raggruppando per SK. sk sarà il mio nuovo indice per i join
# carico tutto in dfw

#df_wear
dfw = df_wear.groupby('sk').mean()
dfs = df_wear.groupby('sk').std()
dfc = df_wear.groupby('sk').count()

dfw[['std_F0','std_Fmax','std_wear_time']] = dfs[['F0','Fmax','wear_time']]
dfw['wear_count'] = dfc['F0']

#df_ox
dfo = df_ox.groupby('SK').mean()
dfs = df_ox.groupby('SK').std()
dfc = df_ox.groupby('SK').count()

dfw[['AL2O3_mean','SIO2_mean','CAO_mean']] = dfo[['AL2O3_i','SIO2_i','CAO_i']]
# dfm['metallurcial_count'] = dfc['col']

dfw['dF_perc'] = (dfw.Fmax-dfw.F0)/dfw.F0*100
print('b')

#df_met
dfm = df_met.groupby('SK').mean()
dfs = df_met.groupby('SK').std()
dfc = df_met.groupby('SK').count()

features = ['C', 'S', 'P', 'SI', 'MN', 'CR', 'NI', 'MO', 'CU', 'SN', 'V',
       'W', 'CO', 'TI', 'NB', 'N2', 'O2 ', 'area', 'k2_OA', 'k2_OS', 'k2_OG',
       'k3_OA', 'k3_OS', 'k3_OG', 'As', 'Ag', 'Affs', 'Bs', 'Bg', 'Bffs', 'Cs',
       'Cg', 'Cffs', 'Ds', 'Dg', 'Dffs', 'rm_[Mpa]', 'rp_02_[Mpa]']

dfw[features] = dfm[features]


dfw = dfw.reset_index()
dfw['Fmax/F0'] = dfw.Fmax/dfw.F0
dfw['dF'] = dfw['Fmax/F0'] - 1
mat = []
for i in range(0,len(dfw.col)):
    mat.append(np.unique(df_wear[df_wear.col==dfw.col[i]].materiale.values)[0])

dfw['materiale'] = mat




dfw = dfw.dropna()
