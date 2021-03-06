import numpy as np


def franke(x):
    """The Franke objective function."""
    x = x.ravel()
    y = x[0]
    z = x[1]
    T1 = 0.75 * np.exp(-(9. * y - 2.)**2 / 4 - (9. * z - 2.)**2 / 4.)
    T2 = 0.75 * np.exp(-(9. * y + 1.)**2 / 49 - (9. * z + 1.) / 10.)
    T3 = 0.5 * np.exp(-(9. * y - 7.)**2 / 4 - (9. * z - 3.)**2 / 4.)
    T4 = -0.2 * np.exp(-(9. * y - 4.)**2 - (9. * z - 7.)**2)

    return T1 + T2 + T3 + T4
