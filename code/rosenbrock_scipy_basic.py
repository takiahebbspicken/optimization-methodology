from scipy.optimize import minimize
import numpy as np

def obj(x):
    return (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2


def con(x):
    g = np.zeros(2)
    g[0] =  1 - x[0]**2 - x[1]**2
    g[1] = 5 - x[0] - 3*x[1]
    return g

constraints = {'type': 'ineq', 'fun': con}
options = {'disp': True}
x0 = [3.0, 3.0]

res = minimize(obj, x0, constraints=constraints, options=options)
print('x =', res.x)
print('f = ', res.fun)
print(res.success)
