from math import log10, sqrt

def yplus_pipe(U, D, rho, mu, yplus):
    Re = rho*U*D/mu
    f = 1/(1.82*log10(Re) - 1.64)**2
    u_tau = sqrt(f/8)*U
    return yplus*mu/(rho*u_tau)

def first_cell_size(y):
    "Since y is the height for a given yplus, times 2 for the cell size"
    return y*2

def estimate_k(U, I):
    return 3/2*(U*I)**2

def estimate_eps(k, l):
    return (0.09**(3/4))*(k**(3/2))/l

def estimate_l(D):
    return 0.07*D


if __name__ == "__main__":

    #REC*** 14m conditions using HCS
    U = 11.69
    D = 0.295275*2
    rho = 3.125
    mu = 8.808E-6

    #REP*** 30m conditions using HCs
    U = 20.14
    D = 0.320675*2
    rho = 2.1314776275527
    mu = 9.71207824840234E-6

    yplus_1 = first_cell_size(yplus_pipe(U,D,rho,mu,1))
    yplus_30 = first_cell_size(yplus_pipe(U,D,rho,mu,30))

    print("Para y+=1:", yplus_1)
    print("Para y+=30:", yplus_30)

    #inlet conditions
    l_in = estimate_l(D)
    k_in = estimate_k(U, 0.05)
    eps_in = estimate_eps(k_in, l_in)
    print("l_in:", l_in)
    print("k_in:", k_in)
    print("eps_in:", eps_in)
