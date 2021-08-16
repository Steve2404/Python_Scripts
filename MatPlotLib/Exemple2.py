import matplotlib.pyplot as plt

sample1= [10, 14, 50, 80, 70, 80, 90, 50, 40, 10]
sample2= [70, 30, 40, 50, 80, 90, 95, 80, 40, 10]
plt.plot(sample1, 'b-o', sample2, 'g--^')
plt.legend(("sample1", "sample2"))
plt.xlabel("time")
plt.ylabel("speed")
plt.show()