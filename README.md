## Office Space Allocation
Checkpoint one python office allocation 
## How to use
git clone this repo and enter into the folder that you can run python
run ```python main.py```
and use the following utility codes

```
andela = Spaces()
andela.populate_spaces_with_rooms()
andela.add_people_from_files("input.txt")
andela.get_all_rooms_and_occupants()

andela.get_total_occupants("office","2")
andela.get_info_of_worker("Abiodun","office","2")
print andela.get_unallocated_employee_for_office()
print andela.get_unallocated_employee_for_living()
```
