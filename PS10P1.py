def compute_forecast(month, sales):
    forecast_percent = {
        'Jan': 0.10, 'Feb': 0.10, 'Mar': 0.10,
        'Apr': 0.15, 'May': 0.15, 'Jun': 0.15,
        'Jul': 0.20, 'Aug': 0.20, 'Sep': 0.20,
        'Oct': 0.25, 'Nov': 0.25, 'Dec': 0.25
    }
    next_month_sales = sales * (1 + forecast_percent.get(month, 0))
    return next_month_sales

while True:
    repeat = input("Do you want to run the program? (Yes or No): ").strip().lower()
    if repeat != 'yes':
        break
    
    last_name = input("Enter your last name: ").strip()
    month = input("Enter the month: ").strip().title()
    sales = float(input("Enter sales: "))
    
    next_month_sales = compute_forecast(month, sales)
    print(f"Next month's sales forecast for {last_name} in {month} is: ${next_month_sales:.2f}\n")

print("Program ended.")
