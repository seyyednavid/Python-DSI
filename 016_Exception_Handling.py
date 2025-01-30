

age = int(input("Enter your age: "))



try:
    age = int(input("Enter your age: "))
    print(age)
except:
    print("Not a valid input, please try again")
    
    

print(some_object) # NameError

my_list = [1, 2]
my_list[4]        # IndexError

"a" + 5           # TypeError

int("python")     # ValueError

3/0               # ZeroDivisionError



try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("Not a valid input, please try again")



try:
    age = int(input("Enter your age: "))
    print(age)
except NameError:
    print("Not a valid input, please try again") # ValueError: invalid literal for int() with base 10: '44r'

    
    
    
try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError as error_type:
    print(f"Not a valid input {error_type}, please try again")   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    