import numpy as np
import pandas as pd
from types import SimpleNamespace 

class Ray():
	
	def __init__(self, x= None, y= None, z=None, p=None):	
		if np.array(p != None).any():
			self.p = p
		elif np.array(x != None).any():
			self.p = np.dstack([x, y, z])
		else:
			raise("Invalid input for Ray Creation, x not a vector")
			
	def separate(self):
		x = self.p[:,:,0]
		y = self.p[:,:,1]
		z = self.p[:,:,2]
		return x, y, z
		
	def scaleRay(self, scale = 1):
		norm = np.sqrt(np.sum(self.p**2, axis = 2))
		norm = scale/norm
		return  factorRay(self, dstack[norm, norm, norm])
		
		
		
	
class NullScreenTest():
		
	def __init__(self, parameters = None):
		self.par = parameters
		self.p = Ray(x=0, y=0, z= parameters.PinholeDistance)
		self.p1 = self.create_ideal_pattern()
		self.p2 = self.project_sensor_to_surface()

	def create_ideal_pattern(self):
		'''
		xl = np.linspace(-1, 1, 500)*5 
		yl = np.linspace(-1, 1, 500)*5
		x, y = np.meshgrid(xl, yl)
		z = 0*x + 80
		'''
		
		xl = np.linspace(-1, 1, 500)*self.par.CCDX 
		yl = np.linspace(-1, 1, 500)*self.par.CCDY
		x, y = np.meshgrid(xl, yl)
		z = 0*x + (self.par.FocalDistance + self.par.PinholeDistance)
		
		return Ray(x = x, y = y, z = z)
		
	def project_sensor_to_surface(self): 
		r = self.par.CurvatureRadious
		I = addRay(self.p, self.p1.scaleRay(-1))
		x, y, z = self.p1.separate()
		Ix, Iy, Iz = I.separate()
		
		A = Iz**2
		B = 2*(Iz - r*Iy)
		C = (z**2 - 2*r*y)
		
		t = -B + np.sqrt(B**2 - 4*A*C)
		t = t/(2*A)
		return addRay(self.p1, I.scaleRay(t))
	
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
	return Ray(p = A.p * B)
	
	
#sim = NullScreenTest()
#print(sim.p2)
