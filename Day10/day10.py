# Level 3 Exercises

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("is_prime(7):", is_prime(7))  # Output: True
print("is_prime(10):", is_prime(10))  # Output: False

# 2. Write a function which checks if all items are unique in the list.
def all_unique(lst):
    return len(lst) == len(set(lst))

print("all_unique([1, 2, 3, 4]):", all_unique([1, 2, 3, 4]))  # Output: True
print("all_unique([1, 2, 2, 4]):", all_unique([1, 2, 2, 4]))  # Output: False

# 3. Write a function which checks if all the items of the list are of the same data type.
def same_data_type(lst):
    return len(set(map(type, lst))) == 1

print("same_data_type([1, 2, 3, 4]):", same_data_type([1, 2, 3, 4]))  # Output: True
print("same_data_type([1, '2', 3]):", same_data_type([1, '2', 3]))  # Output: False

# 4. Write a function which checks if provided variable is a valid Python variable
import keyword

def is_valid_variable(name):
    if name.isidentifier() and not keyword.iskeyword(name):
        return True
    return False

print("is_valid_variable('my_var'):", is_valid_variable('my_var'))  # Output: True
print("is_valid_variable('1var'):", is_valid_variable('1var'))  # Output: False

# 5. Create a function called the most_spoken_languages_in_the_world
# You can use a dictionary of the languages with their number of speakers (sample data)
languages = {
    'Mandarin': 1100, 'Spanish': 460, 'English': 380, 'Hindi': 340, 'Arabic': 310,
    'Bengali': 230, 'Portuguese': 220, 'Russian': 155, 'Japanese': 125, 'Lahnda': 105
}

def most_spoken_languages(languages, top=10):
    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:top]

print("Most spoken languages:", most_spoken_languages(languages))

# 6. Create a function called the most_populated_countries
# Using a sample dictionary of country population data
countries_population = {
    'China': 1393409038, 'India': 1366417754, 'USA': 331002651, 'Indonesia': 273523615,
    'Pakistan': 220892340, 'Brazil': 212559417, 'Nigeria': 206139589, 'Bangladesh': 164689383,
    'Russia': 145934462, 'Mexico': 128933395
}

def most_populated_countries(countries_population, top=10):
    sorted_countries = sorted(countries_population.items(), key=lambda x: x[1], reverse=True)
    return sorted_countries[:top]

print("Most populated countries:", most_populated_countries(countries_population))
