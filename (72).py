import pandas as pd
marksUT= {'Name':['Raman','Raman','Raman','Zuhaire','Zuhaire','Zuhaire', 'Ashravy','Ashravy','Ashravy','Mishti','Mishti','Mishti'],'UT':[1,2,3,1,2,3,1,2,3,1,2,3],'Maths':[22,21,14,20,23,22,23,24,12,15,18,17],'Science':[21,20,19,17,15,18,19,22,25,22,21,18],'S.St':[18,17,15,22,21,19,20,24,19,25,25,20],'Hindi':[20,22,24,24,25,23,15,17,21,22,24,25],'Eng':[21,24,23,19,15,13,22,21,23,22,23,20]}
df=pd.DataFrame(marksUT)
print(df)
print(df.max())#shows the maximum value of each column of the DataFrame
print(df.max(numeric_only=True))#shows the  maximum value for the columns having only numeric values
dfut2 = df[df.UT == 2]
print('\nResult of Unit Test 2:\n\n',dfut2)
print('\nMaximum Mark obtained in Each Subject in Unit Test 2: \n\n',dfut2.max(numeric_only=True))
