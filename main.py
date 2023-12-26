import mysql.connector
class Test:
  mydb=str()
  mycursor=str()
  def __init__(self):
    self.mydb = mysql.connector.connect(host="localhost",user="root",password="")
    self.mycursor = self.mydb.cursor()
    self.mycursor.execute("use classicmodels")  
  def show_all_in_table(self,tbname):  
    self.mycursor.execute(f"select * from {tbname}")
    myresult = self.mycursor.fetchall()
    for x in myresult:
       print(x)
  def add_customer(self,fname,lname,datalist):
    sql=f"""select employeenumber from 
    employees where firstname='{fname}' and 
     lastname='{lname}'"""
    self.mycursor.execute(sql)
    myresult = self.mycursor.fetchall()
    emnum=list(myresult)[0][0]
    sql="select max(customerNumber) from customers"
    self.mycursor.execute(sql)
    myresult = self.mycursor.fetchall()
    cn=int(list(myresult)[0][0])+1
    
    sql=f"""
    insert  into customers(
        customerNumber,
        customerName,
        contactLastName,
        contactFirstName,
        phone,
        addressLine1,
        addressLine2,
        city,
        state,
        postalCode,
        country,
        salesRepEmployeeNumber,
        creditLimit) 
        values ({cn},
        '{datalist[0]}',
        '{datalist[1]}',
        '{datalist[2]}',
        '{datalist[3]}',
        '{datalist[4]}',
        '{datalist[5]}',
        '{datalist[6]}',
        '{datalist[7]}',
        '{datalist[8]}',
        '{datalist[9]}',
        {emnum},
        '{datalist[10]}')"""
    self.mycursor.execute(sql)
    self.mydb.commit()
    
ob=Test()
# To show all data in table use:
#ob.show_all_in_table("employees")"""
# To add data into cutomer Table use:
# datalist=["a","a","a","a","a","a","a","a","a","a",1370,"a"]
# you need to specify employee name and last name example:
#ob.add_customer("Diane","Murphy",datalist)
