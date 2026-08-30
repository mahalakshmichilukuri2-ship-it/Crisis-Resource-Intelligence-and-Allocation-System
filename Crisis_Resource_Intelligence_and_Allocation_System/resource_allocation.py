import csv
import os

FILE_NAME = "data/allocations.csv"


class Allocation:

    def __init__(self, allocation_id, crisis_id,
                 resource_name, quantity, location):

        self.allocation_id = allocation_id
        self.crisis_id = crisis_id
        self.resource_name = resource_name
        self.quantity = quantity
        self.location = location

    def to_dict(self):

        return {
            "Allocation ID": self.allocation_id,
            "Crisis ID": self.crisis_id,
            "Resource": self.resource_name,
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
                    "Allocation ID",
                    "Crisis ID",
                    "Resource",
                    "Quantity",
                    "Location"
                ]
            )

            writer.writeheader()


def allocate_resource():

    create_file()

    print("\n----- Resource Allocation -----")

    allocation_id = input("Enter Allocation ID: ")
    crisis_id = input("Enter Crisis ID: ")
    resource = input("Enter Resource Name: ")
    quantity = input("Enter Quantity: ")
    location = input("Enter Location: ")

    allocation = Allocation(
        allocation_id,
        crisis_id,
        resource,
        quantity,
        location
    )

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Allocation ID",
                "Crisis ID",
                "Resource",
                "Quantity",
                "Location"
            ]
        )

        writer.writerow(allocation.to_dict())

    print("\nResource Allocated Successfully.")


def view_allocations():

    create_file()

    print("\n----- Allocation Records -----")

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(row)


def search_allocation():

    create_file()

    allocation_id = input("Enter Allocation ID: ")

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Allocation ID"] == allocation_id:

                print("\nAllocation Found")
                print(row)

                found = True
                break

    if not found:
        print("\nAllocation Not Found")


def allocation_menu():

    while True:

        print("\n========== Resource Allocation ==========")
        print("1. Allocate Resource")
        print("2. View Allocations")
        print("3. Search Allocation")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            allocate_resource()

        elif choice == "2":
            view_allocations()

        elif choice == "3":
            search_allocation()

        elif choice == "4":
            print("Exiting Resource Allocation...")
            break

        else:
            print("Invalid Choice!")