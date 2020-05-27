import numpy as np
#import pandas as pd

class Ray():
	
	def __init__(self, x=None, y=None, z=None, p = None):
		if p != None
			self.p = p
		elif None in x:
			self.p = np.dstack([x, y, z])
		else:
			raise('Cannot create CriticalRayPoint, input inexistent')
			
	def separate(self):
		x = self.p[:,:,0]
		y = self.p[:,:,1]
		z = self.p[:,:,2]
		return x, y, z
		
	def scaleRay(self, scale = 1):
		norm = np.sqrt(np.sum(self.p**2, axis = 2))
		norm = scale/np.dstack([norm, norm, norm])
		return  factorRay(self, norm)
		
		
		
	
class NullScreenTest():
		
	def __init__(self, parameters = None):
		self.par = parameters
		self.p = Ray(x=0, y=0, z= self.par.PinholeDistance.values)
		self.p1 = self.create_ideal_pattern()
		self.p2 = self.project_sensor_to_surface()

	def create_ideal_pattern(self):
		xl = np.linspace(-1, 1, 500)*self.par.CCDX.values 
		yl = np.linspace(-1, 1, 500)*self.par.CCDY.values
		x, y = np.meshgrid(xl, yl)
		z = 0*x + (self.par.FocalDistance.values + self.par.PinholeDistance.values)
		return Ray(x = x, y = y, z = z)
		
	def project_sensor_to_surface(self): 
		t = 1
		I = addRay(self.p, self.p1.scaleRay(-1)).scaleRay(t)
		return addRay(self.p1, I)
	
	def project_surface_to_screen(self):
		w = 1
		I = addRay(self.p, self.p1.scaleRay(-1)).scaleRay()
		R = addRay(I, N.scaleRay(dotRay(I, N))).scaleRay(w)
		



def dotRay(A, B):
	return np.sum(A.p*B.p, axis = 2)

def addRay(A, B):
	xa, ya, za = A.separate()
	xb, yb, zb = B.separate()
	return Ray(x = xa + xb, y = ya + yb, z = za + zb)
	
def factorRay(A, B):
	return Ray(A.p * B)
	
