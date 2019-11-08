class Customer:
    def __init__(self, name, address, vehicle_no, contact_no, nic_no, customer_id, customer_type="General", service_status=None):
        self.name = name
        self.address = address
        self.vehicle_no = vehicle_no
        self.contact_no = contact_no
        self.nic_no = nic_no
        self.customer_type = customer_type
        self.customer_id = customer_id
        self.service_status = service_status

    def __repr__(self):
        return f'Name: {self.name}, NIC: {self.nic_no}'


class Clean_park:
    def __init__(self):
        self.customer_list = []
        self.customer_id_list = []

    def add_customer(self):
        name = input("Input Customer Name: ")
        if name == "":
            raise ValueError("Please fill required fields...")
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

    def find_customer(self, customer_list):
        find_customer = int(input("Input Customer ID: "))
        first = 0
        last = len(customer_list) - 1
        while first != last:
            mid = (first + last) // 2
            if customer_list[mid].customer_id == find_customer:
                customer_list[mid] = self.update_customer_details(customer_list[first])
                print("Customer updated.")
                return True
            else:
                if find_customer < customer_list[mid].customer_id:
                    last = mid
                else:
                    first = mid
        if customer_list[first].customer_id == find_customer:
            customer_list[first] = self.update_customer_details(customer_list[first])
            print("Customer updated.")
            return True
        else:
            raise ValueError("Customer not found.")

    def update_customer_details(self, customer):
        customer.name = input("New customer name: ")
        customer.address = input("New address: ")
        customer.vehicle_no = input("New vehicle No.: ")
        customer.contact_no = input("New contact No.: ")
        customer.nic_no = input("New NIC No.: ")
        customer.customer_type = input("New customer type: ")
        return customer

    def view_customer_details(self):
        view_customer = int(input("Input Customer ID: "))
        if view_customer in self.customer_id_list:
            self.customer_list = [customer for customer in self.customer_list if customer.customer_id == view_customer]
            print(self.customer_list)
        else:
            print("No customer under this identity")

    def request_service(self, customer):
        requested_customer = int(input("Input customer ID: "))
        if requested_customer in self.customer_id_list:
            for customer in self.customer_list:
                if customer.service_status is None:
                    print("Please enter these values\
                    Enter I for in progress\
                    Enter C for completed\
                    Enter N for not conducted")
                    customer.service_status = input("Input service status: ")
                    customer.vehicle_no = input("Input vehicle number: ")
                    self.customer_list.append(customer.service_status)
                    self.customer_list.append(customer.vehicle_no)
                elif customer.service_status == "I":
                    customer.service_status = input("Input service status: ")
                    customer.vehicle_no = input("Input vehicle number: ")
                return True

    def select_option(self):
        while True:
            print("Welcome to Clean Park Daily Car Service")
            print("Select Options")
            print("Enter No.1 to register a new customer")
            print("Enter No.2 to remove a customer")
            print("Enter No.3 to update customer details")
            print("Enter No.4 to view customer details")
            print("Enter No.5 to view all customers")
            print("Enter No.6 to request for a service")
            print("Enter No.7 to add the service to queue")
            print("Enter No.8 to remove the service from queue")
            print("Enter No.9 to view the service status")
            try:
                choice = int(input("Select option: "))
                if choice is 1:
                    self.add_customer()
                elif choice is 2:
                    self.remove_customer()
                elif choice is 3:
                    self.find_customer(self.customer_list)
                elif choice is 4:
                    self.view_customer_details()
                elif choice is 5:
                    for customer in self.customer_list:
                        print("Customer Name: ", customer.name, "Customer ID: ", customer.customer_id)
                elif choice is 6:
                    self.request_service(self.customer_id_list)
                else:
                    raise ValueError("Invalid Option.")
            except ValueError:
                print("Invalid choice. Please input a valid option.")


menu1 = Clean_park()
menu1.select_option()
