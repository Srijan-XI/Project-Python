<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt

# Define data
t = np.linspace(0, 10, 100)  # Time values
s = np.sin(t)  # Sine function

# Create subplots
fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(8, 3))
plt.tight_layout()  # Ensure proper layout

# --- First subplot (with twin axes) ---
l1, = ax1.plot(t, s, label="Sine (left)")
ax1.set_xlabel("Time")
ax1.set_ylabel("Sine Value")

ax2 = ax1.twinx()  # Create secondary y-axis
l2, = ax2.plot(t, np.arange(len(t)), 'C1', label="Straight (right)")
ax2.set_ylabel("Straight Line")

# Fix: Add legends properly
ax1.legend(handles=[l1, l2], loc="upper left")

# --- Second subplot (with secondary x-axis) ---
ax3.plot(t, s)
ax3.set_xlabel("Angle [rad]")
ax3.set_ylabel("Sine Value")

# Create secondary x-axis for degrees
ax4 = ax3.secondary_xaxis('top', functions=(np.rad2deg, np.deg2rad))
ax4.set_xlabel("Angle [°]")

# Show the plot
plt.show()
=======
import numpy as np
import matplotlib.pyplot as plt

# Define data
t = np.linspace(0, 10, 100)  # Time values
s = np.sin(t)  # Sine function

# Create subplots
fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(8, 3))
plt.tight_layout()  # Ensure proper layout

# --- First subplot (with twin axes) ---
l1, = ax1.plot(t, s, label="Sine (left)")
ax1.set_xlabel("Time")
ax1.set_ylabel("Sine Value")

ax2 = ax1.twinx()  # Create secondary y-axis
l2, = ax2.plot(t, np.arange(len(t)), 'C1', label="Straight (right)")
ax2.set_ylabel("Straight Line")

# Fix: Add legends properly
ax1.legend(handles=[l1, l2], loc="upper left")

# --- Second subplot (with secondary x-axis) ---
ax3.plot(t, s)
ax3.set_xlabel("Angle [rad]")
ax3.set_ylabel("Sine Value")

# Create secondary x-axis for degrees
ax4 = ax3.secondary_xaxis('top', functions=(np.rad2deg, np.deg2rad))
ax4.set_xlabel("Angle [°]")

# Show the plot
plt.show()
>>>>>>> 397691e3bddc1c2468c0790a7ae5dcc8aba4e6c3
