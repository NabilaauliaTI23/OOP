# Banking System Simulation
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")
    
    def display_details(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 500:
            print("Withdrawal limit exceeded! Maximum allowed: $500")
        else:
            super().withdraw(amount)

class PremiumSavingsAccount(SavingsAccount):
    def withdraw(self, amount):
        if amount > 2000:
            print("Withdrawal limit exceeded! Maximum allowed: $2000")
        else:
            super().withdraw(amount)

# Employee Management System
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def calculate_salary(self):
        return self.salary
    
    def show_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: ${self.calculate_salary()}")

class Manager(Employee):
    def calculate_salary(self):
        return self.salary * 1.2  # 20% bonus

class Engineer(Employee):
    def calculate_salary(self):
        return self.salary * 1.1  # 10% performance bonus

class Intern(Employee):
    def calculate_salary(self):
        return self.salary  # Fixed stipend

# Vehicle Rental System
class Vehicle:
    def __init__(self, brand, model, rental_rate):
        self.brand = brand
        self.model = model
        self.rental_rate = rental_rate
    
    def calculate_rental(self, days):
        return self.rental_rate * days

class Car(Vehicle):
    def open_trunk(self):
        print("Trunk opened!")

class Bike(Vehicle):
    def kickstart(self):
        print("Bike kickstarted!")

class LuxuryFeatures:
    def enable_gps(self):
        print("GPS enabled!")
    
    def enable_heated_seats(self):
        print("Heated seats enabled!")

class LuxuryCar(Car, LuxuryFeatures):
    def calculate_rental(self, days):
        return super().calculate_rental(days) + 50 * days  # Extra charge for luxury

# Testing the implementation
if __name__ == "__main__":
    # Banking System Test
    print("\nBanking System Test:")
    savings = SavingsAccount("SA123", 1000)
    savings.deposit(200)
    savings.withdraw(600)
    savings.withdraw(400)
    savings.display_details()
    
    premium = PremiumSavingsAccount("PA456", 5000)
    premium.withdraw(1500)
    premium.withdraw(2500)
    premium.display_details()
    
    # Employee Management Test
    print("\nEmployee Management Test:")
    emp1 = Manager("Alice", 101, 5000)
    emp2 = Engineer("Bob", 102, 4000)
    emp3 = Intern("Charlie", 103, 1500)
    emp1.show_details()
    emp2.show_details()
    emp3.show_details()
    
    # Vehicle Rental Test
    print("\nVehicle Rental Test:")
    car = Car("Toyota", "Camry", 50)
    bike = Bike("Yamaha", "R15", 30)
    luxury_car = LuxuryCar("BMW", "7 Series", 100)
    
    print(f"Car rental for 3 days: ${car.calculate_rental(3)}")
    print(f"Bike rental for 2 days: ${bike.calculate_rental(2)}")
    print(f"LuxuryCar rental for 5 days: ${luxury_car.calculate_rental(5)}")
    
    luxury_car.enable_gps()
    luxury_car.enable_heated_seats()