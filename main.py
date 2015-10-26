from models.people import *
from models.amity import *
import re
from random import choice


class Spaces(object):

	def __init__(self):
		"""initialzing global variables
		offices,living spaces,allocated employees are all set to empty lists
		it takes care of living spaces and offices that are filled as well
		"""
		self.offices = []
		self.filled_offices = []
		self.livings = []
		self.filled_livings = []
		self.employees = []
		self.allocated_employee_for_office = []
		self.allocated_employee_for_living = []
		self.unallocated_employee_living = []
		self.unallocated_employee_office = []

	def read_input_files(self,path):
		"""this utility function reads from the input file
		strip the tabs seperate it into dictionaries and append it to the employess array
		@params path to file
		returns lists
		"""
		new_employees = []
		with open(path,"r") as input_file:
			file_contents = input_file.read().splitlines()

		for files in file_contents:
			temp =  re.split(r'\t+', files.rstrip('\t'))
			Person = {
			'Name': unicode(temp[0], errors='ignore'),
			'Position': temp[1],
			'Living': temp[2] if 2 < len(temp) else None
			}
			self.employees.append(Person)
			new_employees.append(Person)

		return new_employees

	def add_people_from_files(self,path):
		"""
		Get files from input sources and randomly assign them to room by iterating
		through each of the files
		@params path
		@returns void
		"""
		pending_allocation = self.read_input_files(path)
		for person in pending_allocation:
			self.add_people_to_room(person)

	def populate_spaces_with_rooms(self):
		""" This auto populates the offices and the living spaces in the andela classes
		it poplates both the room and the office from 1 - 10 
		"""
		for i in range(1, 3):
			single_office = Office(str(i))
			single_living = Living(str(i))
			self.offices.append(single_office)
			self.livings.append(single_living)

	def allocate_to_offices(self,person):
		""" This is a utility method used to assign offices to fellows and staffs alike since each 
		employee must have an office it is appended un the add_people to room method
		@params instace of Person
		"""
		office = self.check_and_return_avaialable_space(self.offices)
		if isinstance(office, Office):
			office.add_people(person)
			self.allocated_employee_for_office.append(person)
			
		else:
			self.unallocated_employee_office.append(person)
			print str(office)

	def add_people_to_room(self,worker):
		""" this is the function that gets called each time a fellow or a staff is to be randomly assigned to an office or a room
		it made use of the recursive method check_if_room_is_filled()
		@params person's dictionary, option only availale for fellows(Y for living space no for none)
		(might change, thinking if dictionary should be an elegant way of executing this)
		"""
		if worker['Position'] == 'STAFF':
			person = Staff(worker['Name'])
			
		elif worker['Position'] == 'FELLOW':
			person = Fellow(worker['Name'])
			
		else:
			return "Position Not Available at andela"

		self.allocate_to_offices(person)

		#this randomly assigns living spaces for fellows that have an option of living space
		if worker['Position'] == 'FELLOW' and worker['Living'] == 'Y':
			living = self.check_and_return_avaialable_space(self.livings)
			if isinstance(living, Living):
				living.add_people(person)
				self.allocated_employee_for_living.append(person)
			else:
				print str(living)
				self.unallocated_employee_living.append(person)


	def check_and_return_avaialable_space(self, space_type):
		""" This is a recursive function to randomly allocate living space and offices for staffs and fellows alike 
		This append filled rooms to self.filled_offices or self.filled_livings respectively
		@returns instace of Office or Living if there are spaces left
		@returns string if there isn't
		@params space_type(offices or livings)
		"""
		if space_type:
			room = choice(space_type)
			if room.is_available():
				return room
			else:
				space_type.remove(room)
				self.filled_offices.append(room) if space_type is self.offices else self.filled_livings.append(room)
				return self.check_and_return_avaialable_space(space_type)
		else:
			return "All Offices are filled up" if space_type is self.offices else "All Living Spaces Are Filled Up"

	def print_office_names(self):
		"""get the number of people allocated to all the offices on a print_living_name
		no @params needed
		"""
		if self.filled_offices:
			for office in self.filled_offices:
				print "\n" +str(office)
				print office.get_people()
		for office in self.offices:
			print "\n" +str(office) 
			print office.get_people()

	def print_living_names(self):
		"""get the number of people allocated to all the living on a print_living_name
		no @params needed
		"""
		if self.filled_livings:
			for living in self.filled_livings:
				print  "\n" + str(living)
				print living.get_people()
		for living in self.livings:
			print  "\n" + str(living)
			print living.get_people()

	def get_all_rooms_and_occupants(self):
		""" Returns all the occupants Room names Offices Names in Amity
		"""
		self.print_living_names()
		self.print_office_names()

	def get_total_occupants(self, space_type, name):
		""" This is to get the total occupants of a particular room
		the params needed are the space_type which can either be offices or living space
		Then the name of the room range from 1 - 10
		for eg andela.get_total_occupants("office","2") gets the total number of offices in ROOM 2 (Office)
		"""
		room = self.find_room(space_type, name)
		if isinstance(room,Amity):
			if room.get_people():
				print "\n" + str(room) + " Occupants"
				print room.get_people()
			else:
				print "No Occupant in this room"
		else:
			print "Invalid room name"
	def get_info_of_worker(self,person_name,space_type,number):
		room = self.find_room(space_type,number)
		if room:
			for person in room.people:
				if person_name == person.name:

					return person.get_info()

	def find_room(self, space_type, number):
		""" This is a utility function to get a particular room properties in amity
		@params space_type(office or living), room number
		@returns instace of ROOM
		"""
		if space_type is "office":
			for room in self.offices:
				if number is room.name:
					return room
			for room in self.filled_offices:
				if number is room.name:
					return room
		else:
			for room in self.livings:
				if number is room.name:
					return room
			for room in self.filled_livings:
				if number is room.name:
					return room

	def get_unallocated_employee_for_office(self):
		""" Get the number of people that are yet to be allocated to an office
		@params none
		@returns strings of names / a string passing in the error
		"""
		print "\n" + "Unallocated people for office space"
		return ', '.join([person.name for person in self.unallocated_employee_office]) if len(self.unallocated_employee_office) > 0 else  "No Unallocated Fellows\Staffs for Office Space"
	def get_unallocated_employee_for_living(self):
		"""Returns the number of fellows that are yet to be allocated living spaces
		@params none
		@return string of names

		"""
		print "\n" + "Unallocated people for living space"
		return ', '.join([person.name for person in self.unallocated_employee_living]) if len(self.unallocated_employee_living) > 0 else  "No Unallocated Fellow\Staffs for Living Space"




    	



if __name__ == '__main__':
    andela = Spaces()
    andela.populate_spaces_with_rooms()
    andela.add_people_from_files("data/input.txt")
    andela.get_all_rooms_and_occupants()

   


    andela.get_total_occupants("office","2")
    andela.get_info_of_worker("ANDREW PHILLIPS","office","2")
    print andela.get_unallocated_employee_for_office()
    print andela.get_unallocated_employee_for_living()


