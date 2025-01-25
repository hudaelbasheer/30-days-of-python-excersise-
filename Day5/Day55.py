# Level 1
# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
items_list = ['apple', 'banana', 'mango', 'orange', 'grape', 'pineapple']

# 3. Find the length of your list
print(len(items_list))

# 4. Get the first item, the middle item, and the last item of the list
print(items_list[0])  # First item
print(items_list[len(items_list) // 2])  # Middle item
print(items_list[-1])  # Last item

# 5. Declare a list with mixed data types
mixed_data_types = ['Hidayah Bashir Dayyib', 25, 1.65, 'Married', 'Kano, Nigeria']

# 6. Declare a list of IT companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list
print(it_companies)

# 8. Print number of companies in the list
print(len(it_companies))

# 9. Print first, middle, and last company
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

# 10. Modify one of the companies
it_companies[2] = 'Meta'
print(it_companies)

# 11. Add an IT company
it_companies.append('Tesla')
print(it_companies)

# 12. Insert a company in the middle
it_companies.insert(len(it_companies) // 2, 'Samsung')
print(it_companies)

# 13. Change a company to uppercase (excluding 'IBM')
it_companies[1] = it_companies[1].upper()
print(it_companies)

# 14. Join with '#; '
print('#; '.join(it_companies))

# 15. Check if a company exists
print('Apple' in it_companies)

# 16. Sort the list
it_companies.sort()
print(it_companies)

# 17. Reverse the list
it_companies.reverse()
print(it_companies)

# 18. Slice the first 3 companies
print(it_companies[:3])

# 19. Slice the last 3 companies
print(it_companies[-3:])

# 20. Slice the middle company or companies
middle_index = len(it_companies) // 2
print(it_companies[middle_index])

# 21-25. Remove first, middle, last, and clear list
it_companies.pop(0)
print(it_companies)

it_companies.pop(len(it_companies) // 2)
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

# 26. Join front-end and back-end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# 27. Insert Python and SQL after Redux
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

# Level 2
# List of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(min_age, max_age)

# Add min and max age again
ages.append(min_age)
ages.append(max_age)
print(ages)

# Find median
median_age = (ages[len(ages) // 2] + ages[len(ages) // 2 - 1]) / 2
print(median_age)

# Find average
average_age = sum(ages) / len(ages)
print(average_age)

# Range of ages
range_of_ages = max_age - min_age
print(range_of_ages)

# Compare min-average and max-average
print(abs(min_age - average_age))
print(abs(max_age - average_age))

# Find middle country
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_country = countries[len(countries) // 2]
print(middle_country)

# Split countries list
half = len(countries) // 2
first_half = countries[:half + 1]
second_half = countries[half + 1:]
print(first_half)
print(second_half)

# Unpack first three countries
first, second, third, *scandic = countries
print(first, second, third)
print(scandic)

# Level 1

# 1. Create an empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# 2. Create a tuple containing names of your sisters and brothers
sisters = ("Fatimah", "Aisha", "Zainab")
brothers = ("Abdullahi", "Yusuf", "Ibrahim")
print("Sisters:", sisters)
print("Brothers:", brothers)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print("Siblings:", siblings)

# 4. How many siblings do you have?
num_siblings = len(siblings)
print("Number of siblings:", num_siblings)

# 5. Modify the siblings tuple and add the name of your father and mother
family_members = siblings + ("Father", "Mother")
print("Family members:", family_members)

# Level 2
# Level 2

# 1. Unpack siblings and parents from family_members
siblings = family_members[:-2]  # Extract all except the last two (Father, Mother)
parents = family_members[-2:]  # Extract the last two (Father, Mother)
print("Siblings (unpacked):", siblings)
print("Parents (unpacked):", parents)

# 2. Create fruits, vegetables and animal products tuples
fruits = ("Apple", "Banana", "Orange")
vegetables = ("Tomato", "Carrot", "Spinach")
animal_products = ("Milk", "Egg", "Cheese")

# 3. Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)

# 4. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)

# 5. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]  # Two middle items for even-length list
else:
    middle_items = food_stuff_lt[middle_index]  # One middle item for odd-length list
print("Middle item(s):", middle_items)

# 6. Slice out the first three items and the last three items from the food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# 7. Delete the food_stuff_tp tuple completely
del food_stuff_tp
print("food_stuff_tp tuple has been deleted.")

# 8. Check if an item exists in a tuple
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

# Check if 'Estonia' is a nordic country
is_estonia_nordic = "Estonia" in nordic_countries
print("Is Estonia a nordic country?", is_estonia_nordic)

# Check if 'Iceland' is a nordic country
is_iceland_nordic = "Iceland" in nordic_countries
print("Is Iceland a nordic country?", is_iceland_nordic)

# Level 2

# 1. Unpack siblings and parents from family_members
siblings = family_members[:-2]  # Extract all except the last two (Father, Mother)
parents = family_members[-2:]  # Extract the last two (Father, Mother)
print("Siblings (unpacked):", siblings)
print("Parents (unpacked):", parents)

# 2. Create fruits, vegetables and animal products tuples
fruits = ("Apple", "Banana", "Orange")
vegetables = ("Tomato", "Carrot", "Spinach")
animal_products = ("Milk", "Egg", "Cheese")

# 3. Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)

# 4. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)

# 5. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]  # Two middle items for even-length list
else:
    middle_items = food_stuff_lt[middle_index]  # One middle item for odd-length list
print("Middle item(s):", middle_items)

# 6. Slice out the first three items and the last three items from the food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# 7. Delete the food_stuff_tp tuple completely
del food_stuff_tp
print("food_stuff_tp tuple has been deleted.")

# 8. Check if an item exists in a tuple
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

# Check if 'Estonia' is a nordic country
is_estonia_nordic = "Estonia" in nordic_countries
print("Is Estonia a nordic country?", is_estonia_nordic)

# Check if 'Iceland' is a nordic country
is_iceland_nordic = "Iceland" in nordic_countries
print("Is Iceland a nordic country?", is_iceland_nordic)

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Sets Exercises: Level 1
# 1. Find the length of the set it_companies
print("Length of it_companies:", len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("it_companies after adding 'Twitter':", it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update({'Netflix', 'Tesla', 'Zoom'})
print("it_companies after adding multiple companies:", it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Facebook')  # Use remove
print("it_companies after removing 'Facebook':", it_companies)

# 5. Difference between remove and discard
# Remove raises a KeyError if the item is not in the set, while discard does not.
it_companies.discard('NonExistentCompany')  # This will not raise an error

# Sets Exercises: Level 2
# 1. Join A and B
A_B_union = A.union(B)
print("A union B:", A_B_union)

# 2. Find A intersection B
A_B_intersection = A.intersection(B)
print("A intersection B:", A_B_intersection)

# 3. Is A subset of B
is_subset = A.issubset(B)
print("Is A a subset of B?", is_subset)

# 4. Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?", are_disjoint)

# 5. Join A with B and B with A
A_update_B = A.copy()
A_update_B.update(B)
B_update_A = B.copy()
B_update_A.update(A)
print("A updated with B:", A_update_B)
print("B updated with A:", B_update_A)

# 6. Symmetric difference between A and B
sym_diff = A.symmetric_difference(B)
print("Symmetric difference between A and B:", sym_diff)

# 7. Delete the sets completely
del A, B
print("Sets A and B have been deleted.")

# Sets Exercises: Level 3
# 1. Convert ages to a set and compare the length of the list and the set
age_set = set(age)
print("Length of age list:", len(age))
print("Length of age set:", len(age_set))
print("The set is smaller than the list" if len(age_set) < len(age) else "The list is smaller or equal.")

# 2. Explain the difference between string, list, tuple, and set
print("""Differences:
- String: An immutable sequence of characters. Example: 'Hello'.
- List: A mutable, ordered sequence of items. Example: [1, 2, 3].
- Tuple: An immutable, ordered sequence of items. Example: (1, 2, 3).
- Set: An unordered, mutable collection of unique items. Example: {1, 2, 3}.
""")

# 3. Count unique words in the sentence
sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))

# 🎉 CONGRATULATIONS ! 🎉
