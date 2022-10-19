import math, cmath 
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
# ============================================================================

"Task 1"
List_approx_ln=[]
List_ln=[]
List_difference=[]

def approx_ln (x,n):
    
    a=(1+x)/2
    g=np.sqrt(x)
    
    for i in range (1,n+1):
        
        List_approx_ln.append((x-1)/a)
        List_ln.append(math.log(x, np.e))
        
        List_difference.append(abs(List_approx_ln[-1]-List_ln[-1]))
        a=(a+g)/2
        g=np.sqrt(a*g)   
       
        
    plt.plot(List_approx_ln)
    plt.plot(List_ln)
    
    plt.show()
    
    plt.plot(List_difference)
    plt.show()
    
    return List_approx_ln[-1] 


# ============================================================================

