import csv
import os

FILE_NAME = "data/hospitals.csv"


class Hospital:

    def __init__(self, hospital_id, hospital_name, location, beds):

        self.hospital_id = hospital_id
        self.hospital_name = hospital_name
        self.location = location
        self.beds = beds

    def to_dict(self):

        return {
            "Hospital ID": self.hospital_id,
            "Hospital Name": self.hospital_name,
            "Location": self.location,
            "Available Beds": self.beds
        }


def create_file():

    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "Hospital ID",
                    "Hospital Name",
                    "Location",
                    "Available Beds"
                ]
            )

            writer.writeheader()


def add_hospital():

    create_file()

    print("\n----- Add Hospital -----")

    hospital_id = input("Enter Hospital ID: ")
    hospital_name = input("Enter Hospital Name: ")
    location = input("Enter Location: ")
    beds = input("Enter Available Beds: ")

    hospital = Hospital(
        hospital_id,
        hospital_name,
        location,
        beds
    )

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Hospital ID",
                "Hospital Name",
                "Location",
                "Available Beds"
            ]
        )

        writer.writerow(hospital.to_dict())

    print("\nHospital Added Successfully.")


def view_hospital():

    create_file()

    print("\n----- Hospital Records -----")

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(row)


def search_hospital():

    create_file()

    search_id = input("\nEnter Hospital ID to Search: ")

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Hospital ID"] == search_id:

                print("\nHospital Found")
                print(row)

                found = True
                break

    if not found:
        print("\nHospital Not Found.")


def hospital_menu():

    while True:

        print("\n========== Hospital Management ==========")
        print("1. Add Hospital")
        print("2. View Hospital")
        print("3. Search Hospital")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_hospital()

        elif choice == "2":
            view_hospital()

        elif choice == "3":
            search_hospital()

        elif choice == "4":
            print("Exiting Hospital Management...")
            break

        else:
            print("Invalid Choice! Please try again.")