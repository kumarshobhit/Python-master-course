import matplotlib.pyplot as plt 
import numpy as np 

x=np.arange(10)
y1=x**2
y2=2*x+3

plt.plot(x,y1) ;
plt.plot(x,y2) ; 
plt.show()