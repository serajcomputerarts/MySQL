from databaseClasses.table import  Table
from databaseClasses.column import  Column ,ColumnDataType

class  ProductLine(Table):
    productLine : Column('productLine',ColumnDataType.idString) = ''
    textDescription : Column('textDescription',ColumnDataType.string,True) = ''
    htmlDescription : Column('htmlDescription', ColumnDataType.string,True) = ''
    image : Column('image', ColumnDataType.blob) = ''

    def __init__(self):
        super().__init__("productlines")
    