import numpy as np
import matplotlib.pyplot as plt


def differentiate(u, dt):
    du = np.zeros(u.shape)
    du[0] = (u[1] - u[0])/dt
    du[-1] = (u[-1] - u[-2])/dt
    for i in range(1, len(u) - 1):
        du[i] = (u[i+1] - u[i-1])/2/dt
    return du

def differentiate_vector(u, dt):
    du = np.zeros(u.shape)
    du[0] = (u[1] - u[0])/dt
    du[-1] = (u[-1] - u[-2])/dt
    du[1:-1] = (u[2:] - u[:-2])/2/dt

    return du

def test_differentiate():
    t = np.linspace(0, 1, 10)
    dt = t[1] - t[0]
    u = t**2
    du1 = differentiate(u, dt)
    du2 = differentiate_vector(u, dt)
    assert np.allclose(du1, du2)

if __name__ == '__main__':
    t = np.linspace(0, 4*np.pi, 1001)
    dt = t[1] - t[0]
    y = np.sin(t)
    dy_ex = np.cos(t)
    dy = differentiate(y, dt)
    dy_vec = differentiate_vector(y, dt)
    plt.plot(t, dy_ex)
    plt.plot(t, dy, '--')
    plt.plot(t, dy_vec, ':')
    plt.legend(["dy exact", "dy using loops", "dy vectorized"])
    plt.show()


    test_differentiate()
    