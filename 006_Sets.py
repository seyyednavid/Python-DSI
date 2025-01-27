

my_set = {1, 2, 3}

my_set = set([1, 2, 3])

# a set is a data structure in which no duplicated values are allowed to exist.

my_set = {1, 1, 2, 3}
print(my_set)  # {1, 2, 3} , automatically eliminates any duplicates.

# there is no index in set
my_set[0] # TypeError: 'set' object is not subscriptable

# Sets is much faster than lists, python searches a set means that the time taken to find an element, no matter 
# how many elements are in the set, does not really change that much, whereas with a list the whole list needs to be searched.


# the most common use of a set to find the unique values from within a list.

my_list = {1, 2, 1, 3, 1, 4, 5, 6}
unique_values = set(my_list)
print(unique_values)


len(my_set)

my_set.add(4)
print(my_set)

my_set.update({5, 6, 7})
print(my_set) #{1, 2, 3, 4, 5, 6, 7}

my_set.discard(7)
print(my_set) # {1, 2, 3, 4, 5, 6}

my_set.discard(9) # works fine, even though it does not exist in our set
my_set.remove(9)  # KeyError: 9


set1 = {1,2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

set1.difference(set2) # {1, 2}
set2.difference(set1) # {6, 7}

print(set1) # {1, 2, 3, 4, 5}
set1.difference_update(set2)
print(set1) # {1, 2}


set1 = {1,2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

set1.intersection(set2) # shared values {3, 4, 5}


set1.intersection_update(set2)
print(set1) # {3, 4, 5}



























