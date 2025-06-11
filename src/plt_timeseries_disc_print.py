import numpy as np
import matplotlib.pyplot as plt

m_2022_05 = np.array([])  # ...
m_2023_05 = np.array([])  # ...

tage = np.arange(1, 29, 1)

plt.plot(tage, m_2022_05, "+", tage, m_2023_05, "*")
plt.xlabel("Tage (Monat Mai)")
plt.ylabel("Gewicht (kg)")
plt.legend(("2022", "2023"))

plt.show()
