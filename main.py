__doc__ = "main method"

#required imports
import matplotlib.pyplot as plt
import math

#Define fixed variables
initial_velocity = 55
final_velocity = 0
coefficiant_of_friction = 0.65
gravity = -9.81
time_step = 0.1
initial_distance = 0
inclination = math.radians(10)

#calculation of acceleration:
acceleration = (coefficiant_of_friction * gravity * math.cos(inclination))\
    + (gravity * math.sin(inclination))

#while loop to calculate the braking time:
init_braking_time = 0
braking_time = []
velocity_list = []
distance_list = []

while initial_velocity>=0:
  velocity_list.append(initial_velocity)
  distance_list.append(initial_distance)
  initial_velocity = (acceleration*time_step)+initial_velocity
  initial_distance = initial_distance + (initial_velocity*time_step) \
    + (0.5*acceleration*(time_step**2))
  init_braking_time+=0.1
  braking_time.append(init_braking_time)

#_________Plotting___________________

#define figure
fig = plt.figure(figsize=(13,5))
#add one plot
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

#define plots
ax1.plot(braking_time, velocity_list, color ="blue", lw = 2)
ax2.plot(braking_time, distance_list, color ="red", lw = 2)

#add axis label
ax1.set_xlabel("time")
ax1.set_ylabel("velocity")
ax1.grid()
ax2.set_xlabel("time")
ax2.set_ylabel("distance")
ax2.grid()
#add plot label
fig.suptitle("Plot Sample\n\n", fontweight ="bold")


# Save the figure as a PDF
plt.savefig("Plots.pdf")

# Display the plot
plt.show()

#End of code


