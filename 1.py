import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mu = 100
sigma = 15
x =  mu+sigma*np.random.randn(100)
plt.figure(figsize=(10,7))
y = np.arange(len(x))
n,edges,p=plt.hist(x,bins=40,histtype='step')
m = 0.5*(edges[1:]+edges[:-1])
m = m.tolist()
l = len(m)
m.insert(0,m[0]-10)
m.append(m[l-1]+10)
n=n.tolist()
n.insert(0,0)
n.append(0)
plt.plot(m,n,'-^')
plt.show()