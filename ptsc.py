import numpy as np
import pandas as pd

class NullScreenTest():
	
	
	def __init__(self, parameters = []):
		self.par = parameters
	
	def create_ideal_pattern(self):
		p1 = np.ones([3, 500])
		p1[0‚ :] = np.linspace(-1, 1, 500)*self.par.CCDX.values[0] 
		p1[1, :] = np.linspace(-1, 1, 500)*self.par.CCDY.values[0]
		'''
		p1[0, :] = np.linspace(0, 1, 500)*5
		p1[1, :] = np.linspace(0, 5, 500)
		'''
		p1[2, :] = p1[2, :]*(self.par.FocalLength.values[0] + self.par.b.values[0])
		return p1

	def generate_NS(self):
		self.p1 = self.create_ideal_pattern()
		self.p2 = self.project_to_surface()
		self.p3 = self.project_to_NullScreen()	
