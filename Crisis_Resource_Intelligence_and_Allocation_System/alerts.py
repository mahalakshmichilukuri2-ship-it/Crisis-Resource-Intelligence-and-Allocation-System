import pandas as pd
import os

RESOURCE_FILE = "data/resources.csv"
HOSPITAL_FILE = "data/hospitals.csv"
VEHICLE_FILE = "data/vehicles.csv"

def low_resource_alert():

    print("\n========== Low Resource Alert ==========")

    if not os.path.exists(RESOURCE_FILE):
        print("Resource file not found.")
        return

    df = pd.read_csv(RESOURCE_FILE)

    if df.empty:
        print("No resource data available.")
        return

    quantity = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0)

    found = False

    for i in range(len(df)):
        if quantity[i] < 10:
            print(f"{df['Resource Name'][i]} is running low (Quantity: {quantity[i]})")
            found = True

    if not found:
        print("All resources are sufficient.")


def hospital_alert():

    print("\n========== Hospital Bed Alert ==========")

    if not os.path.exists(HOSPITAL_FILE):
        print("Hospital file not found.")
        return

    df = pd.read_csv(HOSPITAL_FILE)

    if df.empty:
        print("No hospital data available.")
        return

    beds = pd.to_numeric(df["Available Beds"], errors="coerce").fillna(0)

    found = False

    for i in range(len(df)):
        if beds[i] == 0:
            print(f"{df['Hospital Name'][i]} has no available beds.")
            found = True

    if not found:
        print("Beds are available in all hospitals.")


def vehicle_alert():

    print("\n========== Vehicle Alert ==========")

    if not os.path.exists(VEHICLE_FILE):
        print("Vehicle file not found.")
        return

    df = pd.read_csv(VEHICLE_FILE)

    if df.empty:
        print("No vehicle data available.")
        return

    found = False

    for i in range(len(df)):
        if df["Status"][i].lower() != "available":
            print(f"{df['Vehicle Type'][i]} ({df['Vehicle ID'][i]}) is Busy.")
            found = True

    if not found:
        print("All vehicles are available.")


def emergency_alert():

    print("\n========== Emergency Alert ==========")
    print("Emergency! Immediate response is required.")
    print("Allocate resources, hospitals, vehicles, and volunteers immediately.")


def alerts_menu():

    while True:

        print("\n========== ALERTS ==========")
        print("1. Low Resource Alert")
        print("2. Hospital Bed Alert")
        print("3. Vehicle Alert")
        print("4. Emergency Alert")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            low_resource_alert()

        elif choice == "2":
            hospital_alert()

        elif choice == "3":
            vehicle_alert()

        elif choice == "4":
            emergency_alert()

        elif choice == "5":
            print("Exiting Alerts...")
            break

        else:
            print("Invalid Choice!")