import matplotlib.pyplot as plt
Info = ("Gold","Silver","Bronze","Total")
India = (80,59,59,198)
Australia = (20,26,20,66)
plt.bar(Info,India)
plt.bar(Info,Australia)
plt.xlabel("Stats")
plt.ylabel("No.of Golds")
plt.show() #output 