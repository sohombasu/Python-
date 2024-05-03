import pandas as pd
data = [["Tv","LG",12000,700],["TV","VIDEOCON",10000,650],["TV","LG",15000,800],["AC","SONY",14000,750]]
DF = pd.DataFrame(data,columns=['Item','Company','Rupees','USD'])
print(DF)
