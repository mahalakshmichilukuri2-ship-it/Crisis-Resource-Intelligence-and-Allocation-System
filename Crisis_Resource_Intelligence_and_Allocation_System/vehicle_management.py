import csv
import os

FILE_NAME = "data/vehicles.csv"


class Vehicle:

    def __init__(self, vehicle_id, vehicle_type, driver_name, status):

        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.driver_name = driver_name
        self.status = status

    def to_dict(self):

        return {
            "Vehicle ID": self.vehicle_id,
            "Vehicle Type": self.vehicle_type,
            "Driver Name": self.driver_name,
            "Status": self.status
        }


def create_file():

    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "Vehicle ID",
                    "Vehicle Type",
                    "Driver Name",
                    "Status"
                ]
            )

            writer.writeheader()


def add_vehicle():

    create_file()

    print("\n----- Add Vehicle -----")

    vehicle_id = input("Enter Vehicle ID: ")
    vehicle_type = input("Enter Vehicle Type: ")
    driver_name = input("Enter Driver Name: ")
    status = input("Enter Status (Available/Busy): ")

    vehicle = Vehicle(
        vehicle_id,
        vehicle_type,
        driver_name,
        status
    )

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Vehicle ID",
                "Vehicle Type",
                "Driver Name",
                "Status"
            ]
        )

        writer.writerow(vehicle.to_dict())

    print("\nVehicle Added Successfully.")


def view_vehicle():

    create_file()

    print("\n----- Vehicle Records -----")

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(row)


def search_vehicle():

    create_file()

    search_id = input("\nEnter Vehicle ID to Search: ")

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Vehicle ID"] == search_id:

                print("\nVehicle Found")
                print(row)

                found = True
                break

    if not found:
        print("\nVehicle Not Found.")


def vehicle_menu():

    while True:

        print("\n========== Vehicle Management ==========")
        print("1. Add Vehicle")
        print("2. View Vehicle")
        print("3. Search Vehicle")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_vehicle()

        elif choice == "2":
            view_vehicle()

        elif choice == "3":
            search_vehicle()

        elif choice == "4":
            print("Exiting Vehicle Management...")
            break

        else:
            print("Invalid Choice! Please try again.")