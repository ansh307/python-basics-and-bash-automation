import random

VACCINES = ["Pfizer", "Moderna", "AstraZeneca", "Johnson & Johnson"]

random.shuffle(VACCINES)

LUCKY = random.choice(VACCINES)

for vaccine in VACCINES:
    print("")
    print(f"Vaccine: {vaccine}")
    
    if vaccine == LUCKY:
        print("Lucky vaccine found!")
        continue  # Skip the rest of the loop for this iteration
    
    print("This is not the lucky vaccine.")
    