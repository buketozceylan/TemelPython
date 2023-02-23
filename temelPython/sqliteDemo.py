import sqlite3

def selectOperations():

    connection = sqlite3.connect("chinook.db")

    # cursor = connection.execute(" select FirstName,LastName from customers where city='Paris' or country='Brazil' order by FirstName asc" )
    # for row in cursor:
    #     print("First Name = "+row[0])
    #     print("Last Name = "+srow[1])
    #     print("*************")
    
    # cursor = connection.execute(" select city,count(*) from customers group by city having count(*)>1 order by count(*)" )
    # for row in cursor:
    #     print("City = "+row[0])
    #     print("Count = "+str(row[1]))
    #     print("*************")
    
    cursor = connection.execute("select FirstName,LastName from customers where FirstName like '%a'")
    for row in cursor:
        print("First Name = "+row[0])
        print("Last Name = "+row[1])
        print("*************")
    
    
    connection.close()

selectOperations()
def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("insert into customers (firstName,lastName,City,email) values('Bukis','Ozceylan','Izmir','buketozceylan@outlook.com')")
    connection.commit()
    connection.close()
    
    
#insertCustomer()

def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("update customers set city ='Ankara' where city='Izmir'")
    connection.commit()
    connection.close()
    
#updateCustomer()

def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("delete from customers where city='Ankara'")
    connection.commit()
    connection.close()
    
deleteCustomer()

def joinOperations():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("select albums.Title, artists.Name from artists inner join albums on artists.ArtistId = albums.ArtistId")
    for row in cursor:
        print("Title = "+row[0]+ "Name = "+row[1])
       
    
    
    connection.close()
    
joinOperations()
















