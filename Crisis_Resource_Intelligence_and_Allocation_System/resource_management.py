import csv
import os

FILE_NAME = "data/resources.csv"


class Resource:

    def __init__(self, resource_id, resource_name, quantity, location):

        self.resource_id = resource_id
        self.resource_name = resource_name
        self.quantity = quantity
        self.location = location

    def to_dict(self):

        return {
            "Resource ID": self.resource_id,
            "Resource Name": self.resource_name,
            "Quantity": self.quantity,
            "Location": self.location
        }


def create_file():

    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "Resource ID",
                    "Resource Name",
                    "Quantity",
                    "Location"
                ]
            )

            writer.writeheader()


def add_resource():

    create_file()

    print("\n----- Add Resource -----")

    resource_id = input("Enter Resource ID: ")
    resource_name = input("Enter Resource Name: ")
    quantity = input("Enter Quantity: ")
    location = input("Enter Location: ")

    resource = Resource(
        resource_id,
        resource_name,
        quantity,
        location
    )

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Resource ID",
                "Resource Name",
                "Quantity",
                "Location"
            ]
        )

        writer.writerow(resource.to_dict())

    print("\nResource Added Successfully.")


def view_resource():

    create_file()

    print("\n----- Resource Records -----")

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(row)


def search_resource():

    create_file()

    search_id = input("\nEnter Resource ID to Search: ")

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Resource ID"] == search_id:

                print("\nResource Found")
                print(row)

                found = True
                break

    if not found:
        print("\nResource Not Found.")


def resource_menu():

    while True:

        print("\n========== Resource Management ==========")
        print("1. Add Resource")
        print("2. View Resource")
        print("3. Search Resource")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_resource()

        elif choice == "2":
            view_resource()

        elif choice == "3":
            search_resource()

        elif choice == "4":
            print("Exiting Resource Management...")
            break

        else:
            print("Invalid Choice! Please try again.")