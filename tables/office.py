from databaseClasses.table import  Table
from databaseClasses.column import  Column ,ColumnDataType

class  Office(Table):
    officeCode : Column('officeCode',ColumnDataType.id) = 0
    city : Column('city',ColumnDataType.string) = ''
    phone : Column('phone', ColumnDataType.string) = ''
    addressLine1 : Column('addressLine1', ColumnDataType.string) = ''
    addressLine2 : Column('addressLine2', ColumnDataType.string,True) = ''
    state : Column('state', ColumnDataType.string,True) = ''
    country : Column('country', ColumnDataType.string) = ''
    postalCode : Column('postalCode', ColumnDataType.string) = ''
    territory : Column('territory', ColumnDataType.string) = ''

    def __init__(self):
        super().__init__("offices")
    