#!/usr/bin/python 
import os
import time
import sqlite3 as mydb 
import sys

""" Log Current Time, Temperature in Celsius and Fahrenheit 
    To an Sqlite3 database """
def logTime():
<<<<<<< HEAD
	con = mydb.connect('/home/pi/Tests/testTime.db') 
	with con:
	  
		cur = con.cursor()
		currentDate=time.strftime('%Y-%m-%d')
		currentTime=time.strftime('%H-%M-%S')
		cur.execute('INSERT INTO timeData(xDate,xTime) values(?,?)', (currentDate,currentTime))
		con.commit()
		cur.execute("SELECT * FROM TimeData")
		print(cur.fetchall())
		print "Time logged"
=======
	#connection to database 
	con = mydb.connect('/home/pi/Tests/testTime.db') 
	with con: #with the connection do this chunk
		cur = con.cursor()
		#gets date and time with specified formats
		currentDate=time.strftime('%Y-%m-%d')
		currentTime=time.strftime('%H-%M-%S')
	    #puts elemeents into the database called timeData that has colums date and time, the values being put in are currentDate and currentTime that we computed
		cur.execute('INSERT INTO timeData(xDate,xTime) values(?,?)', (currentDate,currentTime))
		con.commit()
		#selects the correct time database
		cur.execute("SELECT * FROM timeData")
		print(cur.fetchall()) #prints all
		print "Time logged" 
>>>>>>> 7080d1f8a58de5fcf007ceaab3c6782b204291f8
logTime()
