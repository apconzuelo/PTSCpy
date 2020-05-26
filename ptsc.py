import numpy as np
#import pandas as pd

class NullScreenTest():
	
	
	def __init__(self, parameters = []):
		self.par = parameters
		self.p1 = self.create_ideal_pattern()
	
	def create_ideal_pattern(self):
		x = np.linspace(-1, 1, 500)*self.par.CCDX.values 
		y = np.linspace(-1, 1, 500)*self.par.CCDY.values
		z = np.ones([1, 500])*(self.par.FocalDistance.values + self.par.PinholeDistance.values)
		return np.vstack([x, y, z])

	def generate_NS(self):
		self.p1 = self.create_ideal_pattern()
		self.p2 = self.project_to_surface()
		self.p3 = self.project_to_NullScreen()	
