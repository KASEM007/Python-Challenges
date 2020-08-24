class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type


    def update_membership(self, new_membership):



# x = Customer("Kasem", "Gold")
# print(x.name, "membership type is", x.membership_type)

customers = [
    Customer("Kasem", "Gold"),
    Customer("Aysha", "Silver"),
    Customer("Huda", "Bronz"),
]

customers[1].verified = False
print(customers[1].verified)


















# https://www.youtube.com/watch?v=MikphENIrOo&t=47s
