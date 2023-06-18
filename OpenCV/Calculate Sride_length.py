# distance covered in one step (in meters)
step_distance = 0.7 

# number of steps taken in a given distance
num_steps = 50 

# distance covered by the person (in meters)
distance = num_steps * step_distance 

# stride length (in meters)
stride_length = distance / num_steps 

print(f"The stride length is {stride_length:.2f} meters.")