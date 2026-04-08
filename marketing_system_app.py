# DUMMY DATA
# Initial dataset as benchmark campaign database simulation
benchmarks = [
    {"Date": "2020-01-25", "Category": "Chinese New Year", "Platform": "Facebook", "Best CPR": 12000, "Notes": "High season sales spike"},
    {"Date": "2021-02-12", "Category": "Chinese New Year", "Platform": "Instagram", "Best CPR": 13500, "Notes": "Engagement strong"},
    {"Date": "2022-02-01", "Category": "Chinese New Year", "Platform": "TikTok", "Best CPR": 12500, "Notes": "Video ads worked well"},
    {"Date": "2021-02-14", "Category": "Valentine", "Platform": "Instagram", "Best CPR": 17000, "Notes": "Gift trend increased"},
    {"Date": "2021-02-14", "Category": "Valentine", "Platform": "Facebook", "Best CPR": 15500, "Notes": "Better reach than IG"},
    {"Date": "2022-02-14", "Category": "Valentine", "Platform": "TikTok", "Best CPR": 14800, "Notes": "Short video promo effective"},
    {"Date": "2022-04-03", "Category": "Ramadan", "Platform": "TikTok", "Best CPR": 13000, "Notes": "Video content performed well"},
    {"Date": "2023-03-23", "Category": "Ramadan", "Platform": "Facebook", "Best CPR": 14500, "Notes": "Conversion focused"},
    {"Date": "2024-03-12", "Category": "Ramadan", "Platform": "Google", "Best CPR": 15000, "Notes": "High intent search traffic"},
    {"Date": "2024-05-05", "Category": "Company Anniversary", "Platform": "Facebook", "Best CPR": 14000, "Notes": "Big discount campaign"},
    {"Date": "2024-05-05", "Category": "Company Anniversary", "Platform": "Instagram", "Best CPR": 13800, "Notes": "Stories ads effective"},
    {"Date": "2024-05-05", "Category": "Company Anniversary", "Platform": "Google", "Best CPR": 16500, "Notes": "Search cost higher"},
    {"Date": "2020-09-09", "Category": "Marketplace Sale", "Platform": "Shopee Ads", "Best CPR": 9500, "Notes": "9.9 strong marketplace push"},
    {"Date": "2022-11-11", "Category": "Marketplace Sale", "Platform": "Shopee Ads", "Best CPR": 9000, "Notes": "11.11 lowest CPR recorded"},
    {"Date": "2021-12-12", "Category": "Marketplace Sale", "Platform": "TikTok", "Best CPR": 11000, "Notes": "12.12 flash sale traffic spike"},
    {"Date": "2024-03-03", "Category": "Marketplace Sale", "Platform": "Tokopedia Ads", "Best CPR": 10000, "Notes": "3.3 cost efficient campaign"},
    {"Date": "2023-01-01", "Category": "New Year", "Platform": "Google", "Best CPR": 21000, "Notes": "Awareness heavy"},
    {"Date": "2024-01-01", "Category": "New Year", "Platform": "Google", "Best CPR": 20000, "Notes": "Slightly improved CPR"},
    {"Date": "2023-06-06", "Category": "Mid Year Sale", "Platform": "Facebook", "Best CPR": 13500, "Notes": "Stable performance"},
    {"Date": "2022-10-31", "Category": "Halloween", "Platform": "Instagram", "Best CPR": 16000, "Notes": "Seasonal promo"},
]

# LIBRARY
# Import dependencies used in the program
from collections import defaultdict
from tabulate import tabulate
from datetime import datetime
import pandas as pd

# ID GENERATOR
# Generator function for unique campaign IDs
def generate_pk(data):
    # Short code mapping for platforms
    platform_code = {
        "facebook": "FB",
        "instagram": "IG",
        "tiktok": "TT",
        "google": "GG",
        "shopee ads": "SP",
        "tokopedia ads": "TP",
        "youtube": "YT"
    }

    counter = defaultdict(int)  # Counter to maintain ID uniqueness

    # Generate IDs for initial data
    for row in data:
        tanggal = row["Date"].replace("-", "")[2:]
        platform = platform_code.get(row["Platform"].lower(), "XX")
        code = f"{platform}{tanggal}"
        counter[code] += 1
        row["ID"] = f"{code}{counter[code]:04d}"

    # Function to generate ID when adding new data
    def generate(platform, tanggal):
        tanggal_format = tanggal.replace("-", "")[2:]
        platform_code_value = platform_code.get(platform.lower(), "XX")
        code = f"{platform_code_value}{tanggal_format}"
        counter[code] += 1
        return f"{code}{counter[code]:04d}"

    return generate

