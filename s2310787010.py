__doc__ = "This is my main file that includes 3 functions\
  the first one is responsible for getting the coefficiant of friction\
    the second one calculates the braking distance and returns 3 lists\
      the third one is responsibe for plotting the data\
        the code simulates the braking distance of the vehicle in \
          different conditions"

#required imports
import matplotlib.pyplot as plt
import math
import argparse

#==========================================
#This method chooses the Coefficiant of friction
#return :Coefficiant of friction
#it takes no parameters
#==========================================

def get_coefficient_of_friction():
  # Coefficient of Friction Table
  frictional_coefficiant = {
      ("concrete", "dry"): 0.5,
      ("concrete", "wet"): 0.35,
      ("ice", "dry"): 0.15,
      ("ice", "wet"): 0.08,
      ("water", "aquaplaning"): 0.05,
      ("gravel", "dry"): 0.35,
      ("sand", "dry"): 0.3,
  }

  while True:
    # User inputs for road type and condition
    road = input("Insert the road type (Concrete/Ice/Water/Gravel/Sand): ")
    condition = input("Insert the road condition (Dry/Wet/Aquaplaning): ")

    # Convert inputs to lowercase to match the data in the table
    road = road.lower()
    condition = condition.lower()

    # Look up coefficient of friction based on user input
    mu = frictional_coefficiant.get((road, condition))

    # Print the result and prompt for new input if not found
    if mu:
      print("The coefficient of friction is:", mu)
      return mu
    else:
      print("No coefficient of friction found for the given inputs")

#===========================================================================
#This method calculates the braking distance
#Returns: three lists(velocity, distance, time)
#param in: coefficiant_of_friction, inclination, initial_velocity, time_step
#===========================================================================
def calculate_braking_lists\
  (coefficiant_of_friction, inclination, initial_velocity, time_step):
  #Define initial variables
  gravity = -9.81
  initial_distance = 0
  init_braking_time = 0
  velocity_list = []
  distance_list = []
  braking_time = []

  #Change angle to radians
  inclination_angle = math.radians(inclination)

  #Calculate the acceleration
  acceleration = (coefficiant_of_friction * gravity * \
                  math.cos(inclination_angle))\
                    + (gravity * math.sin(inclination_angle))

  #calculation of velocity and braking distance
  while initial_velocity >= 0:
    velocity_list.append(initial_velocity)
    distance_list.append(initial_distance)
    initial_velocity = (acceleration * time_step) + initial_velocity
    initial_distance = initial_distance + \
    (initial_velocity * time_step) + (0.5 * acceleration * (time_step**2))
    init_braking_time+=0.1
    braking_time.append(init_braking_time)

  return velocity_list, distance_list, braking_time

#===========================================================================
#This method plots the braking distance/time and velocity/time
#Returns: plot
#param in: velocity list, distance list, bracking_time list
#===========================================================================
def plot_results(velocity, distance, bracking_time):

  # Define figure
  fig = plt.figure(figsize=(13, 5))

  # Add two subplots
  ax1 = fig.add_subplot(121)
  ax2 = fig.add_subplot(122)

  # Plot results on subplots
  ax1.plot(bracking_time, velocity, color="blue", lw=2)
  ax2.plot(bracking_time, distance, color="red", lw=2)

  # Add axis labels and grids
  ax1.set_xlabel("Time (seconds)")
  ax1.set_ylabel("Velocity (meters/second)")
  ax1.grid()

  ax2.set_xlabel("Time (seconds)")
  ax2.set_ylabel("Distance (meters)")
  ax2.grid()

  # Add plot label
  fig.suptitle("Braking Results\n\n", fontweight="bold")

  # Save the figure as a PDF
  plt.savefig("BrakingResults.pdf")

  # Display the plot
  plt.show()

#===========================================================================
#This method is the main method were I call all the functions
#Returns: null
#param in: null
#===========================================================================
def main():
  #Create argument parser
  arg_parser = argparse.ArgumentParser\
    (description="Vehicle parameters")

  #Add arguments for velocity and mass
  arg_parser.add_argument\
    ("initial_velocity", type=float, help="initial velocity of the vehicle.")
  arg_parser.add_argument\
    ("inclination", type=float, help="inclination angle of the road.")
  arg_parser.add_argument\
    ("time_step", type=float, help="inclination angle of the road.")

  #Parse the command-line arguments
  args = arg_parser.parse_args()

  # #Get the coefficiant_of_friction
  mu = get_coefficient_of_friction()

  #get the result lists
  result_velocity, result_distance, result_braking_time =\
      calculate_braking_lists(
  mu, args.inclination, args.initial_velocity, args.time_step)

  #Plot the results
  plot_results(result_velocity, result_distance, result_braking_time)

if __name__ == "__main__":
  main()

#End of code
