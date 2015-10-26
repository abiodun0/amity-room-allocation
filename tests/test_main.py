import unittest
from models.people import *
from main import *
from models.amity import *

class TestOfMainSpacesAllocation(unittest.TestCase):
	"""
	This are for testing the main.py class function and method
	"""
	def setUp(self):
		"""
		This is to setup for the rest of the testing the input
		"""
		self.andela = Spaces()

	def test_to_check_all_all_lists_are_empty(self):
		"""
		This checks if the class is successfully initialized
		"""

		self.assertEqual(len(self.andela.offices),0)
		self.assertEqual(len(self.andela.livings),0)

	def test_read_input_files(self):
		"""
		Check if the input file returns the required list

		"""

		lists = self.andela.read_input_files("data/input.txt")
		self.assertGreater(len(lists),0)
	def test_populate_spaces_with_rooms(self):
		"""
		Test for the randomly spaces method to make sure the offices length is up to 10
		"""

		self.andela.populate_spaces_with_rooms(10)
		self.assertEqual(len(self.andela.offices),10)
		self.assertEqual(len(self.andela.livings),10)

	def test_populate_from_files(self):
		"""
		Test if the employees are populated
		"""

		self.andela.populate_spaces_with_rooms()
		self.andela.add_people_from_files("data/input.txt")
		self.assertGreater(len(self.andela.allocated_employee_for_office),0)

	def test_for_find_room_method(self):
		"""
		Test for add room as an instance of Amity
		"""

		self.andela.populate_spaces_with_rooms()
		room = self.andela.find_room("office","2")
		office = self.andela.find_room("living","2")
		self.assertIsInstance(room,Amity)
	def test_allocate_offices(self):
		"""
		Test the llocate method of the Spaces class
		"""

		self.andela.populate_spaces_with_rooms()
		person = Fellow("Abiodun")
		self.andela.allocate_to_offices(person)
		self.assertEqual(len(self.andela.allocated_employee_for_office),1)

	def test_for_get_unallocated_people_for_offices(self):
		"""
		This checks that there is a message for unallocated people for offices
		"""
		self.andela.populate_spaces_with_rooms()
		self.andela.add_people_from_files("data/input.txt")
		message = self.andela.get_unallocated_employee_for_office()

		self.assertIsNotNone(message)
	def test_for_get_unallocated_people_for_livings(self):
		"""
		This checks that there is a message for unallocated people for living space
		"""
		self.andela.populate_spaces_with_rooms()
		self.andela.add_people_from_files("data/input.txt")
		message = self.andela.get_unallocated_employee_for_living()

		self.assertIsNotNone(message)
		

	def test_for_check_and_return_avaialable_space(self):
		""" this check for return available spaces left in amity if there is any 
		"""
		self.andela.populate_spaces_with_rooms(2)

		office = self.andela.check_and_return_avaialable_space(self.andela.offices)

		self.assertIsInstance(office,Amity)
	def test_for_check_and_return_available_spaces_filled(self):
		"""check for if room is filled"""
		self.andela.populate_spaces_with_rooms(2)
		self.andela.add_people_from_files("data/input.txt")
		office = self.andela.check_and_return_avaialable_space(self.andela.offices)
		self.assertNotIsInstance(office,Amity)
		self.assertGreater(self.andela.filled_offices,0)
		self.assertGreater(self.andela.filled_livings,0)
	def test_for_get_all_rooms_and_occupants(self):
		"""
		Test for printable occupants of an office or living space
		"""
		all_spaces = self.andela.get_all_rooms_and_occupants()
		office = self.andela.print_office_names()
		living = self.andela.print_living_names()
		self.assertIsNone(all_spaces)
		self.assertIsNone(office)
		self.assertIsNone(living)




if __name__ == '__main__':
	unittest.main()