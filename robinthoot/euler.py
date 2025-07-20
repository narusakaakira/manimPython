import numpy as np
import matplotlib.pyplot as plt

# Parameters
Pi = 0.01
beta = 0.0095
delta = 0.0001
zeta = 0.1
alpha = 0.0005

# Time grid
T = 20  # total time
h = 0.01         # time step
N = int(T/h)    # number of steps
t = np.linspace(0, T, N+1)

# Initial conditions
S0 = 5
Z0 = 0
R0 = 1

# Allocate arrays
S = np.zeros(N+1)
Z = np.zeros(N+1)
R = np.zeros(N+1)

# Initial values
S[0] = S0
Z[0] = Z0
R[0] = R0

# Define the derivatives
def derivatives(S, Z, R):
    dS = Pi - beta*S*Z - delta*S
    dZ = beta*S*Z + zeta*R - alpha*S*Z
    dR = delta*S + alpha*S*Z - zeta*R
    return dS, dZ, dR

# Euler method
for n in range(N):
    dS, dZ, dR = derivatives(S[n], Z[n], R[n])
    S[n+1] = S[n] + h*dS
    Z[n+1] = Z[n] + h*dZ
    R[n+1] = R[n] + h*dR
plt.savefig("S_Z_R_graph.pdf")
# Plot results
plt.plot(t, S, label='Susceptibles')
plt.plot(t, Z, label='Zombies')
plt.plot(t, R, label='Removed')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('Euler Method: S-Z-R dynamics')
plt.grid()
plt.show()