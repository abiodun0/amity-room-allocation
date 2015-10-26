"""
This files handles the model of the people that are staff or fellows at amity

"""

class People(object):
	def __init__(self,name,office_name="unallocated"):
		self.name = name
		self.office_name = office_name

	def set_office(self,office_name):
		"""
		Sets the office name for a particular fellow or staff
		"""
		self.office_name = office_name



class Fellow(People):

	def __init__(self,name,living_name="unallocated"):
		"""This calls the super class to set the maximum number of people needed
		for this office
		"""
		super(Fellow,self).__init__(name)
		self.living_name = living_name


	def set_living(self,living_name):
		"""
		Sets the living room space for all the fellows that wants acoomodation
		"""
		self.living_name = living_name


	def get_info(self):
		""" Prints out the persons info in a format manner
		no params
		no returns
		"""
		print "Name: " +self.name + "\n"
		print "Office: " +self.office_name + "\n"
		print "Living: " + self.living_name + "\n"

	pass

class Staff(People):

	def get_info(self):
		""" Prints out the persons info in a format manner
		no params
		no returns
		"""
		print "Name: " +  self.name + "\n"
		print "Office: " +self.office_name + "\n"

	pass