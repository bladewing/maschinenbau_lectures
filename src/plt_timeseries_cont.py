import numpy as np
import matplotlib.pyplot as plt

jahre = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019])
anz = np.array([[10, 12, 13, 15, 17, 20, 12], [5, 5, 6, 4, 5, 7, 6]])

plt.plot(jahre, anz[0, :], jahre, anz[1, :])
plt.xlabel("Jahre")
plt.ylabel("Anzahl Studierende")


plt.show()
