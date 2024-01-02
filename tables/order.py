from databaseClasses.table import  Table
from databaseClasses.column import  Column ,ColumnDataType

class  Order(Table):
    orderNumber : Column('orderNumber',ColumnDataType.id) = 0
    orderDate : Column('orderDate',ColumnDataType.dateTime) = ''
    requiredDate : Column('requiredDate', ColumnDataType.dateTime) = ''
    shippedDate : Column('shippedDate', ColumnDataType.dateTime) = ''
    status : Column('status', ColumnDataType.string) = ''
    comments : Column('comments', ColumnDataType.string,True) = ''
    customerNumber : Column('customerNumber', ColumnDataType.int) = ''

    def __init__(self):
        super().__init__("orders")
    