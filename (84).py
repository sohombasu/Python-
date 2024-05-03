import pandas as pd
S1 = 5000
S2 = pd.Series(data=S1,index=range(2017,2022,2))
print(S2)


import pandas as pd
S1 = [45,55]
S2 = pd.Series(S1*2)
print(S2)


import pandas as pd
S1 = pd.Series([9500,6200,3200,5800,9600])
S1[0]=7000
S1[4]=4000
S1[1::2]=2000
print(S1)
