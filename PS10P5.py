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

def compute_assessed_value(county, market_value):
    assessed_value_percent = {
        'cook': 0.90,
        'dupage': 0.80,
        'mchenry': 0.75,
        'kane': 0.60
    }.get(county.lower(), 0.70)
    
    retu