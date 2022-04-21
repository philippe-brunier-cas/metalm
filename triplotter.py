import pandas as pd
import ternary
import numpy as np
import matplotlib.pyplot as plt
# from trplt import *

def trplt(df,mode,savepic):
  # Scatter Plot ternario
  # mode sono le marche o le schede
  # savepic è il nome di com voglio il png
  
  
  
  plt.style.use('seaborn')
  scale = 100
  size = 30
  figure, tax = ternary.figure(scale=scale)
  figure.set_size_inches(15, 15)
  
  colori = ['r','b','g','m','orange','lime','indigo', 'cyan','navy','k','sienna', 'purple', 'teal', 'grey', 'maroon', 'gold', 'hotpink', 'coral', 'tan', 'azure']
  i = 0

  for tt in list(np.unique(df[mode])):
    dfi = df[df[mode] == tt].reset_index()
    # Plot a few different styles with a legend
    dfii = dfi[dfi.kind == 'D'].reset_index()
    points = dfii[['AL2O3_p','SIO2_p','CAO_p']].values
    tax.scatter(points, marker='o',s=size,c=colori[i], label=tt+'| D type')
  
    dfii = dfi[dfi.kind == 'B-C'].reset_index()
    points = dfii[['AL2O3_p','SIO2_p','CAO_p']].values
    tax.scatter(points, marker='s',s=size,c=colori[i], label=tt+'| B-C type')
    
    i += 1
    
  tax.legend(bbox_to_anchor=(0, 1), fontsize=10)
  tax.set_title("inclusion ternary plot", fontsize=25)
  
  # Set Axis labels and Title
  fontsize = 15
  tax.left_axis_label('SiO2 [%wt]', fontsize=fontsize, offset=0.1)
  tax.right_axis_label('CaO [%wt]', fontsize=fontsize, offset=0.1)
  tax.bottom_axis_label('Al2O3 [%wt]', fontsize=fontsize, offset=0.01)
  
  tax.boundary(linewidth=2.0)
  tax.gridlines(multiple=5, color="blue")
  tax.ticks(axis='lbr', linewidth=1, multiple=5)
  tax.clear_matplotlib_ticks()
  tax.get_axes().axis('off')
  
  tax.savefig ('/data/metalm/output/%s.png' %savepic)
  tax.close()
  plt.style.use('default')



path_data = '/data/metalm/tabella_ox.txt'
df = pd.read_csv(path_data, sep = '\t')

df['SK'] = df['SK'].astype(str)
df['col'] = df['col'].astype(str)

df['AL2O3_p']=df.AL2O3_i*100
df['SIO2_p'] = df.SIO2_i*100
df['CAO_p'] = df.CAO_i*100

trplt(df,'materiale','mat')
trplt(df,'col','col')
trplt(df,'SK','sk')
