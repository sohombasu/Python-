import matplotlib.pyplot as plt
week = ("Subway Sufer","Temple Run","Candy Crush","Bottle Shot","Runner Best")
prices = [4.3,4.6,4.9,3.8,4.0]
plt.barh(week,prices)
plt.xlabel("Games")
plt.ylabel("Rating")
plt.show()

