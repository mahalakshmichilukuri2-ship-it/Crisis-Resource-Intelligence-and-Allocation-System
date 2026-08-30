from crisis_management import crisis_menu
from resource_management import resource_menu
from hospital_management import hospital_menu
from vehicle_management import vehicle_menu
from volunteer_management import volunteer_menu
from resource_allocation import allocation_menu
from analytics import analytics_menu
from reports import reports_menu
from alerts import alerts_menu


def main():

    while True:

        print("\n" + "=" * 65)
        print("CRISIS RESOURCE INTELLIGENCE AND ALLOCATION SYSTEM")
        print("=" * 65)
        print("1. Crisis Management")
        print("2. Resource Management")
        print("3. Hospital Management")
        print("4. Vehicle Management")
        print("5. Volunteer Management")
        print("6. Resource Allocation")
        print("7. Analytics")
        print("8. Reports")
        print("9. Alerts")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            crisis_menu()

        elif choice == "2":
            resource_menu()

        elif choice == "3":
            hospital_menu()

        elif choice == "4":
            vehicle_menu()

        elif choice == "5":
            volunteer_menu()

        elif choice == "6":
            allocation_menu()

        elif choice == "7":
            analytics_menu()

        elif choice == "8":
            reports_menu()

        elif choice == "9":
            alerts_menu()

        elif choice == "10":
            print("\nThank you for using the system.")
            print("Exiting...")
            break

        else:
            print("\nInvalid Choice! Please enter a number between 1 and 10.")


if __name__ == "__main__":
    main()