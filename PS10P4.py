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

def compute_ticket_price(miles):
    if miles >= 30:
        return 12
    elif 20 <= miles <= 29:
        return 10
    elif 10 <= miles <= 19:
        return 8
    else:
        return 5

total_msrp = 0
total_sales_price = 0
total_ticket_price = 0

while True:
    repeat = input("Do you want to run the program? (Yes or No): ").strip().lower()
    if repeat != 'yes':
        break
    
    choice = input("Choose a program: Car Sales (1) or Train Ticket (2): ").strip()
    
    if choice == '1':
        make = input("Enter the make of the car: ").strip()
        model = input("Enter the model of the car: ").strip()
        ev_code = input("Is it an electric vehicle? (Y or N): ").strip().lower()
        msrp = float(input("Enter the MSRP of the car: "))
        
        total_msrp += msrp
        out_the_door_price = compute_out_the_door_price(msrp, make, model, ev_code)
        total_sales_price += out_the_door_price
        
        print(f"Out the door price for the {make} {model}: ${out_the_door_price:.2f}\n")
    elif choice == '2':
        last_name = input("Enter your last name: ").strip()
        miles = int(input("Enter miles from downtown Chicago: "))
        ticket_price = compute_ticket_price(miles)
        total_ticket_price += ticket_price
        
        print(f"Ticket price for {last_name}: ${ticket_price:.2f}\n")

print(f"Total MSRP of all cars: ${total_msrp:.2f}")
print(f"Total sales price of all cars: ${total_sales_price:.2f}")
print(f"Total ticket price of all tickets: ${total_ticket_price:.2f}")
print("Program ended.")
