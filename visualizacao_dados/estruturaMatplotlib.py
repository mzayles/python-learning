import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 100)
y = np.cos(4*t)
y1 = np.sin(4*t)

# figure > axes > axis

plt.figure("Cosseno", figsize=(5, 4))
plt.plot(t, y)
plt.title("Gráfico do Cosseno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.show()

plt.figure("Seno", figsize=(5, 4))
plt.plot(t, y1)
plt.title("Gráfico do Seno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.show()