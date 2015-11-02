import unittest
from models.person import *

class PeopleTest(unittest.TestCase):
	
	def setUp(self):
		""" Test data for the test
		"""
		self.fellow = Fellow("Abiodun")
		self.staff = Staff("Ebun")

	def test_for_init_function(self):
		""" Test for the init function
		"""
		self.assertIsInstance(self.fellow,Fellow)
		self.assertIsInstance(self.staff,Staff)

	def test_for_set_office(self):
		""" Test for the set_office function to make sure it returns the set 
		office name
		"""
		self.fellow.set_office("Room 5")
		self.assertIs(self.fellow.office_name, "Room 5")

	def test_for_init_for_fellow(self):
		"""
		Test for init function with fellow
		"""
		self.assertIsNone(self.fellow.living_name)

	def test_for_set_living_for_fellow_class(self):
		"""
		Test for allocation in fellow class

		"""
		self.fellow.set_living("Amity")
		self.assertIs(self.fellow.living_name,"Amity")
	
	def test_for_get_info(self):
		"""

		Test for getting employees information
		"""

		self.assertIsNone(self.fellow.get_info())
		self.assertIsNone(self.staff.get_info())
	


if __name__ == '__main__':
	unittest.main()