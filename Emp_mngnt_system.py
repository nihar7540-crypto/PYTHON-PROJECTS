class Person:
    """
    Creates a basic person with name and age.
    Arguments: name, age
    Returns: None
    """
    def __init__(self,name,age):
        """
        Initializes the person object.
        Arguments: name, age
        Returns: None
        """
        self.name = name
        self.age = age
        
    def display(self):
        """
        Prints the person details.
        Arguments: None
        Returns: None
        """
        print("Name:", self.name)
        print("Age:", self.age)
        
    def __del__(self):
        """
        Deletes the object and cleans up resources.
        Arguments: None
        Returns: None
        """
        pass

class Employee(Person):
    """
    Creates an employee using inheritance and encapsulation.
    Arguments: name, age, emp_id, salary
    Returns: None
    """
    def __init__(self,name,age,emp_id,salary):
        """
        Initializes employee details using super and private variables.
        Arguments: name, age, emp_id, salary
        Returns: None
        """
        super().__init__(name, age)
        self.__emp_id = emp_id
        self.__salary = salary
        
    def get_salary(self):
        """
        Retrieves the private salary data.
        Arguments: None
        Returns: salary
        """
        return self.__salary
        
    def set_salary(self, salary):
        """
        Updates the private salary data.
        Arguments: salary
        Returns: None
        """
        self.__salary = salary
        
    def display(self):
        """
        Overrides display method to show employee details.
        Arguments: None
        Returns: None
        """
        super().display()
        print("Employee ID:", self.__emp_id)
        print("Salary:", self.__salary)

class Manager(Employee):
    """
    Creates a manager object inherited from employee.
    Arguments: name, age, emp_id, salary, dept
    Returns: None
    """
    def __init__(self,name,age,emp_id,salary,dept):
        """
        Initializes manager details including department.
        Arguments: name, age, emp_id, salary, dept
        Returns: None
        """
        super().__init__(name, age, emp_id, salary)
        self.dept = dept
        
    def display(self):
        """
        Overrides display method to show manager department.
        Arguments: None
        Returns: None
        """
        super().display()
        print("Department:", self.dept)

class Developer(Employee):
    """
    Creates a developer object inherited from employee.
    Arguments: name, age, emp_id, salary, lang
    Returns: None
    """
    def __init__(self,name,age,emp_id,salary,lang):
        """
        Initializes developer details including programming language.
        Arguments: name, age, emp_id, salary, lang
        Returns: None
        """
        super().__init__(name, age, emp_id, salary)
        self.lang = lang
        
    def display(self):
        """
        Overrides display method to show programming language.
        Arguments: None
        Returns: None
        """
        super().display()
        print("Language:", self.lang)

def print_documentation():
    """
    Prints all the docstrings of the project.
    Arguments: None
    Returns: None
    """
    print("###### Project Documentation ######")
    print(Person.__doc__)
    print(Person.__init__.__doc__)
    print(Person.display.__doc__)
    
    print(Employee.__doc__)
    print(Employee.__init__.__doc__)
    print(Employee.get_salary.__doc__)
    print(Employee.set_salary.__doc__)
    print(Employee.display.__doc__)
    
    print(Manager.__doc__)
    print(Manager.__init__.__doc__)
    print(Manager.display.__doc__)
    
    print(Developer.__doc__)
    print(Developer.__init__.__doc__)
    print(Developer.display.__doc__)

# User Interface
records = []

while True:
    print("Choose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        person_obj = Person(name, age)
        records.append(person_obj)
        print("Person created.")
        
    elif choice == "2":
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        emp_id = input("Enter Employee ID: ")
        salary = input("Enter Salary: ")
        employee_obj = Employee(name, age, emp_id, salary)
        records.append(employee_obj)
        print("Employee created.")
        
    elif choice == "3":
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        emp_id = input("Enter Employee ID: ")
        salary = input("Enter Salary: ")
        dept = input("Enter Department: ")
        manager_obj = Manager(name, age, emp_id, salary, dept)
        records.append(manager_obj)
        print("Manager created.")
        
    elif choice == "4":
        check_subclass = issubclass(Manager, Employee)
        print("Manager is subclass of Employee:", check_subclass)
        for record in records:
            record.display()
            
    elif choice == "5":
        print("Thank You , all data freed")
        print_documentation()
        break