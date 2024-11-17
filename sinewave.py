import matplotlib.pyplot as plt
import numpy as np

# Define time range and voltage values for plotting negative cosine graph with given function V(t) = -2.52cos(2000πt)
time = np.arange(-1e-3, 1e-3, 25e-6) # define x-axis values in microseconds (i.e., from -1ms to +1 ms at intervals of .25ms each), with a total of 41 points.
voltage = -2.52 * np.cos(2000 * np.pi * time)   # generate corresponding voltage values based on the defined function V(t) for these x-axis values.

# Create a figure for plotting using plt.subplots()
fig, ax = plt.subplots()

# Set labels and titles of Y axis as per instructions; also set grid lines at .840 Volts with every line spaced by the required distance (25microseconds).
ax.set_ylabel('Voltage [V]')
gridlines = np.arange(-102, -78, 84)      # gridline values at every .84 volts as per instructions: range is set from '-102' to '-78', the step of which represents our required spacing between each line on Y axis (i.e., three lines in total).
ax.set_yticks(gridlines)

# Set labels and titles of X-axis; also set grid lines with required distance:
ax.set_xlabel('Time [microseconds]')
gridlines = np.arange(-100, 350, 250)         # gridline values at every interval of 250microseconds i.e., range is set from '-1' to '4', the step represents our required spacing between each line on X axis (i.e., five lines in total).
ax.set_xticks(gridlines)

# Plot a negative cosine graph based on defined function V(t) = -2.52cos(2000πt)
plt.plot(time*10**6, voltage)

plt.show()
