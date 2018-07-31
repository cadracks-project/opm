# coding: utf-8

import numpy as np


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def random_orthogonal_vector(k):
    x = np.random.randn(3)  # take a random vector
    x -= x.dot(k) * k  # make it orthogonal to k
    x /= np.linalg.norm(x)
    print(np.linalg.norm(x))
    print(np.dot(k, x))
    assert np.linalg.norm(x) == 1.
    assert abs(np.dot(k, x)) <= 1e-10
    return x

v = np.array([0,96.786,-25.150])
nv = normalize(v)
ov = random_orthogonal_vector(nv)

print("%f,%f,%f,%f,%f,%f" % (nv[0], nv[1], nv[2], ov[0], ov[1], ov[2]))
