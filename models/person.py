"""
This files handles the model of the people that are staff or fellows at amity

"""


class Person(object):

    def __init__(self, name, office_name=None):
        self.name = name
        self.office_name = office_name

    def set_office(self, office_name):
        """
        Sets the office name for a particular fellow or staff
        """
        self.office_name = office_name


class Fellow(Person):

    def __init__(self, name,wants_livingspace="N",living_name=None):
        """
        This calls the super class to set the maximum number of people needed
        for this office
        """
        super(Fellow, self).__init__(name)
        self.living_name = living_name
        self.wants_livingspace = wants_livingspace

    def set_living(self, living_name):
        """
        Sets the living room space for all the fellows that wants acoomodation
        """
        self.living_name = living_name

    def set_livingspace(self, wants_livingspace):
    	""" 
    	Sets if the fellow wants living space or not
    	"""
    	self.wants_livingspace = wants_livingspace

    def get_info(self):
        """
        Prints out the persons info in a format manner
        no params
        no returns
        """
        print "Name: " + self.name + "\n"
        print "Office: " + str(self.office_name) + "\n"
        print "Living: " + str(self.living_name) + "\n"

    pass


class Staff(Person):

    def get_info(self):
        """
        Prints out the persons info in a format manner
        no params
        no returns
        """
        print "Name: " + self.name + "\n"
        print "Office: " + str(self.office_name) + "\n"

    pass
