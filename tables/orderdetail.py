from databaseClasses.table import  Table
from databaseClasses.column import  Column ,ColumnDataType

class  OrderDetail(Table):
    orderNumber : Column('orderNumber',ColumnDataType.id) = 0
    productCode : Column('productCode',ColumnDataType.string) = ''
    quantityOrdered : Column('quantityOrdered', ColumnDataType.int) = 0
    priceEach : Column('priceEach', ColumnDataType.float) = 0
    orderLineNumber : Column('orderLineNumber', ColumnDataType.int) = 0

    def __init__(self):
        super().__init__("orderdetails")
    