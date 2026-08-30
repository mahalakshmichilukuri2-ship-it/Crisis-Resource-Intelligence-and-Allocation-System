import csv
import os

FILE_NAME = "data/volunteers.csv"


class Volunteer:

    def __init__(self, volunteer_id, volunteer_name, phone, area):

        self.volunteer_id = volunteer_id
        self.volunteer_name = volunteer_name
        self.phone = phone
        self.area = area

    def to_dict(self):

        return {
            "Volunteer ID": self.volunteer_id,
            "Volunteer Name": self.volunteer_name,
            "Phone": self.phone,
            "Area": self.area
        }


def create_file():

    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "Volunteer ID",
                    "Volunteer Name",
                    "Phone",
                    "Area"
                ]
            )

            writer.writeheader()


def add_volunteer():

    create_file()

    print("\n----- Add Volunteer -----")

    volunteer_id = input("Enter Volunteer ID: ")
    volunteer_name = input("Enter Volunteer Name: ")
    phone = input("Enter Phone Number: ")
    area = input("Enter Assigned Area: ")

    volunteer = Volunteer(
        volunteer_id,
        volunteer_name,
        phone,
        area
    )

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Volunteer ID",
                "Volunteer Name",
                "Phone",
                "Area"
            ]
        )

        writer.writerow(volunteer.to_dict())

    print("\nVolunteer Added Successfully.")


def view_volunteer():

    create_file()

    print("\n----- Volunteer Records -----")

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(row)


def search_volunteer():

    create_file()

    search_id = input("\nEnter Volunteer ID to Search: ")

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Volunteer ID"] == search_id:

                print("\nVolunteer Found")
                print(row)

                found = True
                break

    if not found:
        print("\nVolunteer Not Found.")


def volunteer_menu():

    while True:

        print("\n========== Volunteer Management ==========")
        print("1. Add Volunteer")
        print("2. View Volunteer")
        print("3. Search Volunteer")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_volunteer()

        elif choice == "2":
            view_volunteer()

        elif choice == "3":
            search_volunteer()

        elif choice == "4":
            print("Exiting Volunteer Management...")
            break

        else:
            print("Invalid Choice! Please try again.")