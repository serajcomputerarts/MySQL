from databaseClasses.table import  Table
from databaseClasses.column import  Column ,ColumnDataType

class  Product(Table):
    productCode : Column('productCode',ColumnDataType.idString) = ''
    productName : Column('productName',ColumnDataType.string) = ''
    productLine : Column('productLine',ColumnDataType.string) = ''
    productScale : Column('productScale',ColumnDataType.string) = ''
    productVendor : Column('productVendor',ColumnDataType.string) = ''
    productDescription : Column('productDescription',ColumnDataType.string) = ''
    quantityInStock : Column('quantityInStock',ColumnDataType.int) = 0
    buyPrice : Column('buyPrice',ColumnDataType.float) = 0
    MSRP : Column('MSRP',ColumnDataType.float) = 0

    def __init__(self):
        super().__init__("products")
    