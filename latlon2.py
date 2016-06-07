#!/usr/bin/env python
import re

def decimalat(DegreeString):
	# Converts a string for latitude ot longitude into a float
	SearchString = '(\d+) ([\d.]+) (\w)'
	Result = re.search( SearchString, DegreeString )
	
	Degree = float( Result.group( 1 ) )
	Minute = float( Result.group( 2 ) )
	Compass = Result.group( 3 )
	DecimalDegree = Degree + Minute / 60

	if Compass in 'SW':
		DecimalDegree = - DecimalDegree

	return DecimalDegree


InFileName = 'Marrus_claudanielis.txt'

InFile = open( InFileName, 'r')

Linenumber = 0

for Line in InFile:
	Line = Line.strip()

	if Linenumber > 0:
		#print ( Linenumber )
		#print ( Line )
		ElementList = Line.split( '\t' )
		#print( ElementList )
		print( 'Depth:{} Lat:{} Lon:{}'.format( ElementList[4], ElementList[2], ElementList[3] ) )

		latitude = decimalat( ElementList[ 2 ] )

		print (latitude)

	Linenumber = Linenumber + 1

InFile.close()