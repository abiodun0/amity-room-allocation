## Office Space Allocation [![Coverage Status](https://coveralls.io/repos/andela-ashuaib/amity-room-allocation/badge.svg?branch=master&service=github)](https://coveralls.io/github/andela-ashuaib/amity-room-allocation?branch=master)

Checkpoint one: Python Office Allocation 

## How to use
Clone this repo into a folder, enter into the folder and run

```
pip install -r requirements.txt
```

Run the python interpreter in your command line

```
$ python
```

Once you are inside the python shell run this

```python
import main.py
```

To initialize, assign Spaces class initalization to a variable like so

```python
andela = Building()
```

This program has has an autoload method for you which can be ran like so it accepts an optional parameter
For the number of rooms required to be auto populated

```python
andela.populate_spaces_with_rooms()
```
This results in autopoplating the rooms with ROOM 1 (Living), ROOM 1 (Office)... ROOM 10 (Living), ROOM 10(Office)


Autoloading the employee from input file use this method

```python
andela.add_people_from_files(path)
```

`path` should be the path to your employee list eg. Path => "data/input.txt"


You can get all occupants of the room and offices in the building like so

```python
andela.get_all_rooms_and_occupants()
```

To get the occupant in a particular living space or office you can do it like so
having known the name of the office and the type if its living space or an office

```python
andela.get_total_occupants("office","ROOM 2")
```

To get the information of a person in a particluar office or living space

```python
andela.get_info_of_worker("ANDREW PHILLIPS", "office", "2")
````

To get the information of all the unallocated employees you can run the following command

```python
print andela.get_unallocated_employee_for_office()
print andela.get_unallocated_employee_for_living()
```

To add more offices or more living spaces. You can pass the parameters in like so

```python
andela.add_office("office_name")
andela.add_livingspace("living_space_name")
```

To randomly allocate people to different rooms and / offices you can pass in the syntax as shown below

The person is first passed as an employee which returns either a staff or a fellow object
Then the utility function of add_people_to_room is called like so

```python
biodun = andela.add_new_employee("Abiodun Shuaib","FELLOW","Y")
jacob = andela.add_new_employee("Jacob Filter","STAFF")
andela.add_people_to_room(biodun)
```
