import unittest
from models.room import *
from models.person import *

class RoomTests(unittest.TestCase):
	def setUp(self):
		""" The setup variable to be used throught the test
		"""
		self.office = Office("ROOM 11")
		self.living = Living("ROOM 12")

	def test_for_init_function(self):
		""" Test for the init functions of both 
		"""
		self.assertIs(self.office.max_people, 6)
		self.assertIs(self.living.max_people,4)

	def test_for_add_people(self):
		""" Test for the add people functions
		"""
		person = Fellow("Abiodun")
		self.office.add_person(person)
		self.assertGreater(len(self.office.people),0)

	def test_for_room_avaialble(self):
		""" Test if room is not filled setUp
		"""
		self.assertIs(self.office.is_filled(),False)
	pass


if __name__ == '__main__':
	unittest.main()