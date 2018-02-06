def squared_nums(num_list):
	"""
	Squares numbers in num_list
	num_list: list of numbers
	Returns: list of these numbers squared
	"""
	new_list = [] #make new list
	for num in num_list:
		new_list.append(num ** 2)

	return new_list

def check_title(title_list):
	"""
	Removes strings in title_list that have numbers and aren't title case
	title_list: list of strings
	Returns: list of strings that are titles
	"""
	new_list = [] #make new list
	for title in title_list:
		is_a_tital = True
		temp = tital.split()
		for word in temp:
			for letter in word:
				if (letter.isdecimal()):
				is_a_tital = false
			
			if is_a_tital:
				if(word[0].isupper()):
					new_list.append(word)
	return new_list

def restock_inventory(inventory):
	"""
	Increases inventory of each item in dictionary by 10
	inventory: a dictionary with:
  	key: string that is the name of the inventory item
   	value: integer that equals the number of that item currently on hand
	Returns: updated dictionary where each inventory item is restocked
	"""
	new_dict ={}
	for inven in inventory:
		inven.items() = inven.items() +10

		new_dict.append(inven)
	return new_dict


def filter_0_items(inventory):
	"""
	Removes items that have a value of 0 from a dictionary of inventories
	inventory: dictionary with:
  	key: tring that is the name of the inventory item
   	value: nteger that equals the number of that item currently on hand
	Returns: the same inventory_dict with any item that had 0 quantity removed
	"""
	new_dict ={}
	for inven in inventory:
		if(!(inven.any(0)):
			new_dict.append(inven)
	return new_dict

 def average_grades(grades):
	"""
	Takes grade values from a dictionary and averages them into a final grade
	grades: a dictionary of grades with:
	key: string of students name
	value: list of integer grades received in class
	Returns: dictionary that averages out the grades of each student
	"""
	new_dict ={}
	for inven in inventory:
		inven = sum(inven) / len(inven)
		new_dict.append(inven)
	return new_dict


