import numpy as np
import matplotlib.pyplot as plt

# Parameters
Pi = 0.01
beta = 0.0095
delta = 0.0001
zeta = 0.1
alpha = 0.0005
rho = 0.2
kappa = 0.05
sigma = 0.04
gamma = 0.02

# Time grid
T = 20
h = 0.01
N = int(T / h)
t = np.linspace(0, T, N + 1)

# Initial conditions
S0 = 500
Z0 = 0
R0 = 1
I0 = 0
Q0 = 0

# Allocate arrays
S = np.zeros(N + 1)
I = np.zeros(N + 1)
Z = np.zeros(N + 1)
R = np.zeros(N + 1)
Q = np.zeros(N + 1)

# Initial values
S[0] = S0
I[0] = I0
Z[0] = Z0
R[0] = R0
Q[0] = Q0

# Derivatives
def derivatives(S, I, Z, R, Q):
    dS = Pi - beta * S * Z - delta * S
    dI = beta * S * Z - rho * I - delta * I - kappa * I
    dZ = rho * I + zeta * R - alpha * S * Z - sigma * Z
    dR = delta * S + delta * I + alpha * S * Z - zeta * R + gamma * Q
    dQ = kappa * I + sigma * Z - gamma * Q
    return dS, dI, dZ, dR, dQ

# Euler method
for n in range(N):
    dS, dI, dZ, dR, dQ = derivatives(S[n], I[n], Z[n], R[n], Q[n])
    S[n + 1] = S[n] + h * dS
    I[n + 1] = I[n] + h * dI
    Z[n + 1] = Z[n] + h * dZ
    R[n + 1] = R[n] + h * dR
    Q[n + 1] = Q[n] + h * dQ

# Plot
plt.plot(t, S, label='Susceptibles')
plt.plot(t, I, label='Infected')
plt.plot(t, Z, label='Zombies')
plt.plot(t, R, label='Removed')
plt.plot(t, Q, label='Quarantined')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('Euler Method: S-I-Z-R-Q dynamics')
plt.grid()
plt.show()
