import pandas as pd
d = pd.Series(5000, index=["Qtr1",'Qtr2','Qtr3','Qtr4'])
print(d)

import pandas as pd
s = pd.Series(200,index=range(2020,2029,2))
print(s)

import asyncio
async def main():
    print("Hello.....")
    await asyncio.sleep(1)
    print("...World")
asyncio.run(main())
