import numpy as np
import matplotlib.pyplot as plt
acceleration=2#m/s^2
V_i=0 #m/s (Initial Velocity)
t_1=10 #(time given in seconds)
# Now to find the final velocity after 10 seconds
t_2= 5 #(time for constant acceleration)
time=np.arange(0,t_1+t_2+1,2)
V_f= V_i+ acceleration*t_1
V=np.where(time<t_1,V_i+acceleration*time, V_f)
print(f"time shape: {len(time)}")

print(f"velocity shape: {len(V)}")
plt.figure(figsize=(8,5))
plt.plot(time,V,color='green',marker='o')
plt.title("Velocity vs time")
plt.xlabel("Time(sec)")
plt.ylabel("Velocity(m/s")
plt.grid(True)
plt.show()

