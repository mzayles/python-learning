import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 100)
y = np.cos(t)
y1 = np.sin(t)

plt.figure("Gráfico", figsize=(6, 4))
plt.plot(t, y)
plt.plot(t, y1)
plt.title("Gráfico do Seno e Cosseno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()