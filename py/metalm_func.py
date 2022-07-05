import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

def OLSmodel(df,feature_x,feature_y):
    
    print('x -> ',feature_x)
    print('y ->',feature_y)
    
    x = df[feature_x].values
    y = df[feature_y].values
    
    x = sm.add_constant(x)

    model_sm = sm.OLS(y,x)
    results = model_sm.fit()
    print(results.summary())
    return None


def MultipleLinearRegression(df,feature_x,feature_y):
  plt.style.use('seaborn')
  
  feature_x = list(dcorr.index)
  feature_y = 'tempo_usura'
  
  x = df[feature_x].values
  y = df[feature_y].values
  
  # reshape dei dati necessario per il fit
  # perche al momento sono array(L,) e devono diventare array(L,1)
  
  model = LinearRegression().fit(x, y)
  r_sq = model.score(x, y)
  print('modello lineare a più variabili')
  print('x = ',feature_x)
  print('y = ' ,feature_y)
  
  # print('y = m*x + q')
  # print('m = %1.3f' %model.slope)
  print('R2: \t %1.2f' %r_sq)
  print('coefficents = ' ,model.coef_)
  print('intercept = ', model.intercept_)
  r,c = x.shape
  
  valori = np.zeros(r)
  for i in range(0,r):
    for j in range(0,c):
        valori[i] += np.asarray(df[feature_x[j]])[i]*model.coef_[j]
    valori[i] += model.intercept_
    
  xn = np.arange(df[feature_y].min(),df[feature_y].max(),(df[feature_y].max()-df[feature_y].min())/100)
  plt.figure(figsize=(8,6))
  plt.title('fitting goodness\n%s' %feature_y)
  plt.plot(valori,df[feature_y],'v',label='simulated')
  plt.plot(xn,xn,'--',label='perfect fit')
  plt.text(xn.min(),yn.min()+.5,'r2 = %1.2f' %r_sq)
  # for i in range(0,len(valori)):
  #     plt.text(valori[i],df[feature_y][i]+0.05,str(df.sk[i]))
  plt.xlabel('predicted')
  plt.ylabel('real')
  plt.legend(loc='best')
  plt.show()
  
  plt.style.use('default')
  
  OLSModel(df,feature_x,feature_y)
  
  return model, valori

def LinearModel(df,feature_x,feature_y):
    x = df[feature_x].values
    y = df[feature_y].values
    
    # reshape dei dati necessario per il fit
    # perche al momento sono array(L,) e devono diventare array(L,1)
    
       
    L = len(x)
    x = x.reshape(L,1)
    y = y.reshape(L,1)
    
    model = LinearRegression().fit(x, y)
    r_sq = model.score(x, y)
    print('modello lineare')
    print(feature_x)
    print(feature_y)
    # print('y = m*x + q')
    # print('m = %1.3f' %model.slope)
    print('R2: \t %1.2f' %r_sq)
    
    print(model.coef_)
    print(model.intercept_)
    
    plt.figure(figsize=(10,5))
    plt.plot(x,y,'o',label='data')
    
    xn = np.arange(x.min(),x.max(),step=(x.max()-x.min())/100 )
    yn = model.predict(xn.reshape(len(xn),1))
    
    plt.plot(xn,yn,'--',label='fitted line')
    plt.text(x.min(),y.min()+.5,'r2 = %1.2f' %r_sq)
    plt.legend(loc='best')
    plt.title('Linear Model\n%s vs %s' %(feature_x,feature_y))
    plt.xlabel(feature_x)
    plt.ylabel(feature_y)
    
    return model
  
def CatchCorr(df,n):
  # cerca le prime n correlazioni all'interno di un df
  # le prime n in valore assouluto
  
  corr = df.corr()
  
  dfcorr = pd.DataFrame()
  dfcorr['correlation'] = corr.tempo_usura
  dfcorr['absolute'] = np.abs(corr.tempo_usura)
  
  dfcorr = dfcorr.sort_values('absolute')
  
  print(dfcorr.correlation[-(n-1):-1])
  
  #isolo le prime n veriabili
  dcorr = dfcorr.iloc[-(n-1):-1,:]
  return dcorr
