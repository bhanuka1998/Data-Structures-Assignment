class Customer:
    def __init__(self, name, address, vehicle_no, contact_no, nic_no, customer_id, customer_type="General"):
        self.name = name
        self.address = address
        self.vehicle_no = vehicle_no
        self.contact_no = contact_no
        self.nic_no = nic_no
        self.customer_type = customer_type
        self.customer_id = customer_id


class Clean_park:
    def __init__(self):
        self.customer_list = []
        self.customer_id_list = []

    def add_customer(self):
        name = input("Input Customer Name: ")
        address = input("Input Customer Address: ")
        vehicle_no = input("Input Vehicle Number: ")
        contact_no = input("Input Contact Number: ")
        nic_no = input("Input NIC Number: ")
        # return name, address, vehicle_no, contact_no, nic_no
        if len(self.customer_list) is 0:
            customer_id = 0
        else:
            customer_id = self.customer_list[-1].customer_id + 1
        self.customer_list.append(Customer(name, address, vehicle_no, contact_no, nic_no, customer_id))
        self.customer_id_list.append(customer_id)

    def remove_customer(self):
        to_delete = int(input("Input Customer ID: "))
        if to_delete in self.customer_id_list:
            self.customer_list = [customer for customer in self.customer_list if customer.customer_id != to_delete]
            self.customer_id_list.remove(to_delete)
        else:
            print("No customer under this identity")

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
            if choice is 1:
                self.add_customer()
            elif choice is 2:
                self.remove_customer()
            elif choice is 3:
                pass
            elif choice is 4:
                for customer in self.customer_list:
                    print("Customer Name: ", customer.name, "Customer ID: ", customer.customer_id)



menu1 = Clean_park()
menu1.select_option()