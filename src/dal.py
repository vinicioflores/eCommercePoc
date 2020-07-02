import mysql.connector


#### Data Access Layer - will enapcsulate the SQL CRUD operations to the MySQL cluster

class DalHelper:
	ConnectorDb = ""
	
	def __init__ (self):
	# Here we use the DNS created using Kubernetes Netokwring services into our private VLAN for our MySQL pods, otherwise we'd need to address our cluster by IP (complicated) instead of DNS human-readable address
	# This is for achievement High Availabity of our data tier in case of hiccups - they always happen (*^-^) 
		self.ConnectorDb = mysql.connector.connect(host="mysql-master.default.svc.cluster.local",user="viniciof",password="4getmenot",database="dw")
		
	def Select (self, tablename):
		dataReader = self.ConnectorDb.cursor()
		dataReader.execute("SELECT * FROM " + str(tablename))
		return dataReader.fetchall()

	
		
	