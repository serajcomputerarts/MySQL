from databaseClasses.tableRepository import TableRepository
from tables.customer import Customer
from tables.employee import Employee
from services.employeeService import EmployeeService
import random
import string


class CustomerService(TableRepository):
    employeeService : EmployeeService 
    def  __init__(self):
        CustomerService.employeeService = EmployeeService()
        super().__init__(Customer())

    def __getNewCustomerNumber(self):
        temp = self.getFirst(order="customerNumber desc")
        if(temp == None):
            return 1
        else:
            return temp.customerNumber + 1

    def addCustomer(self,data:Customer,employeeName:str):
        data.customerNumber = self.__getNewCustomerNumber()
        employee  = CustomerService.employeeService.searchByName(employeeName)
        if(employee == None):
            raise Exception("Employee not found")
        data.salesRepEmployeeNumber = employee.employeeNumber
        self.add(data)