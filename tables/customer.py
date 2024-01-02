from databaseClasses.table import  Table
from databaseClasses.column import  Column ,ColumnDataType

class  Customer(Table):
    customerNumber : Column('customerNumber',ColumnDataType.id) = 0
    customerName : Column('customerName',ColumnDataType.string) = ''
    contactLastName : Column('contactLastName', ColumnDataType.string) = ''
    contactFirstName : Column('contactFirstName', ColumnDataType.string) = ''
    phone : Column('phone', ColumnDataType.string) = ''
    addressLine1 : Column('addressLine1', ColumnDataType.string) = ''
    addressLine2 : Column('addressLine2', ColumnDataType.string,True) = ''
    city : Column('city', ColumnDataType.string) = ''
    state : Column('state', ColumnDataType.string,True) = ''
    postalCode : Column('postalCode', ColumnDataType.string,True) = ''
    country : Column('country', ColumnDataType.string) = ''
    salesRepEmployeeNumber : Column('salesRepEmployeeNumber', ColumnDataType.int) = 0
    creditLimit : Column('creditLimit', ColumnDataType.float) = 0

    def __init__(self):
        super().__init__("customers")
    
