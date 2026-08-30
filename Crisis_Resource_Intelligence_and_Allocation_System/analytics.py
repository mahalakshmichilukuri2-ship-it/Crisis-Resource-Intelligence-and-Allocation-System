import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


RESOURCE_FILE = "data/resources.csv"


def view_statistics():

    if not os.path.exists(RESOURCE_FILE):
        print("\nNo resource data found.")
        return

    df = pd.read_csv(RESOURCE_FILE)

    if df.empty:
        print("\nNo records available.")
        return

    print("\n========== Resource Statistics ==========")
    print(df)

    total_resources = len(df)

    quantities = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0)

    total_quantity = np.sum(quantities)
    average_quantity = np.mean(quantities)
    maximum_quantity = np.max(quantities)
    minimum_quantity = np.min(quantities)

    print(f"\nTotal Resources : {total_resources}")
    print(f"Total Quantity  : {total_quantity}")
    print(f"Average Quantity: {average_quantity:.2f}")
    print(f"Maximum Quantity: {maximum_quantity}")
    print(f"Minimum Quantity: {minimum_quantity}")


def bar_chart():

    if not os.path.exists(RESOURCE_FILE):
        print("\nNo resource data found.")
        return

    df = pd.read_csv(RESOURCE_FILE)

    if df.empty:
        print("\nNo records available.")
        return

    quantity = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0)

    plt.figure(figsize=(8,5))
    plt.bar(df["Resource Name"], quantity)

    plt.title("Resource Quantity")
    plt.xlabel("Resource")
    plt.ylabel("Quantity")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def pie_chart():

    if not os.path.exists(RESOURCE_FILE):
        print("\nNo resource data found.")
        return

    df = pd.read_csv(RESOURCE_FILE)

    if df.empty:
        print("\nNo records available.")
        return

    quantity = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0)

    plt.figure(figsize=(6,6))

    plt.pie(
        quantity,
        labels=df["Resource Name"],
        autopct="%1.1f%%"
    )

    plt.title("Resource Distribution")
    plt.show()


def analytics_menu():

    while True:

        print("\n========== Analytics ==========")
        print("1. View Statistics")
        print("2. Bar Chart")
        print("3. Pie Chart")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_statistics()

        elif choice == "2":
            bar_chart()

        elif choice == "3":
            pie_chart()

        elif choice == "4":
            print("Exiting Analytics...")
            break

        else:
            print("Invalid Choice!")