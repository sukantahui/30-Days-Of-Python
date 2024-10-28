import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Creating subplots
plt.figure(figsize=(10, 5))

# First subplot
plt.subplot(1, 2, 1)
plt.plot(x, y1, "r-")
plt.title("Sine Wave")

# Second subplot
plt.subplot(1, 2, 2)
plt.plot(x, y2, "b-")
plt.title("Cosine Wave")

plt.show()