# =============================================
# Digital Aajeevika Bot - App Controller
# =============================================

import uiautomator2 as u2
import time
from config import FORM_CONFIG, WAIT_SHORT, WAIT_MEDIUM, WAIT_LONG
from data_generator import generate_form_data, print_form_data

# Phone se connect karo
d = u2.connect()

def wait(seconds):
    time.sleep(seconds)

def tap_text(text, timeout=10):
    """Kisi bhi text pe tap karo"""
    d(text=text).click()
    wait(WAIT_SHORT)

def tap_contains(text, timeout=10):
    """Partial text se tap karo"""
    d(textContains=text).click()
    wait(WAIT_SHORT)

def scroll_and_tap(text):
    """Scroll karke text dhundho aur tap karo"""
    d(scrollable=True).scroll.to(text=text)
    d(text=text).click()
    wait(WAIT_SHORT)

def type_text(text_to_find, value):
    """Field dhundh ke value type karo"""
    d(text=text_to_find).set_text(str(value))
    wait(WAIT_SHORT)

def tap_index(text, index=0):
    """Same text ke multiple elements mein se index wala tap karo"""
    d(text=text)[index].click()
    wait(WAIT_SHORT)

# =============================================
# STEP 1: Livelihood Activities
# =============================================

def fill_livelihood_activities(data):
    """Crops Based form fill karo"""
    print(">> Livelihood Activities shuru...")

    # Crops Based pe tap
    tap_contains("Crops Based")
    wait(WAIT_MEDIUM)

    # Add Season button
    tap_text("Add Season")
    wait(WAIT_MEDIUM)

    # Season = Rabi
    tap_text("Please select Season")
    wait(WAIT_SHORT)
    tap_text(FORM_CONFIG["season"])

    # Crop Name = Wheat
    tap_text("Please select Crop Name")
    wait(WAIT_SHORT)
    scroll_and_tap(FORM_CONFIG["crop_name"])

    # Area Unit = Bigah
    tap_text("Please select Area Unit")
    wait(WAIT_SHORT)
    tap_text(FORM_CONFIG["area_unit"])

    # Area Under Crop
    d(resourceId="area_under_crop").set_text(data["area_under_crop"])
    wait(WAIT_SHORT)

    # Production Unit = Quintal
    tap_text("Please select Production Unit")
    wait(WAIT_SHORT)
    tap_text(FORM_CONFIG["production_unit"])

    # Total Production
    d(resourceId="total_production").set_text(data["total_production"])
    wait(WAIT_SHORT)

    # Use MSP = No
    tap_text("Please select")
    wait(WAIT_SHORT)
    tap_text(FORM_CONFIG["use_msp"])

    # Avg Market Price
    d(resourceId="avg_market_price").set_text(data["avg_market_price"])
    wait(WAIT_SHORT)

    # Expenditure fields fill karo
    fill_expenditure(data["expenditure"])

    # Save
    tap_text("Save")
    wait(WAIT_LONG)
    print(">> Livelihood Activities done!")

def fill_expenditure(expenditure):
    """Expenditure section fill karo"""
    print(">> Expenditure fill kar raha hoon...")
    field_map = {
        "Seeds And Other Inputs": "seeds_input",
        "Field Preparation & Interculture Operation Cost": "field_prep",
        "Fertilizer & Nutrient Management Cost": "fertilizer",
        "Insect Pest Management Cost": "pest_mgmt",
        "Irrigation Cost": "irrigation",
        "Labour Cost": "labour",
        "Other Cost": "other_cost"
    }
    for field_name, value in expenditure.items():
        try:
            d(textContains=field_name).sibling(
                className="android.widget.EditText"
            ).set_text(str(value))
            wait(WAIT_SHORT)
        except:
            print(f"  Warning: {field_name} field nahi mila")

# =============================================
# STEP 2: Livelihood Support
# =============================================

