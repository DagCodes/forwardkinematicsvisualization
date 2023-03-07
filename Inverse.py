import numpy as np
import matplotlib.pyplot as plt

# Define the lengths of the two links
l1 = 1
l2 = 1

# Define the endpoint position (in meters)
x = 1
y = 1

# Calculate the joint angles (in radians)
r = np.sqrt(x**2 + y**2)
alpha = np.arctan2(y, x)
beta = np.arccos((l1**2 + r**2 - l2**2) / (2*l1*r))
theta1 = alpha - beta
theta2 = np.arccos((l1**2 + l2**2 - r**2) / (2*l1*l2))

# Calculate the endpoint position
x_end = l1*np.cos(theta1) + l2*np.cos(theta1+theta2)
y_end = l1*np.sin(theta1) + l2*np.sin(theta1+theta2)

# Draw the arm and head
plt.plot([0, l1*np.cos(theta1), x_end], [0, l1*np.sin(theta1), y_end], 'o-', lw=2, markersize=10)

# Draw the head
plt.plot(x_end, y_end, 'o', markersize=10)

# Set axis limits and labels
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel('X')
plt.ylabel('Y')

# Add grid
plt.grid(True)

# Display the joint angles
print("Joint angles: (theta1={:.2f}, theta2={:.2f})".format(theta1, theta2))

plt.show()