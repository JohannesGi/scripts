#!/usr/bin/env python
import re
import sys


def decimalat( DegreeString ):
	# Converts a string for latitude or longitude into a float
	SearchString = '(\d+) ([\d.]+) (\w)'
	Result = re.search( SearchString, DegreeString )
	
	Degree = float( Result.group( 1 ) )
	Minute = float( Result.group( 2 ) )
	Compass = Result.group( 3 )
	DecimalDegree = Degree + Minute / 60

	if Compass in 'SW':
		DecimalDegree = - DecimalDegree

	return DecimalDegree

assert( decimalat('36 30.0 N') == 36.5 )
assert( decimalat('36 30.0 S') == -36.5 )
assert( decimalat('36 30.0 W') == -36.5 )
#assetions are like little spies testing your code (eg function). If not true, the programm will abort.

arguments = sys.argv
print arguments

InFileName = sys.argv[ 1 ]

#InFileName = 'Marrus_claudanielis.txt'

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