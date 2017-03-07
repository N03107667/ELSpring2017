#!/usr/bin/python 
import os
import time
import sqlite3 as mydb 
import sys

""" Log Current Time, Temperature in Celsius and Fahrenheit 
    To an Sqlite3 database """
def logTime():
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
logTime()
