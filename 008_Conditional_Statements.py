
# Decision-making logic =>  if , elif, else

"""
What to do today?

If it os sunny...
    I'll go for a run
    
"""
weather =  "Sunny"

if weather == "Sunny":
    print(" I'll go for a run")


weather =  "Cloudy"

if weather == "Sunny":
    print(" I'll go for a run")
    
    
weather =  "Cloudy"

if weather == "Sunny":
    print(" I'll go for a run")  
else:
    print("Let's just stay in bed...")
    
    


weather =  "Cloudy"

if weather == "Sunny":
    print(" I'll go for a run")  
    
elif weather == "Cloudy":
    print("Lets go to the gym!")
    
else:
    print("Let's just stay in bed...")




weather =  "Sunny"
temp = 12

if weather == "Sunny" and temp > 15:
    print(" I'll go for a run")  
else:
    print("Let's just stay in bed...")
    



weather =  "Sunny"
temp = 12

if weather == "Sunny" or temp > 15:
    print(" I'll go for a run")  
else:
    print("Let's just stay in bed...")
    
    
    
sunny = False

if sunny:
    print("let's go for a run")
else:
    print("Let's just stay in bed...")


i = 4

if i % 2 == 0:
    print(f"{i} is an even number")   
else:
    print(f"{i} is an odd number")















