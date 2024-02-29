import numpy as np
import matplotlib.pyplot as plt

# Define the range for x
x = np.linspace(-2, 2, 1000)

# Calculate the y values for the top and bottom functions
f_top = np.sqrt(1 - (np.abs(x) - 1)**2)
f_bot = np.arccos(1 - np.abs(x)) - np.pi

# Plotting the top and bottom functions
plt.figure(figsize=(8, 4))
plt.plot(x, f_top, label='$f_{top} = \sqrt{1 - (|x| - 1)^2}$')
plt.plot(x, f_bot, label='$f_{bot} = arccos(1 - |x|) - \pi$')
plt.title('Plot of the given functions')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
