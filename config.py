# =============================================
# Digital Aajeevika Bot - Configuration File
# =============================================

# App Package Name
APP_PACKAGE = "com.aajeevika.digital"  # Confirm karna hoga

# Login Credentials (agar chahiye toh)
LOGIN = {
    "username": "",
    "password": ""
}

# Form Fixed Values
FORM_CONFIG = {
    "season": "Rabi",
    "crop_name": "Wheat",
    "area_unit": "Bigah",
    "production_unit": "Quintal",
    "use_msp": "No",

    # Livelihood Support
    "support_category": "Loan",
    "fund_source": "Self Help Group (SHG)",
    "fund_type": "Convergence Funds",
    "amount": "5000",
    "own_contribution": "500",

    # Assets
    "asset_category": "Crops Based (Agriculture/Horticulture)",
    "asset_activity": "Wheat",
    "asset_type": "Equipment",
    "asset_name": "Bee Boxes",
    "asset_status": "Owned",
    "procurement_source": "Department of Agriculture",
    "estimated_cost": "2000",

    # Training
    "training_category": "Crops Based (Agriculture/Horticulture)",
    "training_activity": "Wheat",
    "training_name": "Development of non chemical pesticides",
    "training_source": "Department of Agriculture",
    "training_duration": "2"
}

# Random Value Options
RANDOM_CONFIG = {
    "area_under_crop": [2, 3],
    "total_production": [20, 25],
    "avg_market_price": [2400, 2500],
}

# Target Net Income Range
NET_INCOME_MIN = 40000
NET_INCOME_MAX = 45000

# Expenditure Fields (inhe randomly adjust karenge)
EXPENDITURE_FIELDS = [
    "Seeds And Other Inputs",
    "Field Preparation & Interculture Operation Cost",
    "Fertilizer & Nutrient Management Cost",
    "Insect Pest Management Cost",
    "Irrigation Cost",
    "Labour Cost",
    "Other Cost"
]

# Wait Times (seconds)
WAIT_SHORT = 1
WAIT_MEDIUM = 2
WAIT_LONG = 3
