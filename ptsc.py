import numpy as np
#import pandas as pd

class CriticalRayPoint():
	
	def __init__(self, x=None, y=None, z=None):
		if len(x) > 0:
			self = np.vstack([x, y, z]).T
		else:
			raise('Cannot create CriticalRayPoint, input inexistent')
			
	def separate(self):
		x = self[:, 0]
		y = self[:, 1]
		z = self[:, 2]
		return x, y, z
	
	

	
	
	
class NullScreenTest():
		
	def __init__(self, parameters = []):
		self.par = parameters
		self.p1 = self.create_ideal_pattern()
	
	def create_ideal_pattern(self):
		x = np.linspace(-1, 1, 500)*self.par.CCDX.values 
		y = np.linspace(-1, 1, 500)*self.par.CCDY.values
		z = np.ones([1, 500])*(self.par.FocalDistance.values + self.par.PinholeDistance.values)
		return CriticalRayPoint(x, y, z)

	def generate_NS(self):
		self.p1 = self.create_ideal_pattern()
		self.p2 = self.project_to_surface()
		self.p3 = self.project_to_NullScreen()	
