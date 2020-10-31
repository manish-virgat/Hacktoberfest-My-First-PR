import mysql.connector
con = mysql.connector.connect(user='root', password = 'tigermanudon!1234' , host='localhost')
mycursor=con.cursor()
mycursor.execute("Create database nkm")
mycursor.execute(" use nkm")
mycursor.execute(""" create table don(id int primary key,
name varchar(30),
salary int,
city varchar(30))"""
mycursor.execute("insert into don values(1,'muskaan',750000,'Australia')")
con.commit()
print("created")

mj




