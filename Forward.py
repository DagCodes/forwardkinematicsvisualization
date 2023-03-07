# Dagem Sinke

import numpy as np
import matplotlib.pyplot as plt

# Define the lengths of the two links
l1 = 1
l2 = 1

# Define the joint angles (in radians)
theta1 = 0
theta2 = np.pi/6

# Calculate the endpoint position
x = l1*np.cos(theta1) + l2*np.cos(theta1+theta2)
y = l1*np.sin(theta1) + l2*np.sin(theta1+theta2)

# Draw the arm
plt.plot([0, l1*np.cos(theta1), x], [0, l1*np.sin(theta1), y])
plt.xlim(-2, 2)
plt.ylim(-2, 2)

# Display the arm position
print("Arm position: ({:.2f}, {:.2f})".format(x, y))

plt.show()
