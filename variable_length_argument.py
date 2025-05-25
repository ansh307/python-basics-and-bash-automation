# non keyword variable length argument
def order_food(min_order , *args):
    print(f"you have ordered items: \n- {min_order}")
    for item in args:
        print(f"- {item}")

order_food("salad", "burger", "fries", "soda")