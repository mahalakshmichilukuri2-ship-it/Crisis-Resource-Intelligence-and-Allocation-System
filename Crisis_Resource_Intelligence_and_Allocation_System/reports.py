import pandas as pd
import os

FILES = {
    "Crises": "data/crisis_data.csv",
    "Resources": "data/resources.csv",
    "Hospitals": "data/hospitals.csv",
    "Vehicles": "data/vehicles.csv",
    "Volunteers": "data/volunteers.csv",
    "Allocations": "data/allocations.csv"
}


def display_report(title, file_name):

    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    if not os.path.exists(file_name):
        print("File not found.")
        return

    df = pd.read_csv(file_name)

    if df.empty:
        print("No records available.")

        
    else:
        print(df)


def summary_report():

    print("\n========== PROJECT SUMMARY ==========")

    for title, file_name in FILES.items():

        if os.path.exists(file_name):

            df = pd.read_csv(file_name)

            print(f"{title}: {len(df)} Records")

        else:
            print(f"{title}: File Not Found")


def reports_menu():

    while True:

        print("\n========== REPORTS ==========")
        print("1. Crisis Report")
        print("2. Resource Report")
        print("3. Hospital Report")
        print("4. Vehicle Report")
        print("5. Volunteer Report")
        print("6. Allocation Report")
        print("7. Summary Report")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_report("Crisis Report", FILES["Crises"])

        elif choice == "2":
            display_report("Resource Report", FILES["Resources"])

        elif choice == "3":
            display_report("Hospital Report", FILES["Hospitals"])

        elif choice == "4":
            display_report("Vehicle Report", FILES["Vehicles"])

        elif choice == "5":
            display_report("Volunteer Report", FILES["Volunteers"])

        elif choice == "6":
            display_report("Allocation Report", FILES["Allocations"])

        elif choice == "7":
            summary_report()

        elif choice == "8":
            print("Exiting Reports...")
            break

        else:
            print("Invalid Choice!")