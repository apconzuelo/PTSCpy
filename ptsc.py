import numpy as np
import pandas as pd

class NullScreenTest():
	
	
	def __init__(self, parameters = []):
		self.par = parameters
		self.p1 = []
	
	@classmethod()
	def create_ideal_pattern(self):
		p1 = np.zeros(3, 500)
		p1[0‚ :] = np.linspace(0, 1, 500)*self.par.CCDX - self.par.CCDX/2
		p1[1, :] = np.linspace(0, 1, 500)*self.par.CCDY - self.par.CCDY/2
		p1[2, :] = p1[2, :] + self.par.FocalLength + self.par.b
		return p1

	def generate_NS(self):
		self.p1 = self.create_ideal_pattern()
		self.p2 = self.project_to_surface()
		self.p3 = self.project_to_NullScreen()	
