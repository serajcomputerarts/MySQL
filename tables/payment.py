from databaseClasses.table import  Table
from databaseClasses.column import  Column ,ColumnDataType

class  Payment(Table):
    customerNumber : Column('customerNumber',ColumnDataType.id) = 0
    checkNumber : Column('checkNumber',ColumnDataType.string) = ''
    paymentDate : Column('paymentDate', ColumnDataType.dateTime) = ''
    amount : Column('amount', ColumnDataType.float) = 0

    def __init__(self):
        super().__init__("payments")
    