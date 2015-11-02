import unittest
from models.people import *
from main import *
from models.room import *

class TestOfMainSpacesAllocation(unittest.TestCase):
	"""
	This are for testing the main.py class function and method
	"""
	def setUp(self):
		"""
		This is to setup for the rest of the testing the input
		"""
		self.andela = Building()

	def test_to_check_all_all_lists_are_empty(self):
		"""
		This checks if the class is successfully initialized
		"""

		self.assertEqual(len(self.andela.spaces['offices']),0)
		self.assertEqual(len(self.andela.spaces['livingspaces']),0)

	def test_add_living(self):
		"""
		This checks for testing for adding more lving spaces
		"""
		self.andela.add_livingspace("Matrix")
		self.assertEqual(len(self.andela.spaces['livingspaces']),1)
	
	def test_add_office(self):
		"""
		This checks for testing for adding more office spaces
		"""
		self.andela.add_office("Joe")
		self.assertEqual(len(self.andela.spaces['offices']),1)

	def test_populate_spaces_with_rooms(self):
		"""
		Test for the randomly spaces method to make sure the offices length is up to 10
		"""

		self.andela.populate_spaces_with_rooms(10)
		self.assertEqual(len(self.andela.spaces['offices']),10)
		self.assertEqual(len(self.andela.spaces['livingspaces']),10)

	def test_populate_from_files(self):
		"""
		Test if the employees are populated
		"""

		self.andela.populate_spaces_with_rooms()
		self.andela.add_people_from_files("data/input.txt")
		self.assertGreater(len(self.andela.employees),0)

	def test_for_find_room_method(self):
		"""
		Test for add room as an instance of Amity
		"""

		self.andela.populate_spaces_with_rooms()
		room = self.andela.find_room("offices","ROOM 2")
		office = self.andela.find_room("livingspaces","ROOM 2")
		self.assertIsInstance(room,Room)
	
	def test_allocate_offices(self):
		"""
		Test the llocate method of the Spaces class
		"""

		self.andela.populate_spaces_with_rooms()
		person = Fellow("Abiodun")
		self.andela.allocate_to_space(person,"offices")
		self.assertEqual(len(self.andela.allocated_people['offices']),1)

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

	def test_for_print_all_occupants_name_filled(self):
		""" 
		Test for print filled rooms names 
		"""

		self.andela.populate_spaces_with_rooms(2)
		self.andela.add_people_from_files("data/input.txt")
		
		names = self.andela.print_occupants_names("livingspaces")
		self.assertIsNone(names)
		

	def test_for_find_room_function(self):
		"""
		Test for find room when the room is filled
		"""
		self.andela.populate_spaces_with_rooms(2)
		self.andela.add_people_from_files("data/input.txt")

		room_office = self.andela.find_room("offices","ROOM 2")
		room_living = self.andela.find_room("livingspaces","ROOM 2")

		self.assertIsInstance(room_living,Living)
		self.assertIsInstance(room_office,Office)


	def test_for_print_all_occupants_name_not_filled(self):
		""" 
		Test for print not filled rooms names 
		"""

		self.andela.populate_spaces_with_rooms(15)
		self.andela.add_people_from_files("data/input.txt")
		office = self.andela.print_occupants_names("offices")
		
		self.assertIsNone(office)

	def test_for_add_new_employee(self):
		""" 
		Test for add new employee
		"""
		biodun = self.andela.add_new_employee("Abiodun Shuaib","FELLOW","Y")
		
		self.assertIsInstance(biodun,Fellow)

		


	def test_for_check_and_return_available_space(self):
		""" 
		This check for return available spaces left in amity if there is any 
		"""
		self.andela.populate_spaces_with_rooms(2)

		office = self.andela.check_and_return_available_space("offices")

		self.assertIsInstance(office,Room)
	def test_for_check_and_return_available_spaces_filled(self):
		"""
		Check for if room is filled
		"""
		self.andela.populate_spaces_with_rooms(2)
		self.andela.add_people_from_files("data/input.txt")
		office = self.andela.check_and_return_available_space("offices")
		self.assertNotIsInstance(office,Room)
		self.assertGreater(self.andela.filled_spaces['offices'],0)
		self.assertGreater(self.andela.filled_spaces['livingspaces'],0)
	def test_for_get_all_rooms_and_occupants(self):
		"""
		Test for printable occupants of an office or living space
		"""
		all_spaces = self.andela.get_all_rooms_and_occupants()
		office = self.andela.print_occupants_names("offices")
		living = self.andela.print_occupants_names("livingspaces")
		self.assertIsNone(all_spaces)
		self.assertIsNone(office)
		self.assertIsNone(living)




if __name__ == '__main__':
	unittest.main()