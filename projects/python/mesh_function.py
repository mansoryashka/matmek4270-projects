import numpy as np
import matplotlib.pyplot as plt

def mesh_function(f, t):
    f_mesh = np.zeros(t.shape)
    for i in range(len(t)):
        f_mesh[i] = f(t[i])
    return f_mesh

def func(t):
    if t >= 0 and t <= 3:
        return np.exp(-t)
    if t > 3 and t <= 4:
        return np.exp(-3*t)

def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)


if __name__ == '__main__':
    dt = 0.1
    N = int(4/dt)
    t = np.linspace(0, 4, N+1)
    f_mesh = mesh_function(func, t)

    plt.plot(t, f_mesh)
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.show()