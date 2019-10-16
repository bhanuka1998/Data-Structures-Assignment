class customer:
    def __init__(self, name, address, vehicle_no, contact_no, nic_no, customer_type="General"):
        self.name = name
        self.address = address
        self.vehicle_no = vehicle_no
        self.contact_no = contact_no
        self.nic_no = nic_no
        self.customer_type = customer_type

class clean_park:
    def select_option(self):
        while True:
            print("Welcome to Clean Park Daily Car Service")
            print("Select Options")
            print("Enter No.1 to register a new customer")
            print("Enter No.2 to remove a customer")
            print("Enter No.3 to update customer details")
            print("Enter No.4 to view customer details")
            print("Enter No.4 to view all customers")
            print("Enter No.5 to request for a service")
            print("Enter No.6 to add the service to queue")
            print("Enter No.7 to remove the service from queue")
            print("Enter No.8 to view the service status")
            choice = int(input("Select option: "))


menu1 = clean_park()
menu1.select_option()