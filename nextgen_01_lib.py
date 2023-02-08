import numpy as np
import scipy as sp

def get_sp_dist(version='xi'):
    """
    The salmon pox distribution

    Coding: 
    0 well and negative
    1 sick and negative
    2 well and positive
    3 sick and positive
    """
    xk = np.arange(4)
    if version is None:
        pk = (0.82, 0.01, 0.09, 0.09)
    elif version == 'xi':
        pk = (0.7, 0.02, 0.08, 0.2)  
    return sp.stats.rv_discrete(0, 3, name='sp', values=(xk, pk))


def sp_coding(c):
    if c == 0:
        return 'well', 'negative'
    elif c == 1:
        return 'sick', 'negative'
    elif c == 2:
        return 'well', 'positive'
    elif c == 3:
        return 'sick', 'positive'


def get_sp_data(n=100, version='xi', seed=15):
    """
    Generate some data from the salmon pox distribution
    """
    rng = np.random.default_rng(seed)
    
    sp_dist = get_sp_dist(version=version)
    data = sp_dist.rvs(size=n, random_state=rng)
    return [sp_coding(c) for c in data]


def get_wh_dist():
    """
    armspan/height distribution
    """
    mean = np.array([2, 3.5]).reshape(-1,1)
    covar = np.array(
        [1**2, 1*1.5*0.8, 1*1.5*0.8, 1.5**2]
        ).reshape(2,2) * 0.25
    return sp.stats.multivariate_normal(mean=mean.ravel(), cov=covar)


def get_wh_data(n=200, seed=15):
    """
    Generate some data from the armspan/height distribution
    """
    rng = np.random.default_rng(seed)
    wh_dist = get_wh_dist()
    return wh_dist.rvs(size=n, random_state=rng)