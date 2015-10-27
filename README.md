## Office Space Allocation (Test Coverage:83%)
Checkpoint one python office allocation 
## How to use
git clone this repo and enter into the folder that you can run python
run ```python main.py```
and use the following utility codes
Running Tests 
```
python -m unittest tests.test_room
python -m unittest tests.test_main
python -m unittest tests.test_people

using coverage

coverage run  -m  tests.test_main
```
To initialize assign Spaces initalization to a variable like so
```
andela = Spaces()
```
This program has has an autoload method for you which can be ran like so
```
andela.populate_spaces_with_rooms()

```
This results in autopoplating the rooms with ROOM 1 (Living), ROOM 1 (Office)... ROOM 10 (Living), ROOM 10(Office)


Autoloading the employee from input file use this method

````
andela.add_people_from_files("input.txt")

`````

Where path can be anything you have your employeers data


You can get all occupants of the room and offices in the building like so

```
andela.get_all_rooms_and_occupants()
```
To Get the occupant in a particular living space or office you can do it like so

```
andela.get_total_occupants(office_type,name_of_office)

e.g andela.get_total_occupants("office","2")

```
To get info of workers in a particular room

```
andela.get_info_of_work(name_of_person,space_type,name_of_space)

e.g andela.get_info_of_worker("ANDREW PHILLIPS","office","2")
````
To get the information of all the unallocated employees you can run the following command

```
print andela.get_unallocated_employee_for_office()
print andela.get_unallocated_employee_for_living()
```

To Add more living spaces or offices  you can pass the syntax in like so

```
andela.add_more_office("office_name")
andela.add_more_living("living_space_name")
```

To randomly allocate people to different rooms and / offices you can pass in the syntax as shown below
```
person_information = {
	'Name': "Name of Person",
	'Position': "Staff or Fellow",
	'Living' : #Optionnaly wants accomodation or not (Y or N)

}
andela.add_people_to_room(person_information)
```
