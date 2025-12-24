import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 500)
c = np.cos(x)
s = np.sin(x)

plt.figure("Gráficos", figsize=(8, 4))
plt.subplots_adjust(
    left=0.12,
    right=0.943,
    top=0.9,
    bottom=0.14,
    wspace=0.438,
    hspace=0.738
)

# linha, coluna, index

ax1 = plt.subplot(2, 1, 1)
plt.plot(x, c)
ax1.set_title("Gráfico do Cosseno")
ax1.set_xlabel("Eixo de Tempo (s)")
ax1.set_ylabel("Eixo de Amplitude")
ax1.grid()

ax2 = plt.subplot(2, 1, 2)
plt.plot(x, s)
ax2.set_title("Gráfico do Seno")
ax2.set_xlabel("Eixo de Tempo (s)")
ax2.set_ylabel("Eixo de Amplitude")
ax2.grid()

plt.show()