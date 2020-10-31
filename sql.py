import mysql.connector
con = mysql.connector.connect(user='root', password = 'tigermanudon!1234' , host='127.0.0.1')
mycursor=con.cursor()
mycursor.execute("Create database Engineer")
mycursor.execute(" use engineer")
mycursor.execute(""" create table tb1(id int primary key,
name varchar(30),
salary int,
city varchar(30))""")