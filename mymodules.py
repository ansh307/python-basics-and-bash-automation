import random
def vac_feedback(vac, effeciency):
    print(f"Vaccine: {vac}")
    print(f"Effeciency: {effeciency}")
    
    if effeciency > 50 and effeciency < 75:
        print("This vaccine is moderately effective.")
    elif effeciency >= 75 and effeciency <= 90:
        print("This vaccine is highly effective.")
    else:
        print("This vaccine is not effective.")
        
        
def time_activity(*arg, **kwargs):
    min = sum(arg) + random.randint(1, 60)
    choice = random.choice(list(kwargs.values()))
    print(f"Total time spent: {min} minutes on {choice}")

def order_food(min_order , *args):
    print(f"you have ordered items: \n- {min_order}")
    for item in args:
        print(f"- {item}")

