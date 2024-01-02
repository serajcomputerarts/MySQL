from services.customerService import CustomerService
from tables.customer import Customer

customerService = CustomerService()
customer = Customer()
customer.customerName = "Test"
customer.contactLastName = "Test"
customer.contactFirstName = "Test"
customer.phone = "Test"
customer.addressLine1 = "Test"
customer.addressLine2 = "Test"
customer.city = "Test"
customer.state = "Test"
customer.postalCode = "Test"
customer.country = "Test"
customer.creditLimit = 1

customerService.addCustomer(customer,"Murphy")