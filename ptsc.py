import numpy as np
import pandas as pd

class NullScreenTest():
	
	
	def __init__(self, parameters = []):
		self.par = parameters
	
	def create_ideal_pattern(self):
		x = linspace(0, 1, 500)*self.par.CCDX - self.par.CCDX/2
		y = linspace(0, 1, 500)*self.par.CCDY - self.par.CCDY/2

	def generate_NS(self):
		self.p1 = self.create_ideal_pattern()
		self.p2 = self.project_to_surface()
		self.p3 = self.project_to_NullScreen()	
