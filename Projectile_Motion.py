import numpy as np
import math
import matplotlib.pyplot as plt


plt.clf()  # Clear/Initiate Screen

#  Function to plot motion of a ball at constant velocity
def PlotMotion(list_x, list_y, theta):
    #  Initialize Values
    pi = np.pi
    v0 = 100  # m/s  constant velocity
    g = 9.81  # m/s^2  gravitational acceleration
    angle = theta * pi / 180  # angle to be inserted into equations are converted into radians
    yf = 1.0
    yi = 0.0
    t = 0.0
    dt = 0.1

    while yf >= 0:
        #  Equations of motion
        xf = (v0 * np.cos(angle))*t
        yf = yi + (v0 * np.sin(angle))*t - (g*t*t) / 2

        #  Derive new equation by replacing t into eq 2. from eq 1
        y2 = yf + xf*np.sin(angle) / np.cos(angle) - g*xf*xf / (2.0*math.pow(v0*np.cos(angle), 2))

        #   Save x and y values to list
        list_x.append(xf)
        list_y.append(yf)

        t = t + dt

    # Print time taken for projectile to hit the ground in each case
    print t

    plt.plot(x, y)  # Plot data points in the x and y arrays/lists
    '''
         'blue',  # colour
         linestyle='--',  # line style
         linewidth=3,  # line width
         label='Projectile Motion'  # plot label
    '''

    plt.axis([0, 1100, 0, 500])

x = []
y = []
#  Plot motion of the projectile for 3 different angles
PlotMotion(x,y,30)
PlotMotion(x,y,45)
PlotMotion(x,y,70)

plt.show()