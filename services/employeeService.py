from databaseClasses.tableRepository import TableRepository
from tables.employee import Employee
import random
import string


class EmployeeService(TableRepository):
    def  __init__(self):
        super().__init__(Employee())

    def searchByName(self,name:str):
        temp = self.getFirst(where=f"concat(firstName, ' ', lastName) like '%{name}%'")
        return temp
        

   