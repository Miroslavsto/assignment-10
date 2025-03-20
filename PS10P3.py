def compute_out_the_door_price(msrp, make, model, ev_code):
    discount_percent = 0.05  # Default discount
    
    if make.lower() == 'honda' and model.lower() == 'accord':
        discount_percent = 0.10
    elif make.lower() == 'toyota' and model.lower() == 'rav4':
        discount_percent = 0.15
    elif ev_code.lower() == 'y':
        discount_percent = 0.30
    
    discounted_price = msrp * (1 - discount_percent)
    total_price = discounted_price * 1.07  # Add 7% sales tax
    return total_price

total_msrp = 0
total_sales_price = 0

while True:
    repeat = input("Do you want to run the program? (Yes or No): ").strip().lower()
    if repeat != 'yes':
        break
    
    make = input("Enter the make of the car: ").strip()
    model = input("Enter the model of the car: ").strip()
    ev_code = input("Is it an electric vehicle? (Y or N): ").strip().lower()
    msrp = float(input("Enter the MSRP of the car: "))
    
    total_msrp += msrp
    out_the_door_price = compute_out_the_door_price(msrp, make, model, ev_code)
    total_sales_price += out_the_door_price
    
    print(f"Out the door price for the {make} {model}: ${out_the_door_price:.2f}\n")

print(f"Total MSRP of all cars: ${total_msrp:.2f}")
print(f"Total sales price of all cars: ${total_sales_price:.2f}")
print("Program ended.")