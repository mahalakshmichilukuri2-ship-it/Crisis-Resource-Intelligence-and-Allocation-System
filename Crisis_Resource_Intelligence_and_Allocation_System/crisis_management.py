import csv
import os

FILE_NAME = "data/crisis_data.csv"


class Crisis:

    def __init__(self, crisis_id, crisis_type, location, severity, status):

        self.crisis_id = crisis_id
        self.crisis_type = crisis_type
        self.location = location
        self.severity = severity
        self.status = status

    def to_dict(self):

        return {
            "Crisis ID": self.crisis_id,
            "Crisis Type": self.crisis_type,
            "Location": self.location,
            "Severity": self.severity,
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
                    "Crisis ID",
                    "Crisis Type",
                    "Location",
                    "Severity",
                    "Status"
                ]
            )

            writer.writeheader()
def add_crisis():

    create_file()

    print("\n----- Add Crisis -----")

    crisis_id = input("Enter Crisis ID: ")
    crisis_type = input("Enter Crisis Type: ")
    location = input("Enter Location: ")
    severity = input("Enter Severity (Low/Medium/High): ")
    status = input("Enter Status: ")

    crisis = Crisis(
        crisis_id,
        crisis_type,
        location,
        severity,
        status
    )

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Crisis ID",
                "Crisis Type",
                "Location",
                "Severity",
                "Status"
            ]
        )

        writer.writerow(crisis.to_dict())

    print("\nCrisis Added Successfully.")


def view_crisis():

    create_file()

    print("\n----- Crisis Records -----")

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(row)


def search_crisis():

    create_file()

    search_id = input("\nEnter Crisis ID to Search: ")

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Crisis ID"] == search_id:

                print("\nCrisis Found")
                print(row)

                found = True
                break

    if not found:
        print("\nCrisis Not Found.")
def crisis_menu():

    while True:

        print("\n========== Crisis Management ==========")
        print("1. Add Crisis")
        print("2. View Crisis")
        print("3. Search Crisis")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_crisis()

        elif choice == "2":
            view_crisis()

        elif choice == "3":
            search_crisis()

        elif choice == "4":
            print("Exiting Crisis Management...")
            break

        else:
            print("Invalid Choice! Please try again.")