

# While loop - some times we wanna create a loop which isn't limited by a pre-existing data collection such as list or tuple


"""
while some condition is true:
    do something
    test if the condition is still true
"""

i = 1

while i <= 5:
    print(i)
    i += 1



i = 1

while i <= 5:
    print(i)
    if i ==3:
        break
    i += 1
   
    
   
i = 0

while i <= 4:
   i += 1
   if i == 3:
      continue
   print(i)
   