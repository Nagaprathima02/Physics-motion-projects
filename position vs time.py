import numpy as np
import matplotlib.pyplot as plt
velocity= 4.00 #m/s
time_min=2 
x_i= 0 #m
time_sec= time_min*60
x= x_i + velocity*time_sec
plt.figure(figsize=(8, 5))
plt.plot(time_sec, x, marker='o')
plt.title("Jogger's Position Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Position (meters)")
plt.show()
print("The final position of the Jogger is:", x, "meters")