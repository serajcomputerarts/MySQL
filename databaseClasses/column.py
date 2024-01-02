from enum import Enum

class ColumnDataType(Enum):
    id = 1,
    idIncrement = 2,
    idFloat = 3,
    idString = 4,
    string = 5,
    dateTime = 6,
    bool = 7,
    int = 8,
    float = 9,
    blob = 10,


class Column:
    name = str()
    dataType = ColumnDataType
    nullable = bool()

    def __init__(self, name : str, dataType : ColumnDataType, nullable : bool = False):
        self.name = name
        self.dataType = dataType
        self.nullable = nullable

    def isPrimaryKey(self):
        return self.dataType == ColumnDataType.id or self.dataType == ColumnDataType.idIncrement or self.dataType == ColumnDataType.idFloat or self.dataType == ColumnDataType.idString

    def isIncrement(self):
        return self.dataType == ColumnDataType.idIncrement 
    
    def getSqlValue(self,item):
        temp = ""
        keys = vars(item).keys()
        if(self.name in keys):
            temp = vars(item)[self.name]
        if(self.dataType in [ColumnDataType.string,ColumnDataType.idString]):
            temp = f"'{temp}'"
        return temp
        