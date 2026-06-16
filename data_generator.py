# =============================================
# Digital Aajeevika Bot - Data Generator
# =============================================

import random
from config import RANDOM_CONFIG, NET_INCOME_MIN, NET_INCOME_MAX, EXPENDITURE_FIELDS

def get_random_area():
    """Area Under Crop - 2 ya 3"""
    return random.choice(RANDOM_CONFIG["area_under_crop"])

def get_random_production():
    """Total Production - 20 ya 25"""
    return random.choice(RANDOM_CONFIG["total_production"])

def get_random_price():
    """Average Market Price - 2400 ya 2500"""
    return random.choice(RANDOM_CONFIG["avg_market_price"])

def calculate_gross_income(production, price):
    """Gross Income = Total Production x Avg Market Price"""
    return production * price

def generate_expenditure(gross_income):
    """
    Expenditure random generate karo
    Net Income = Gross Income - Total Expenditure
    Net Income 40000 - 45000 ke beech honi chahiye
    """
    # Target net income randomly choose karo
    target_net = random.randint(NET_INCOME_MIN, NET_INCOME_MAX)

    # Total expenditure = Gross - Target Net
    total_expenditure = gross_income - target_net

    if total_expenditure <= 0:
        # Agar gross income kam hai toh minimum expenditure
        total_expenditure = 1000
        target_net = gross_income - total_expenditure

    # 7 fields mein distribute karo randomly
    num_fields = len(EXPENDITURE_FIELDS)
    
    # Random split karo total expenditure ko
    splits = sorted(random.sample(range(1, total_expenditure), num_fields - 1))
    splits = [0] + splits + [total_expenditure]
    values = [splits[i+1] - splits[i] for i in range(num_fields)]

    # Field name ke saath pair karo
    expenditure_data = {}
    for i, field in enumerate(EXPENDITURE_FIELDS):
        expenditure_data[field] = values[i]

    return expenditure_data, total_expenditure, target_net

def generate_form_data():
    """
    Ek member ke liye poora form data generate karo
    """
    area = get_random_area()
    production = get_random_production()
    price = get_random_price()
    gross_income = calculate_gross_income(production, price)
    expenditure, total_exp, net_income = generate_expenditure(gross_income)

    data = {
        "area_under_crop": str(area),
        "total_production": str(production),
        "avg_market_price": str(price),
        "gross_income": gross_income,
        "expenditure": expenditure,
        "total_expenditure": total_exp,
        "net_income": net_income
    }

    return data

def print_form_data(data):
    """Data print karo - debug ke liye"""
    print("\n===== Generated Form Data =====")
    print(f"Area Under Crop   : {data['area_under_crop']} Bigah")
    print(f"Total Production  : {data['total_production']} Quintal")
    print(f"Avg Market Price  : ₹{data['avg_market_price']}")
    print(f"Gross Income      : ₹{data['gross_income']}")
    print(f"\n--- Expenditure ---")
    for field, value in data['expenditure'].items():
        print(f"  {field}: ₹{value}")
    print(f"\nTotal Expenditure : ₹{data['total_expenditure']}")
    print(f"Net Income        : ₹{data['net_income']}")
    print("================================\n")

# Test karne ke liye
if __name__ == "__main__":
    for i in range(3):
        print(f"\n--- Test Member {i+1} ---")
        data = generate_form_data()
        print_form_data(data)
      
