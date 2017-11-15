"""
MySQL setup: (commands given in monitor accessible through ~mysql -h localhost -u root -p~)
CREATE DATABASE authenticator;
USE authenticator;
CREATE TABLE history (indx serial PRIMARY KEY, time datetime, kind varchar(10), name varchar(50));
"""
import mysql.connector

mySQLUser="root"
mySQLPassword="*****" #add real password before calling any function
mySQLHost="localhost"
mySQLDatabase="authenticator"

def DBWrite(name,kind):
	try:
		connection=mysql.connector.connect(user=mySQLUser, password=mySQLPassword, host=mySQLHost, database=mySQLDatabase)
		cur=connection.cursor()
		cur.execute("INSERT INTO history VALUES (DEFAULT,NOW(),'"+kind+"','"+name+"');")
		connection.commit()
		cur.close()
		connection.close()
		return 0
	except:
		return 1

def DBReadAll():
	try:
		connection=mysql.connector.connect(user=mySQLUser, password=mySQLPassword, host=mySQLHost, database=mySQLDatabase)
		cur=connection.cursor()
		cur.execute("SELECT * FROM history;")
		ret=[]
		for i in cur:
			ret+=[[i[1].isoformat(" "),i[2],i[3]]]
		cur.close()
		connection.close()
		return ret
	except:
		return "ERROR"

def DBRead(name):
	try:
		connection=mysql.connector.connect(user=mySQLUser, password=mySQLPassword, host=mySQLHost, database=mySQLDatabase)
		cur=connection.cursor()
		cur.execute("SELECT * FROM history WHERE name='"+name+"';")
		ret=[]
		for i in cur:
			ret+=[[i[1].isoformat(" "),i[2],i[3]]]
		cur.close()
		connection.close()
		return ret
	except:
		return "ERROR"

#DBWrite("Lucas","Entrada")
#DBWrite("Lucas","Saida")
#print DBReadAll()
#print DBRead("Lucas")
