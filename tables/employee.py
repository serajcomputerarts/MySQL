from databaseClasses.table import  Table
from databaseClasses.column import  Column ,ColumnDataType

class  Employee(Table):
    employeeNumber : Column('employeeNumber',ColumnDataType.id) = 0
    lastName : Column('lastName',ColumnDataType.string) = ''
    firstName : Column('firstName', ColumnDataType.string) = ''
    extension : Column('extension', ColumnDataType.string) = ''
    email : Column('email', ColumnDataType.string) = ''
    officeCode : Column('officeCode', ColumnDataType.string) = ''
    reportsTo : Column('reportsTo', ColumnDataType.int,True) = 0
    jobTitle : Column('jobTitle', ColumnDataType.string) = ''

    def __init__(self):
        super().__init__("employees")
    
