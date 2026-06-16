# =============================================
# Digital Aajeevika Bot - Main File
# =============================================

import uiautomator2 as u2
import time
from config import APP_PACKAGE, WAIT_SHORT, WAIT_MEDIUM, WAIT_LONG
from data_generator import generate_form_data, print_form_data
from app_controller import (
    d,
    tap_text,
    tap_contains,
    scroll_and_tap,
    fill_livelihood_activities,
    fill_livelihood_support,
    fill_assets,
    fill_training
)

# =============================================
# Member dhundho aur process karo
# =============================================

def open_app():
    """App open karo"""
    print(">> App open kar raha hoon...")
    d.app_start(APP_PACKAGE)
    time.sleep(WAIT_LONG)
    print(">> App open ho gaya!")

def go_to_members():
    """Members tab pe jao"""
    print(">> Members tab pe ja raha hoon...")
    tap_text("Members")
    time.sleep(WAIT_MEDIUM)

def get_partially_completed_members():
    """Partially completed members ki list lo"""
    members = d(textContains="Partially completed")
    count = members.count
    print(f">> {count} Partially completed members mile!")
    return count

def process_one_member():
    """
    Ek 'Partially completed' member ko process karo
    - 3 dots tap karo
    - Livelihood Activities karo
    - Livelihood Support karo
    - Assets karo
    - Training karo
    """
    try:
        # Pehla "Partially completed" member dhundho
        member_card = d(textContains="Partially completed")[0]
        
        # Member name print karo
        try:
            member_name = member_card.sibling(
                className="android.widget.TextView"
            ).get_text()
            print(f"\n{'='*40}")
            print(f">> Member: {member_name}")
            print(f"{'='*40}")
        except:
            print("\n>> Naya member process ho raha hai...")

        # 3 dots (menu) tap karo
        d(description="More options")[0].click()
        time.sleep(WAIT_SHORT)

        # ---- STEP 1: Livelihood Activities ----
        tap_text("Livelihood Activities")
        time.sleep(WAIT_MEDIUM)

        # Form data generate karo
        data = generate_form_data()
        print_form_data(data)

        # Form fill karo
        fill_livelihood_activities(data)
        time.sleep(WAIT_MEDIUM)

        # Back button
        d.press("back")
        time.sleep(WAIT_MEDIUM)

        # Close button
        tap_text("Close")
        time.sleep(WAIT_MEDIUM)

        # ---- STEP 2: Livelihood Support ----
        # 3 dots phir tap karo
        d(description="More options")[0].click()
        time.sleep(WAIT_SHORT)

        tap_text("Livelihood Support")
        time.sleep(WAIT_MEDIUM)

        fill_livelihood_support()
        time.sleep(WAIT_MEDIUM)

        # ---- STEP 3: Assets ----
        fill_assets()
        time.sleep(WAIT_MEDIUM)

        # ---- STEP 4: Training & Skills ----
        fill_training()
        time.sleep(WAIT_LONG)

        print(">> Yeh member complete ho gaya! ✓")
        return True

    except Exception as e:
        print(f"!! Error aaya: {e}")
        return False

def run_bot(max_members=None):
    """
    Bot chalao
    max_members = kitne members process karne hain
    None = sab kar do
    """
    print("\n" + "="*40)
    print("  DIGITAL AAJEEVIKA BOT SHURU")
    print("="*40)

    # App open karo
    open_app()

    # Members tab pe jao
    go_to_members()

    # Kitne members hain
    total = get_partially_completed_members()
    
    if total == 0:
        print(">> Koi Partially completed member nahi mila!")
        return

    # Max members set karo
    if max_members is None:
        max_members = total

    print(f">> Total {max_members} members process karenge\n")

    success = 0
    failed = 0

    for i in range(max_members):
        print(f"\n>> Member {i+1}/{max_members} shuru...")
        
        result = process_one_member()
        
        if result:
            success += 1
        else:
            failed += 1
            print(f"!! Member {i+1} fail hua, agli member pe ja raha hoon...")

        # Thoda wait karo
        time.sleep(WAIT_MEDIUM)

    # Final report
    print("\n" + "="*40)
    print("  BOT COMPLETE!")
    print(f"  Successful : {success}")
    print(f"  Failed     : {failed}")
    print(f"  Total      : {max_members}")
    print("="*40)

# =============================================
# Run karo
# =============================================

if __name__ == "__main__":
    # Pehle sirf 1 member test karo
    # Sahi kaam kare toh max_members=None kar do (sab)
    run_bot(max_members=1)
      
