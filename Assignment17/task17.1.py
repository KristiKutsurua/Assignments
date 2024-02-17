class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"

class House:
    def __init__(self, ID, price, owner, status="გასაყიდი"):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status

    def sell_home(self, buyer, loan_size=None):
        if loan_size is None:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "გაყიდული"
            print(f"The house with ID {self.ID} has been sold to {buyer.name}")
        else:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "გაყიდული სესხით"
            buyer.loan += loan_size
            print(f"The house with ID {self.ID} has been loaned to {buyer.name} with a loan size of {loan_size}")

# Creating Person objects
seller = Person("Giorgi")
buyer = Person("Nika")

# Creating House object with the seller as the owner
house = House(ID=123, price=200000, owner=seller)

print("Before selling:")
print("Seller:", seller)
print("Buyer:", buyer)
print("House Owner:", house.owner.name)
print("Status:", house.status)  # Output the owner's name instead of the object reference

# Selling the house to the buyer without a loan
house.sell_home(buyer)

print("\nAfter selling without a loan:")
print("Seller:", seller)
print("Buyer:", buyer)
print("House Owner:", house.owner.name)
print("Status:", house.status)  # Output the owner's name instead of the object reference

# Creating House object with the seller as the owner again
house2 = House(ID=456, price=300000, owner=seller)

house2.sell_home(buyer, loan_size=50000)

print("\nAfter selling with a loan:")
print("Seller:", seller)
print("Buyer:", buyer)
print("House Owner:", house2.owner.name)
print("Status:", house.status)