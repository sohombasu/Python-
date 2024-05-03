#import numpy as np#
#import matplotlib.pyplot as plt#
#A=np.arange(1,20,1.25)#
#B=np.log(A)#
#C=np.log10(A)#
#plt.scatter(A,B)#
#plt.scatter(A,C)#
#plt.show()#


import numpy as np
import pandas as pd
dict={'Name':pd.Series(['Anu','Abhishek','Rajeev','Ritu']),'Age':pd.Series([26,25,24,31]),'Score':pd.Series([87,67,89,55])}
df=pd.DataFrame(dict)
print("Dataframe contents are")
print(df)
print(df.count())



