class Employee:
    def _init_(self, emp_id, name, salary):
        """Initializes employee attributes."""
        self.emp_id = emp_id
        self.name = name
        self.salary = float(salary)

    def get_category(self):
        """Categorizes the employee based on their salary."""
        if self.salary >= 70000:
            return "High Salary"
        elif 40000 <= self.salary <= 69999:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display_details(self):
        """Returns a formatted string of the employee's information."""
        category = self.get_category()
        return f"ID: {self.emp_id:<10} Name: {self.name:<20} Salary: ₹{self.salary:<12,.2f} Category: {category}"


class Company:
    def _init_(self, company_name):
        """Initializes the company with a name and an empty employee repository."""
        self.company_name = company_name
        self.employees = []

    def add_employee(self, emp_id, name, salary):
        """Creates a new Employee instance and adds it to the list."""
        new_employee = Employee(emp_id, name, salary)
        self.employees.append(new_employee)
        print(f"Success: Employee '{name}' added successfully.")

    def display_all_employees(self):
        """Displays the details of all employees in the company."""
        print(f"\n--- {self.company_name} Employee Directory ---")
        if not self.employees:
            print("No employees found in the system.")
            return
        
        for emp in self.employees:
            print(emp.display_details())


# --- Demonstration of the Application ---
if _name_ == "_main_":
    # Create a Company instance
    my_company = Company("TechCorp Solutions")

    # Add employee details
    print("--- Adding Employees ---")
    my_company.add_employee("E001", "Aarav Sharma", 85000)   # High Salary
    my_company.add_employee("E002", "Diya Patel", 55000)     # Medium Salary
    my_company.add_employee("E003", "Amit Kumar", 32000)     # Low Salary
    my_company.add_employee("E004", "Sneha Reddy", 40000)    # Medium Salary (Edge case)

    # Display all employee information
    my_company.display_all_employees()