def fill_livelihood_support():
    """Livelihood Support form fill karo"""
    print(">> Livelihood Support shuru...")

    # + button tap
    d(description="Add").click()
    wait(WAIT_MEDIUM)

    # Category
    tap_text("Please select Livelihood Category")
    wait(WAIT_SHORT)
    tap_contains("Crop Based Agriculture")

    # Activity = Wheat
    tap_text("Please select Livelihood Activity")
    wait(WAIT_SHORT)
    tap_text(FORM_CONFIG["crop_name"])

    # Support Category = Loan
    tap_text("Please select Livelihood Support Category")
    wait(WAIT_SHORT)
    tap_text(FORM_CONFIG["support_category"])

    # Fund Source = SHG
    tap_text("Please select")
    wait(WAIT_SHORT)
    tap_contains("Self Help Group")

    # Type of Fund = Convergence Funds
    tap_text("Please select Type Of Fund")
    wait(WAIT_SHORT)
    tap_text(FORM_CONFIG["fund_type"])

    # Amount
    d(textContains="Amount").sibling(
        className="android.widget.EditText"
    ).set_text(FORM_CONFIG["amount"])
    wait(WAIT_SHORT)

    # Own Contribution
    d(textContains="Own Contribution").sibling(
        className="android.widget.EditText"
    ).set_text(FORM_CONFIG["own_contribution"])
    wait(WAIT_SHORT)

    # Save
    tap_text("Save")
    wait(WAIT_LONG)

    # Next
    tap_text("Next")
    wait(WAIT_MEDIUM)
    print(">> Livelihood Support done!")

# =============================================
# STEP 3: Assets
# =============================================

def fill_assets():
    """Assets form fill karo"""
    print(">> Assets shuru...")

    # + button
    d(description="Add").click()
    wait(WAIT_MEDIUM)

    # Livelihood Category
    tap_text("Please select Livelihood Category")
    wait(WAIT_SHORT)
    tap_contains("Crops Based")

    # Activity
    tap_text("Please select Livelihood Activity")
    wait(WAIT_SHORT)
    tap_text(FORM_CONFIG["asset_activity"])

    # Asset Type
    tap_text("Please select Asset Type")
    wait(WAIT_SHORT)
    tap_text(FORM_CONFIG["asset_type"])

    # Asset Name
    tap_text("Please select Asset Name")
    wait(WAIT_SHORT)
    tap_text(FORM_CONFIG["asset_name"])

    # Asset Status
    tap_text("Please select Asset Status")
    wait(WAIT_SHORT)
    tap_text(FORM_CONFIG["asset_status"])

    # Procurement Source
    tap_text("Please select Procurement Source")
    wait(WAIT_SHORT)
    tap_text(FORM_CONFIG["procurement_source"])

    # Estimated Cost
    d(textContains="Estimated Cost").sibling(
        className="android.widget.EditText"
    ).set_text(FORM_CONFIG["estimated_cost"])
    wait(WAIT_SHORT)

    # Save
    tap_text("Save")
    wait(WAIT_LONG)

    # Next
    tap_text("Next")
    wait(WAIT_MEDIUM)
    print(">> Assets done!")

# =============================================
# STEP 4: Training & Skills
# =============================================

def fill_training():
    """Training & Skills form fill karo"""
    print(">> Training & Skills shuru...")

    # + button
    d(description="Add").click()
    wait(WAIT_MEDIUM)

    # Category
    tap_text("Please select Livelihood Category")
    wait(WAIT_SHORT)
    tap_contains("Crops Based")

    # Activity
    tap_text("Please select Livelihood Activity")
    wait(WAIT_SHORT)
    tap_text(FORM_CONFIG["training_activity"])

    # Training Name
    tap_text("Please select Training Name")
    wait(WAIT_SHORT)
    tap_contains("Development of non chemical")

    # Training Source
    tap_text("Please select Training Source")
    wait(WAIT_SHORT)
    tap_text(FORM_CONFIG["training_source"])

    # Duration
    d(textContains="Duration").sibling(
        className="android.widget.EditText"
    ).set_text(FORM_CONFIG["training_duration"])
    wait(WAIT_SHORT)

    # Save
    tap_text("Save")
    wait(WAIT_LONG)

    # Send For Approval
    tap_text("Send For Approval")
    wait(WAIT_LONG)
    print(">> Training done! Send For Approval clicked!")
  
