

my_list = [1, 3.6, "Four"]

my_tuple = (1, 3.6, "Four")


x = tuple(my_list)

x = list(x)

# tuple is immutable but list is mutable - Once a tuple is created, its size and elements cannot be changed.
# we use it for proficiency in speed processing,as python knows tuple is immutable , it can store it in a single block of memory 
# rather than multiple block of memory, which is the case for lists.

my_tuple.append(4)   # AttributeError: 'tuple' object has no attribute 'append
my_tuple.sort()      # AttributeError: 'tuple' object has no attribute 'sort'


 
len(my_tuple)

my_tuple[0]

my_tuple[-1]

my_tuple[1:3]

my_tuple.index(3.6)

3.6 in my_tuple