# Initialize ID generator
generate_id = generate_pk(benchmarks)

# LOGIN & PROGRAM STATE
# Global program status variables and user data
program_running = True
users = [
    {"username": "admin", "password": "admin123", "role": "admin"},
    {"username": "staff", "password": "staff123", "role": "staff"}
]

# Login authentication function
def login():
    print("\n==== Welcome to PWD Marketing System ====\n")

    username_input = input("Username: ").strip()
    password_input = input("Password: ").strip()

    for user in users:
        if user["username"] == username_input and user["password"] == password_input:
            print("\nLogin successful!")
            return user["role"]

    print("\nIncorrect username or password!")
    return None

# MATCH CHECKER
# Find benchmark by category & platform
def checker(category, platform):
    for b in benchmarks:
        if b["Category"].lower() == category.lower() and b["Platform"].lower() == platform.lower():
            return b
    return None

# Find benchmark by ID
def checker_by_id(primary_id):
    for b in benchmarks:
        if b["ID"].lower() == primary_id.lower():
            return b
    return None

# CONFIRMATION
# Confirmation when input is invalid
def warning_continue():
    while True:
        print("\nInvalid input!")
        warning = input("Do you want to continue the program? (Y/N): ").strip().lower()
        if warning == "y":
            return True
        elif warning == "n":
            dashboard()
            return False
        else:
            print("Input must be Y or N.")

# Confirmation before saving changes
def confirm_save():
    while True:
        save = input("Save data changes? (Y/N): ").strip().lower()
        if save == "y":
            return True
        elif save == "n":
            dashboard()
            return False
        else:
            print("Input must be Y or N.")

# TABLE DATA
# Display benchmark table
def table_benchmark(data=None):
    if data is None:
        data = benchmarks

    if not data:
        print("\nNo data available yet.")
        return

    # List Comprehension
    tabel = [[
        b["ID"],
        b["Date"],
        b["Category"],
        b["Platform"],
        f"{int(b['Best CPR']):,}",
        b["Notes"]
    ] for b in data]

    print("\n==== Benchmark Data List ====")
    print(tabulate(tabel,
        headers=["ID", "Date", "Category", "Platform", "Best CPR", "Notes"],
        tablefmt="rounded_outline")
    )

# Display unique category & platform combinations
def table_category_platform(data=None):
    if data is None:
        data = benchmarks

    seen = set()
    tabel = []

    for b in data:
        key = (b["Category"].lower(), b["Platform"].lower())
        if key not in seen:
            seen.add(key)
            tabel.append([b["Category"], b["Platform"]])

    if not tabel:
        print("\nNo data available yet.")
        return

    # Add row numbers at the front
    tabel = [[i+1, *row] for i, row in enumerate(tabel)]

    print("\n==== Category & Platform List ====")
    print(tabulate(tabel,
        headers=["No", "Category", "Platform"],
        tablefmt="rounded_outline")
    )

# MAIN MENU
# Display dashboard based on role
def dashboard(role):
    print("\n--- Performance Marketing System ---\n")
    print("1. View Benchmark Campaign Data")

    if role == "admin":
        print("2. Add Benchmark Campaign Data")
        print("3. Update Benchmark Campaign Data")
        print("4. Delete Benchmark Campaign Data")
        print("5. Evaluate Campaign Performance")
        print("6. Logout")
    else:
        print("2. Evaluate Campaign Performance")
        print("3. Logout")

# CREATE
# Add new benchmark
def add_benchmark():
    while True:
        print("\n--- Add Data Menu ---")
        print("1. Add Data")
        print("2. Back")
        choice = input("\nChoose: ").strip()

        if choice == "1":
            table_benchmark()
            print("\nPlease fill in the following data! (type 'K' to cancel)")

            # Date validation
            while True:
                date = input("\nCampaign start date (YYYY-MM-DD): ").strip()

                if date.lower() == "k":
                    break
                try:
                    datetime.strptime(date, "%Y-%m-%d")
                    break
                except:
                    if not warning_continue():
                        continue

            # Category input
            while True:
                cat = input("Campaign category: ").strip()

                if cat.lower() == "k":
                    break
                if cat.isdigit():
                    print("Input cannot be a number")
                    continue
                break

            # Platform validation
            allowed_platform = ["facebook","instagram","tiktok","google","shopee ads","tokopedia ads","youtube"]
            while True:
                plat = input("Ad platform: ").strip()

                if plat.lower() == "k":
                    break

                if plat.lower() not in allowed_platform:
                    print("\nPlatform not available.")
                    if not warning_continue():
                        continue
                    else:
                        continue

                break

            # CPR validation
            while True:
                cpr_input = input("Cost per result (Rp): ").strip()

                if cpr_input.lower() == "k":
                    break

                try:
                    cpr = float(cpr_input)

                    if cpr == 0:
                        print("\nInput cannot be 0")
                        continue

                    if cpr < 1000:
                        print("\nInput cannot be less than Rp 1,000")
                        continue

                    break

                except ValueError:
                    print("\nEnter a valid number or 'k' to cancel.")
                    if not warning_continue():
                        continue

            # Notes input
            while True:
                notes = input("Notes: ").strip()

                if notes.lower() == "k":
                    break
                if notes.isdigit():
                    print("Input cannot be a number")
                    continue
                break

            # Duplicate check
            if checker(cat, plat):
                print("\nBenchmark already exists for this category & platform.")
                continue

            # Save data
            if confirm_save():
                benchmarks.append({
                    "Date": date,
                    "Category": cat,
                    "Platform": plat,
                    "Best CPR": cpr,
                    "Notes": notes,
                    "ID": generate_id(plat, date)
                })
                print(f"\nBenchmark {cat} successfully added.")

        elif choice == "2":
            break
        else:
            warning_continue()

