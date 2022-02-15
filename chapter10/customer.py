class Customer:
    name = "John Johnsson"
    total = 1000
    paymenttype = "Masterexpress"
    number = "1234-5678-9012345"

    def printout(self):
        print("Name: ", self.name)
        print("Total: ", self.total)
        print("Payment type: ", self.paymenttype)
        print("Card/Bill number: ", self.number)

class ManageCustomer(Customer):
    def addbill(self):
        self.total = self.total + 50
    
    def payment(self):
        self.total = self.total - 100


def main():
    customer = Customer()
    manager = ManageCustomer()

if __name__ == "__main__":
    main()