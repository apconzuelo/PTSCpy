import numpy as np
#import pandas as pd

class CriticalRayPoint():
	
	def __init__(self, x=None, y=None, z=None):
		if len(x) > 0:
			self.p = np.dstack([x, y, z])
		else:
			raise('Cannot create CriticalRayPoint, input inexistent')

	
	
	
class NullScreenTest():
		
	def __init__(self, parameters = []):
		self.par = parameters
		self.p1 = self.create_ideal_pattern()
	
	def create_ideal_pattern(self):
		xl = np.linspace(-1, 1, 500)*self.par.CCDX.values 
		yl = np.linspace(-1, 1, 500)*self.par.CCDY.values
		
		x, y = np.meshgrid(xl, yl)
		z = np.ones(xl.shape)*(self.par.FocalDistance.values + self.par.PinholeDistance.values)
		return CriticalRayPoint(x, y, z)

	def generate_NS(self):
		self.p1 = self.create_ideal_pattern()
		self.p2 = self.project_to_surface()
		self.p3 = self.project_to_NullScreen()	
