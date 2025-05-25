'''
VACCINES = ["Pfizer", "Moderna", "AstraZeneca", "Johnson & Johnson"]

for vaccine in VACCINES:
    print("")
    print("Vaccine is :", )
    for i in vaccine:
        print(f"Character: {i}")
        
print("End of for loop")

'''

import time

x= 0
while True:
    print(f"x is {x}")
    x += 1
    time.sleep(2) 
    if x >= 5:
        break
print("End of while loop")
    
