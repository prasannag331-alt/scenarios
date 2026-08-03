import argparse
import csv
import sys


def read_employee_records(filename):
    """Reads employee records from the given CSV file."""
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            # Using DictReader to easily access fields by header names
            reader = csv.DictReader(file)

            # Check if file has headers
            if not reader.fieldnames:
                print(f"Error: The file '{filename}' is empty or invalid.")
                return []

            return list(reader)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def display_all_employees(records):
    """Displays all employee details in a structured format."""
    if not records:
        print("No employee records found.")
        return

    print("\n--- Employee Records ---")
    # Dynamically print headers based on CSV columns
    headers = records[0].keys()
    header_line = " | ".join(headers)
    print(header_line)
    print("-" * len(header_line))

    for row in records:
        print(" | ".join(row.values()))
    print("------------------------\n")


def search_employee(records, emp_id):
    """Searches for a specific employee using Employee ID."""
    if not records:
        print("No records available to search.")
        return

    # Determine the exact name of the ID column (handling potential spaces/casing)
    id_field = None
    for key in records[0].keys():
        if "id" in key.lower():
            id_field = key
            break

    if not id_field:
        print("Error: Could not identify an 'Employee ID' column in the CSV.")
        return

    # Perform the search
    for row in records:
        if row[id_field].strip() == emp_id.strip():
            print(f"\nEmployee Found:")
            for key, value in row.items():
                print(f"{key}: {value}")
            return

    print(f"\nEmployee with ID '{emp_id}' not found.")


def main():
    # Setup command-line argument parser
    parser = argparse.ArgumentParser(
        description="Employee Record Management System"
    )
    parser.add_argument(
        "filename",
        help="Path to the employee CSV file (e.g., employee.csv)",
    )
    args = parser.parse_args()

    # 1. Read employee records
    records = read_employee_records(args.filename)

    # 2. Display all employee details
    display_all_employees(records)

    # 3. Search for an employee using Employee ID
    search_id = input("Enter Employee ID to search: ")
    search_employee(records, search_id)


if _name_ == "_main_":
    main()
