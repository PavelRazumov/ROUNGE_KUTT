import scipy as np 
import matplotlib.pyplot as plt 
from Solve import DSolve 


def drawResult(X,Y,labels): 
	labelY = labels[0] 
	labelYTrue = labels[1] 
	plt.plot(X, Y, color = 'green') 
	#plt.legend((labelY, labelYTrue)) 
	plt.show() 

#////////////////////////////////// 

f = lambda x,y,z: -((y**2 + z**2)*z + z) / (((y**2 + z**2)*z + z) ** 2 + ((y**2 + z**2)*y - y) ** 2 ) ** 0.5#z / ((y-z)**2 + y*z) ** 0.5
g = lambda x,y,z: ((y**2 + z**2)*y - y) /(((y**2 + z**2)*z + z) ** 2 + ((y**2 + z**2)*y - y) ** 2 ) ** 0.5#-y /((y-z)**2 + y*z) ** 0.5
#////////////////////////////////// 

dS = DSolve() 

dS.setStep(0.00001) 
X,Y,Z = dS.Runge_Kutta([g,f],[(0,0),(0,0.001)]) 
drawResult(Y,Z,('X', 'Y'))