# READ
# Display and filter data
def read_table():
    while True:
        print("\n--- Table Menu ---")
        print("1. Show All")
        print("2. Filter Data")
        print("3. Back")
        main_choice = input("\nChoose: ")

        if main_choice == "1":
            table_benchmark()
            print("\nNote: Information displayed is benchmark data.")

        elif main_choice == "2":
            while True:
                print("\n--- Filter By ---")
                print("1. Date")
                print("2. Category")
                print("3. Platform")
                print("4. Back")
                filter_choice = input("\nChoose: ")

                # Display data by date range
                if filter_choice == "1":
                    print("\n(type 'K' to cancel)\n")
                    while True:
                        df = pd.DataFrame(benchmarks)
                        df["Date"] = pd.to_datetime(df["Date"])

                        start_input = input("Enter Start Date (YYYY-MM-DD): ").strip()
                        if start_input.lower() == "k":
                            break

                        end_input = input("Enter End Date (YYYY-MM-DD): ").strip()
                        if end_input.lower() == "k":
                            break

                        try:
                            awalan = datetime.strptime(start_input, "%Y-%m-%d")
                            akhiran = datetime.strptime(end_input, "%Y-%m-%d")

                            filtered = df[df["Date"].between(awalan, akhiran)]

                            if not filtered.empty:
                                table_benchmark(filtered.to_dict("records"))
                            else:
                                print("\nData not found.")
                            break

                        except ValueError:
                            print("\nInvalid date format. Use YYYY-MM-DD.")
                            continue

                # Display data by category
                elif filter_choice == "2":
                    while True:
                        print("\n(type 'K' to cancel)\n")
                        cat = input("Category: ").strip().lower()

                        if cat == "k":
                            break

                        if cat.isdigit():
                            print("Input cannot be a number")
                            continue

                        results = [b for b in benchmarks if b["Category"].lower() == cat]

                        if results:
                            table_benchmark(results)
                        else:
                            print("\nData not found.")

                        break

                # Display data by platform
                elif filter_choice == "3":
                    while True:
                        print("\n(type 'K' to cancel)\n")
                        plat = input("Platform: ").strip().lower()

                        if plat == "k":
                            break

                        if plat.isdigit():
                            print("Input cannot be a number")
                            continue

                        results = [b for b in benchmarks if b["Platform"].lower() == plat]

                        if results:
                            table_benchmark(results)
                        else:
                            print("\nPlatform not available.")

                        break

                elif filter_choice == "4":
                    break
                else:
                    warning_continue()

        elif main_choice == "3":
            break
        else:
            warning_continue()

