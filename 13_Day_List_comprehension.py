#1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positiveNum = [i for i in numbers if i > 0]
##print(positiveNum)

#2. Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list = [k for j in [i for j in list_of_lists for i in j]for k in j]
##print(flat_list)

#3. Using list comprehension create the following list of tuples:
"""
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
"""

result = [(i, *(i**j for j in range(6))) for i in range(11)]
#since the first segment where we have range results in a constructor, we had to *(
print(f'Resulting list is:\n {result}')

#4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country.upper(), country[:3].upper(), city.upper()] for innerList in countries for country, city in innerList]
##print(output)

#5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [{'country': country.upper(), 'city': city.upper()} for innerList in countries for country, city in innerList]
##print(output)

#6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [name + " " + surname for innerL in names for name, surname in innerL]
##print(output)