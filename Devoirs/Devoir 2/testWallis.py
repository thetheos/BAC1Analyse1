import math
import numpy as np
#compute the lenght of arc of an ellipse

def compute_wallis(n):
    #n must be even
    if n%2 != 0:
        return -1
    wallis = np.pi/2
    for i in range(1,(n//2)+1):
        wallis *= ((n+1-2*i))/(n-(2*i)+2)

    return wallis

def comput_double_fac(n):
    fac = 1
    if n< 0:
        return 1
    if n%2 == 0:
        for i in range(2,n+1,2):
            fac *= i
        return fac
    for i in range(1,n+1,2):
        fac *= i
    return fac

def compute_fac(n):
    fac = 1
    for i in range(1,n+1):
        fac *= i
    return fac

def quarter_ellipse_lenght(exc,n):
    lenght = np.pi/2
    for i in range(1,n+1):
        lenght -= 1/((2**i) * compute_fac(i)) * comput_double_fac(2*i-3) * exc**(2*i) * compute_wallis(2*i)
        #print(i)
        #print( "1/{0}*{1} * {2} * {3} * {4}".format(2**i, compute_fac(i), comput_double_fac(2*i-3), exc**(2*i), compute_wallis(2*i)))
    return lenght

for i in range(1,152):
    #print("Lenght: {0:.8f}".format(quarter_ellipse_lenght(0.8326818,i)))
    print("{1} Lenght: {0:.9f}".format(quarter_ellipse_lenght(0.8326818,i),i))
