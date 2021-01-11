import numpy as np

def project(P,x0,max_iter=1000,tol=1e-6):
    assert len(x0.shape) == 1, "x0 must be a vector"

    x = x0.copy()
    p = len(P)
    y = np.zeros((p,x0.shape[0]))

    n = 0
    cI = float('inf')
    while n < max_iter and cI >= tol:
        cI = 0
        for i in range(0,p):
            # Update iterate
            prev_x = x.copy()
            x = P[i](prev_x - y[i,:])

            # Update increment
            prev_y = y[i,:].copy()
            y[i,:] = x - (prev_x - prev_y)

            # Stop condition
            cI += np.linalg.norm(prev_y - y[i,:])**2

            n += 1
    return x
