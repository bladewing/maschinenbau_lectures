import numpy as np
import matplotlib.pyplot as plt

m_2022_05 = np.array(["..."])
m_2023_05 = np.array(["..."])
tage = np.arange(1, 29, 1)

beideplots = plt.figure(layout="constrained")
verlauf1 = beideplots.add_subplot(2, 1, 1)
verlauf1.set_title("2022")
verlauf1.plot(tage, m_2022_05, "+")
verlauf1.set_xlabel("Tage (Monat Mai)")
verlauf1.set_ylabel("Gewicht (kg)")
verlauf2 = beideplots.add_subplot(2, 1, 2)
verlauf2.set_title("2023")
verlauf2.plot(tage, m_2023_05, "+")
verlauf2.set_xlabel("Tage (Monat Mai)")
verlauf2.set_ylabel("Gewicht (kg)")

plt.show()
