import mysql.connector
from databaseClasses.table import Table
from databaseClasses.query import Query
from tables.customer import Customer
from tables.employee import Employee
from tables.office import Office
from tables.orderdetail import OrderDetail
from tables.order import Order
from tables.payment import Payment
from tables.productline import ProductLine
from tables.product import Product


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class Database :
    __con : str = None
    tables : list[Table] = [
        Customer(),
        Employee(),
        Office(),
        OrderDetail(),
        Order(),
        Payment(),
        ProductLine(),
        Product(),
    ]
    DataBaseName = "classicmodels"
    host="localhost"
    user="root"
    password="123456"
    __cur : str = None


    
    def __init__(self):
        if(Database.__con == None):
            Database.__con = mysql.connector.connect(host=self.host,user=self.user,password=self.password)
            Database.__cur = Database.__con.cursor()
            Database.__con.row_factory = dict_factory
            Database.__cur.execute(f"use {Database.DataBaseName}")



    def executeQuery(self,query : str = "",commit : bool = False):
        Database.__cur.execute(query)
        if(commit):
            Database.__con.commit()
        res = [dict_factory(Database.__cur, row) for row in Database.__cur.fetchall()]
        return res
    

