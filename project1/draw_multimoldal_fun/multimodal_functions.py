import numpy as np

def six_hump_camel(x, y): 
    term1 = (4 - 2.1 * x**2 + (x**4) / 3) * x**2
    term2 = x * y + (-4 + 4 * y**2) * y**2
    return  term1+term2

def easom(x, y):
    return -np.cos(x) * np.cos(y) * np.exp(-(x - np.pi)**2 - (y - np.pi)**2)

def peaks(x, y):
    term1 = 3 * (1 - x)**2 * np.exp(-(x**2) - (y + 1)**2)
    term2 = - 10 * (x/5 - x**3 - y**5) * np.exp(-x**2 - y**2)
    term3 = - (1/3) * np.exp(-(x + 1)**2 - y**2)
    return  term1 +term2 +term3


def rastrigin(x, y, A=10):
    term1 = 2 * A + x**2 - A * np.cos(2 * np.pi * x) 
    term2 = y**2 - A * np.cos(2 * np.pi * y)
    return term1 + term2

def ackley(x, y, a=20, b=0.2, c=2*np.pi):
    term1 = -a * np.exp(-b * np.sqrt((x**2 + y**2) / 2))
    term2 = -np.exp((np.cos(c * x) + np.cos(c * y)) / 2) + a + np.exp(1)
    return term1 + term2

def michalewicz(x, y, m=10):
    term1 = -np.sin(x) * (np.sin(1 * x**2 / np.pi))**(2 * m)
    term2 = -np.sin(y) * (np.sin(2 * y**2 / np.pi))**(2 * m)
    return term1 + term2

def bukin(x, y):# -3 3
    term1 = 100 * np.sqrt(np.abs(y - 0.01*x**2))
    term2 = 0.01 * np.abs(x + 10)
    return term1 + term2

def drop_wave(x, y):# [-5,5] [-2,2]
    frac1 = 1 + np.cos(12 * np.sqrt(x**2 + y**2))
    frac2 = 0.5 * (x**2 + y**2) + 2
    return -frac1 / frac2

def cross_in_tray(x, y):# -10 10 or -2 2
    fact1 = np.sin(x) * np.sin(y)
    fact2 = np.exp(np.abs(100 - np.sqrt(x**2 + y**2) / np.pi))
    return -0.0001 * (np.abs(fact1 * fact2) + 1) ** 0.1

def eggholder(x, y): #[-600,600]
    term1 = -(y + 47) * np.sin(np.sqrt(np.abs(y + x / 2 + 47)))
    term2 = -x * np.sin(np.sqrt(np.abs(x - (y + 47))))
    return term1 + term2

def holder_table(x, y): # -10 10
    fact1 = np.sin(x) * np.cos(y)
    fact2 = np.exp(np.abs(1 - np.sqrt(x**2 + y**2) / np.pi))
    return -np.abs(fact1 * fact2)


def langermann(x, y, m=5, c=None, A=None): # 0 10
    if c is None:
        if m == 5:
            c = [1, 2, 5, 2, 3]
        else:
            raise ValueError('Value of the m-dimensional vector c is required.')
    
    if A is None:
        if m==5:
            A = [[3, 5], [5, 2], [2, 1], [1, 4], [7, 9]]
        else:
            raise ValueError('Value of the (mxd)-dimensional matrix A is required.')
            
    outer = 0
    for ii in range(m):
        inner = 0
        for xj, Aij in zip([x, y], A[ii]):
            inner += (xj - Aij) ** 2
        new = c[ii] * np.exp(-inner/np.pi) * np.cos(np.pi * inner)
        outer += new
    return outer

def levy(x, y): # -10 10
    w = [1 + (xi - 1) / 4 for xi in [x, y]]
    term1 = (np.sin(np.pi * w[0])) ** 2
    term3 = (w[1] - 1) ** 2 * (1 + (np.sin(2 * np.pi * w[1])) ** 2)
    sum_terms = 0
    for wi in w[:-1]:
        new = (wi - 1) ** 2 * (1 + 10 * (np.sin(np.pi * wi + 1)) ** 2)
        sum_terms += new
    return term1 + sum_terms + term3

def levy13(x, y):
    term1 = (np.sin(3 * np.pi * x)) ** 2
    term2 = (x - 1) ** 2 * (1 + (np.sin(3 * np.pi * y)) ** 2)
    term3 = (y - 1) ** 2 * (1 + (np.sin(2 * np.pi * y)) ** 2)
    return term1 + term2 + term3

def schaffer2(x, y): # [-50 50 -50 50] or [-2 2 -2 2]
    fact1 = (np.sin(x**2 - y**2))**2 - 0.5
    fact2 = (1 + 0.001 * (x**2 + y**2))**2
    return 0.5 + fact1 / fact2

def schaffer4(x, y): # [-10 10 -10 10] or -2 2 -2 2
    fact1 = (np.cos(np.sin(np.abs(x**2 - y**2))))**2 - 0.5
    fact2 = (1 + 0.001 * (x**2 + y**2))**2
    return 0.5 + fact1 / fact2

def goldstein_price(x, y): # -2 2 -2 2
    return (1 + (x + y + 1)**2 * (19 - 14*x + 3*(x**2) - 14*y + 6*x*y + 3*y**2)) *\
           (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*(x**2) + 48*y - 36*x*y + 27*(y**2)))


def three_hump_camel(x, y): # -5 5 -5 5 or -2 2 -2 2 
    term1 = 2*x**2
    term2 = -1.05*x**4
    term3 = x**6 / 6
    term4 = x*y
    term5 = y**2
    return term1 + term2 + term3 + term4 + term5

# def dejong5(x, y): # -50 50 -50 50
#     A = np.array([[a for a in [-32, -16, 0, 16, 32] for _ in range(5)],
#                   [a for _ in range(5) for a in [-32, -16, 0, 16, 32]]])
#     s = np.sum(1. / (np.arange(1, 26) + np.sum(((np.array([x, y]) - A)**6), axis=0)))
#     return 1 / (0.002 + s)






def first_penalized(x, y): # default
    term1 = (np.sin(np.pi*(1+(x+1)/4)))**2
    term2 = (np.sin(np.pi*(1+(y+1)/4)))**2
    return (np.pi/2) * (10 * (term1 + term2) + (x/4)**2 + (y/4)**2)

def second_penalized(x, y): # -5 5 -5 5 
    term1 = (np.sin(3*np.pi*x))**2
    term2 = (np.sin(3*np.pi*y))**2
    return 0.1 * (term1 + (x-1)**2 * (1 + term2) + (y-1)**2 * (1 + (np.sin(2*np.pi*y))**2))

def shekels_foxholes(x, y): # -100 100 -100 100
    aS = np.array([[-32, -16, 0, 16, 32]*5, np.repeat([-32, -16, 0, 16, 32], 5)])
    bS = np.sum((np.array([x, y]).reshape(2, 1) - aS)**6, axis=0)
    return (1/500 + np.sum(1./(np.arange(1, 26) + bS)))**(-1)

def quartic(x, y): # -1 1 -1 1
    return 0.5 * ((x**4) + (y**4)) + np.random.rand()

def styblinski_tang(x, y): # -5 5 -5 5
    return 0.5 * (x**4 - 16*x**2 + 5*x + y**4 - 16*y**2 + 5*y)