# UPDATE
# Update benchmark data
def update_benchmark():
    while True:
        print("\n--- Update Data Menu ---")
        print("1. Update Data")
        print("2. Back")
        choice = input("\nChoose: ").strip()

        if choice == "1":
            table_benchmark()
            print("\n(type 'K' to cancel)")

            kid = input("\nCampaign ID to update: ").strip()
            if kid.lower() == "k":
                continue

            b = checker_by_id(kid)
            if not b:
                print("\nBenchmark data not found!")
                continue

            print("\nLeave blank if you don't want to update a field!\n")

            # Update platform
            while True:
                plat_input = input(f"Platform ({b['Platform']}): ").strip()

                if plat_input.lower() == "k":
                    break

                if not plat_input:
                    plat = b["Platform"]
                    break

                if plat_input.isdigit():
                    print("Input cannot be a number")
                    continue

                allowed_platform = ["facebook","instagram","tiktok","google","shopee ads","tokopedia ads","youtube"]
                if plat_input.lower() not in allowed_platform:
                    print("\nPlatform not available.")
                    continue

                plat = plat_input
                break

            # Update CPR
            while True:
                cpr_input = input(f"Best CPR ({b['Best CPR']}): ").strip()

                if cpr_input.lower() == "k":
                    break

                if not cpr_input:
                    cpr = b["Best CPR"]
                    break

                try:
                    cpr = float(cpr_input)
                    break
                except:
                    if not warning_continue():
                        continue

            # Update notes
            while True:
                notes_input = input(f"Notes ({b['Notes']}): ").strip()

                if notes_input.lower() == "k":
                    break

                if not notes_input:
                    notes = b["Notes"]
                    break

                if notes_input.isdigit():
                    print("Input cannot be a number")
                    continue

                notes = notes_input
                break

            # Check if there are any changes
            if (plat == b["Platform"] and cpr == b["Best CPR"] and notes == b["Notes"]):
                print("\nNo data changes detected.")
                continue

            # Save changes
            if confirm_save():
                b.update({"Platform": plat, "Best CPR": cpr, "Notes": notes})
                print(f"\nBenchmark data {b['ID']} successfully updated.")

        elif choice == "2":
            break
        else:
            warning_continue()

# DELETE
# Delete benchmark data
def delete_benchmark():
    while True:
        print("\n--- Delete Data Menu ---")
        print("1. Delete Data")
        print("2. Back")
        choice = input("\nChoose: ").strip()

        if choice == "1":
            table_benchmark()
            kid = input("\nCampaign ID to delete: ").strip()

            if kid.lower() == "k":
                break

            b = checker_by_id(kid)
            if not b:
                print("\nBenchmark data not found!")
                continue

            if confirm_save():
                benchmarks.remove(b)
                print(f"\nBenchmark data {b['ID']} successfully deleted.")

        elif choice == "2":
            break
        else:
            warning_continue()

# PERFORMANCE
# Compare actual CPR against benchmark
def performance_check():
    while True:
        print("\n--- Performance Menu ---")
        print("1. Check Campaign Performance")
        print("2. Back")
        choice = input("\nChoose: ").strip()

        if choice == "1":
            table_category_platform()
            print("\n(type 'K' to cancel)")

            while True:
                cat = input("\nCategory: ").strip()
                if cat.lower() == "k":
                    return
                if cat.isdigit():
                    print("Input cannot be a number")
                    continue
                break

            allowed_platform = ["facebook","instagram","tiktok","google","shopee ads","tokopedia ads","youtube"]
            while True:
                plat = input("Platform: ").strip()

                if plat.lower() == "k":
                    return

                if plat.isdigit():
                    print("Input cannot be a number")
                    continue

                if plat.lower() not in allowed_platform:
                    print("\nPlatform not available.")
                    if not warning_continue():
                        continue
                    continue

                break

            b = checker(cat, plat)
            if not b:
                print("\nBenchmark not found.")
                continue

            # Actual CPR input
            while True:
                actual_input = input("Actual CPR: ").strip()

                if actual_input.lower() == "k":
                    return

                try:
                    actual = int(actual_input)

                    if actual == 0:
                        print("\nInput cannot be 0")
                        continue

                    if actual < 1000:
                        print("\nInput cannot be less than Rp 1,000")
                        continue

                    break

                except ValueError:
                    warning_continue()
                    continue

            benchmark = b["Best CPR"]

            print(f"\nBenchmark : Rp {benchmark}")
            print(f"Actual    : Rp {actual}")

            if actual > benchmark:
                print(f"\nPerformance below benchmark, Rp {actual - benchmark} more expensive. Needs evaluation!")
            elif actual == benchmark:
                print("\nPerformance meets benchmark, keep it up!")
            else:
                print(f"\nPerformance above benchmark, Rp {benchmark - actual} cheaper!")

        elif choice == "2":
            break
        else:
            warning_continue()

# MAIN LOOP
# Program entry point
while True:
    role = login()
    if not role:
        continue

    while program_running:
        dashboard(role)
        menu = input("\nChoose Menu Number: ").strip()

        if role == "admin":
            if menu == "1":
                read_table()
            elif menu == "2":
                add_benchmark()
            elif menu == "3":
                update_benchmark()
            elif menu == "4":
                delete_benchmark()
            elif menu == "5":
                performance_check()
            elif menu == "6":
                print("\nLogout successful.")
                break
            else:
                print("\nInvalid input!\n")

        else:
            if menu == "1":
                read_table()
            elif menu == "2":
                performance_check()
            elif menu == "3":
                print("\nLogout successful.")
                break
            else:
                print("\nInvalid input!\n")
