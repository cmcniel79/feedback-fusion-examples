import numpy as np
import matplotlib.pyplot as plt

# A first order dynamic system is one whose behavior can be described with a first-order
# ordinary differential equation (ODE). A first-order ODE is one in which the highest-order
# derivative is a first derivative.

# First order systems are typically written as 
# (1) x_dot + 1/tau * x = f(t) 
# 
# where:
# x = displacement, or the equivalent property for the given system,
# x_dot = velocity, or equivalent,
# tau = the time constant, and
# f(t) = the forcing function, a function of time

# The ODE from above has homogeneous and particular solutions, xh and xp, which describe the
# response of the system. The general solution is given by x = xh + xp.

# Homogeneous Solution
# The homogeneous solution (xh) depends on the inherent characteristics of the system and
# describes the system’s free response. This is the solution of the equation
# x_dot + 1/tau * x = 0

# which is identical to (1) except that the right-hand side of the equation is equal to zero. This
# means that there is no forcing function; no force is continuing to act upon the system after time
# t = 0.

# To find the system response, we first assume that the solution to this equation is in the form:
# xh = e^(-t/tau)
# This is then substituted into the original equation, (4), to find

# This is the characteristic equation. Solving the characteristic equation for λ and then substituting
# the result back into (5), the solution becomes

tau = 1
t = np.linspace(0, 5, 100)
xh = np.exp(-t/tau)


plt.plot(t, xh, label='Steady State Response')
plt.axhline(0.5, linestyle='--', color='k', label='Input Command')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Response')
plt.show()
