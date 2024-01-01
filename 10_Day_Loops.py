#1. Iterate 0 to 10 using for loop, do the same using while loop.
## for loop
"""for i in range(11):
    print(i)"""

## while loop
"""j = 0
while j < 11:
    print(j)
    j += 1"""

#2. Iterate 10 to 0 using for loop, do the same using while loop.
## for loop
"""for i in range(10, 0, -1):
    print(i)"""

## while loop
"""j = 10
while j >= 0:
    print(j)
    j -= 1"""

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######

"""for i in range(1, 8, 1):
    print('#'*i)"""

#4. Use nested loops to create the following:

# # # # # # # #
"""(...) x 7"""

"""for i in range(8):
    for j in range(8):
        print("# ", end="")
    print()"""

#5. Print the following pattern:

"""0 x 0 = 0
1 x 1 = 1
...
10 x 10 = 100"""

"""for i in range(11):
    for j in range(11):
        print(f"{j} x {j} = {j * j}")
    break"""

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

"""my_list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for word in my_list:
    print(word, end=",")"""

#7. Use for loop to iterate from 0 to 100 and print only even numbers
"""for i in range(101):
    if i % 2 == 0:
        print(i, end=", ")"""

#8. Use for loop to iterate from 0 to 100 and print only odd numbers
"""for j in range(101):
    if j % 2 != 0:
        print(j, end=", ")"""

#LEVEL 2
#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
"""total = 0
for i in range (101):
    total += i
print(f"The sum of all numbers to 100 is {total}.")"""

#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
"""total_even = 0
total_odd = 0
for i in range (101):
    if i % 2 == 0:
        total_even += i
    else:
        total_odd += i

print(f"The total sum of even numbers is {total_even} and the total sum of odd numbers is {total_odd}.")"""

#LEVEL 3
#1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
"""from countries import countries
for i in countries:
    if i.find("land") != -1:
        print(i)"""

#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
"""fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in fruits:
    reversed_fruits.insert(0, i)

print(reversed_fruits)"""

#3. Go to the data folder and use the countries_data.py file.
#i. What are the total number of languages in the data
#{'name': 'Zimbabwe', 'capital': 'Harare', 'languages': ['English', 'Shona', 'Northern Ndebele'],
# 'population': 14240168, 'flag': 'https://restcountries.eu/data/zwe.svg', 'currency': 'Botswana pula'}
from countries_data import countries
"""all_languages = []
for country in countries:
    all_languages.extend(country.get("languages", []))
unique_languages = len(set(all_languages))
print(f"There are {unique_languages} unique languages.")"""

#ii. Find the ten most spoken languages from the data
language_population = {}
for country in countries:
    languages = country.get("languages", []) #using get() to retrieve the value of languages key from country list
    population = country.get("population", 0) #using get() to retrieve the value of population key from country list
    print(languages)
    print(population)

#iii. Find the 10 most populated countries in the world