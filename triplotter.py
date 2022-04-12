import pandas as pd
import ternary

def trnplt(df):
  # Scatter Plot
  scale = 100
  figure, tax = ternary.figure(scale=scale)
  figure.set_size_inches(15, 15)
  # Plot a few different styles with a legend
  points = df[['AL2O3_p','SIO2_p','CAO_p']].values
  tax.scatter(points, marker='s', color='red', label="Red Squares")
  points = random_points(30, scale=scale)
  tax.scatter(points, marker='D', color='green', label="Green Diamonds")
  tax.legend()
  
  tax.set_title("Plot", fontsize=20)
  tax.boundary(linewidth=2.0)
  tax.gridlines(multiple=5, color="blue")
  tax.ticks(axis='lbr', linewidth=1, multiple=5)
  tax.clear_matplotlib_ticks()
  tax.get_axes().axis('off')
  
  tax.show()
  return None

path_data = '/data/tabella_ox.txt'
df = pd.read_csv(path_data, sep = '\t')
df['AL2O3_p']=df.AL2O3_i*100
df['SIO2_p'] = df.SIO2_i*100
df['CAO_p'] = df.CAO_i*100
