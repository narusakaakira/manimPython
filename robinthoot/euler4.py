import numpy as np
import matplotlib.pyplot as plt

# Parameters
Pi = 0.01
beta = 0.0095
delta = 0.0001
zeta = 0.1
alpha = 0.0005
rho = 0.2
c = 0.3

# Time grid
T = 30
h = 0.01
N = int(T / h)
t = np.linspace(0, T, N + 1)

# Initial conditions
S0 = 500
Z0 = 0
R0 = 1
I0 = 0

S = np.zeros(N + 1)
I = np.zeros(N + 1)
Z = np.zeros(N + 1)
R = np.zeros(N + 1)

S[0] = S0
I[0] = I0
Z[0] = Z0
R[0] = R0

def derivatives(S, I, Z, R):
    dS = Pi - beta * S * Z - delta * S + c * Z
    dI = beta * S * Z - rho * I - delta * I
    dZ = rho * I + zeta * R - alpha * S * Z - c * Z
    dR = delta * S + delta * I + alpha * S * Z - zeta * R
    return dS, dI, dZ, dR

for n in range(N):
    dS, dI, dZ, dR = derivatives(S[n], I[n], Z[n], R[n])
    S[n + 1] = S[n] + h * dS
    I[n + 1] = I[n] + h * dI
    Z[n + 1] = Z[n] + h * dZ
    R[n + 1] = R[n] + h * dR

plt.plot(t, S, label='Susceptibles')
plt.plot(t, I, label='Infected')
plt.plot(t, Z, label='Zombies')
plt.plot(t, R, label='Removed')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('Euler Method: S-I-Z-R dynamics')
plt.grid()
plt.show()
