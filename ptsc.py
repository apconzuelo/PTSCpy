class NullScreenTest(parameters):
	
	
	def __init__(self,parameters):
		self.par = parameters
	
	def create_ideal_pattern(self):
		x = np.linspace(0, 1, par.NumberOfPoints)*self.par.CCDx - self.par.CCDx/2
		y = np.linspace(0, 1, par.NumberOfPoints)*self.par.CCDy - self.par.CCDy/2

	def generate_NS(self):
		self.p1 = self.create_ideal_pattern()
		self.p2 = self.project_to_surface()
		self.p3 = self.project_to_NullScreen()	
