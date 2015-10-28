## Office Space Allocation [![Coverage Status](https://coveralls.io/repos/andela-ashuaib/amity-room-allocation/badge.svg?branch=master&service=github)](https://coveralls.io/github/andela-ashuaib/amity-room-allocation?branch=master)

Checkpoint one python office allocation 
## How to use
git clone this repo into a folder, enter into the folder and run

```  - pip install -r requirements.txt ```


run 

```$ python ```

Once you are inside the python shell run this

```import main.py```

To initialize, assign Spaces class initalization to a variable like so
```
andela = Spaces()
```
This program has has an autoload method for you which can be ran like so it accepts an optional parameter
For the number of rooms required to be auto populated

```
andela.populate_spaces_with_rooms()

```
This results in autopoplating the rooms with ROOM 1 (Living), ROOM 1 (Office)... ROOM 10 (Living), ROOM 10(Office)


Autoloading the employee from input file use this method

````
andela.add_people_from_files(path)

`````
Where path should be the path to your employee lists of directories
e,g path "data/input.txt"


You can get all occupants of the room and offices in the building like so

```
andela.get_all_rooms_and_occupants()
```
To Get the occupant in a particular living space or office you can do it like so
having known the name of the office and the type if its living space or an office

```
andela.get_total_occupants(office_type,name_of_office)

e.g andela.get_total_occupants("office","ROOM 2")

```
To get the info of a person in a particluar office or living space

```
andela.get_info_of_work(name_of_person,space_type,name_of_space)

e.g andela.get_info_of_worker("ANDREW PHILLIPS","office","2")
````

To get the information of all the unallocated employees you can run the following command

```
print andela.get_unallocated_employee_for_office()
print andela.get_unallocated_employee_for_living()
```

To add more offices or more living spaces. You can pass the parameters in like so

```
andela.add_more_office("office_name")
andela.add_more_living("living_space_name")
```

To randomly allocate people to different rooms and / offices you can pass in the syntax as shown below

The person's information should be passed in a dictionary format
```
person_information = {
	'Name': "Name of Person",
	'Position': "Staff or Fellow",
	'Living' : #Optionnaly wants accomodation or not (Y or N)

}
andela.add_people_to_room(person_information)
```
